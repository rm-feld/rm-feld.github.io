import { resolveRelative, type SimpleSlug } from "@quartz-community/utils"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

// Hardcoded top nav — edit this list to add/remove/reorder tabs.
// `slug` should match the target file's path (without .md), relative to `content/`.
const navItems: { label: string; slug: SimpleSlug }[] = [
  { label: "Home", slug: "index" as SimpleSlug },
  { label: "Vault", slug: "vault/index" as SimpleSlug },
  { label: "Research", slug: "research" as SimpleSlug },
  { label: "Publications", slug: "publications" as SimpleSlug },
]

const TopNav: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const slug = fileData.slug!
  return (
    <nav class={`top-nav ${displayClass ?? ""}`}>
      <ul>
        {navItems.map((item) => (
          <li>
            <a href={resolveRelative(slug, item.slug)}>{item.label}</a>
          </li>
        ))}
      </ul>
    </nav>
  )
}

TopNav.css = `
.top-nav {
  flex: none;
}
.top-nav ul {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1.5rem;
  list-style: none;
  margin: 0;
  padding: 0;
}
.top-nav a {
  font-family: var(--headerFont);
  font-weight: 600;
  font-size: 1rem;
  color: var(--dark);
  text-decoration: none;
  white-space: nowrap;
}
.top-nav a:hover {
  color: var(--tertiary);
}
`

export default (() => TopNav) satisfies QuartzComponentConstructor
