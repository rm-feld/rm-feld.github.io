import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { componentRegistry } from "./quartz/components/registry"
import { ConditionalRender } from "./quartz/components"
import { PageTypes } from "./quartz/plugins"
import TopNavConstructor from "./quartz/components/TopNav"
import type { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./quartz/components/types"

const config = await loadQuartzConfig()

// --- Folder-scoped layout ---------------------------------------------------
// Pages whose slug lives under `vault/` (i.e. anything copied from website/vault/)
// get the full Quartz treatment (Explorer, Graph, Backlinks). Everything else
// (index, research, publications) gets a plain, uncluttered layout.
const isVaultPage = (props: QuartzComponentProps): boolean =>
  (props.fileData.slug ?? "").startsWith("vault/")

// Community "component-only" plugins (Explorer, Graph, Backlinks, Search, ...) are
// registered into componentRegistry by name during loadQuartzConfig() above — they
// aren't re-exported as callable constructors from .quartz/plugins, so we have to
// pull instances back out of the registry here in order to wrap/reposition them.
function getRegisteredComponent(name: string): QuartzComponent {
  const reg = componentRegistry.get(name) ?? componentRegistry.get(name[0].toUpperCase() + name.slice(1))
  if (!reg) {
    throw new Error(`quartz.ts: could not find component "${name}" in the component registry`)
  }
  if (typeof reg.component === "function" && !("displayName" in reg.component)) {
    const overrides = componentRegistry.getOptionOverrides(name)
    return componentRegistry.instantiate(
      reg.component as QuartzComponentConstructor,
      overrides && Object.keys(overrides).length > 0 ? overrides : undefined,
    )
  }
  return reg.component as QuartzComponent
}

const TopNav = TopNavConstructor()
const Search = getRegisteredComponent("search")
const PageTitle = getRegisteredComponent("page-title")
const Spacer = getRegisteredComponent("spacer")
const Darkmode = getRegisteredComponent("darkmode")
const ReaderMode = getRegisteredComponent("reader-mode")
const TableOfContents = getRegisteredComponent("table-of-contents")
const Explorer = getRegisteredComponent("explorer")

// Graph, Backlinks, etc. are "component-only" plugins (side-effect-imported,
// not run through the normal plugin factory pipeline) — the `options:` block
// under their entry in quartz.config.yaml is silently ignored for these.
// Overrides have to be registered here instead, before instantiation.
componentRegistry.setOptionOverrides("graph", {
  localGraph: { showTags: false },
  globalGraph: { showTags: false },
})
const Graph = getRegisteredComponent("graph")
const Backlinks = getRegisteredComponent("backlinks")

const customLayout = await loadQuartzLayout({
  defaults: {
    // Hardcoded top nav + search icon, shown on every page.
    header: [TopNav, Search],
  },
  byPageType: {
    content: {
      left: [
        PageTitle,
        Spacer,
        Darkmode,
        ReaderMode,
        ConditionalRender({ component: Explorer, condition: isVaultPage }),
      ],
      right: [
        ConditionalRender({ component: Graph, condition: isVaultPage }),
        ConditionalRender({ component: Backlinks, condition: isVaultPage }),
        TableOfContents,
      ],
    },
  },
})

// resolveLayout() in the dispatcher prefers a page-type's own `header` over the
// shared default whenever it's an array at all (even []), and loadQuartzLayout()
// force-sets every byPageType entry's header to [] before merging in overrides
// that don't mention `header`. So the nav has to be stamped onto every page type
// explicitly, not just left to fall through from `defaults`.
for (const pageType of Object.values(customLayout.byPageType)) {
  pageType.header = [TopNav, Search]
}

// loadQuartzConfig() already built a default PageTypeDispatcher emitter (using the
// *unmodified* layout) and pushed it into config.plugins.emitters. Swap it out for
// one built from our customized layout so the override above actually takes effect.
config.plugins.emitters = config.plugins.emitters.filter((e) => e.name !== "PageTypeDispatcher")
config.plugins.emitters.push(
  PageTypes.PageTypeDispatcher({
    defaults: customLayout.defaults,
    byPageType: customLayout.byPageType,
  }),
)

export default config
export const layout = customLayout
