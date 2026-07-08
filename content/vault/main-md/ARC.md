---
type: method
aliases: [arc]
tags: [stanford-stats/y2]
previous:
next:
modified: 2025-11-12T07:30:54-08:00
created: 2025-11-12T07:29:20-08:00
---

> [!todo] ARC
> Consider a linear 
> 1. Compute marginal and conditional likelihoods 
> 2. 


> [!abstract]- Properties
> > [!faq]- General Statements
> >```dataview 
> > list from "atoms" where contains(about, this.file.link)
> > ```
> 
> 
> > [!fail]- Forward Implications
> > ```dataview
> > list from "atoms" where contains(given, this.file.link)
> > ```
>
> > [!tldr]- Reverse Implications
> > ```dataview
> > list from "atoms" where contains(implies, this.file.link)
> > ```

> [!hint]- Motivation

> [!attention]- Context & Comparison
> 

> [!warning]- Warnings
> 

> [!example]- Examples
>
> ```dataview 
> list from "atoms" where (type="example" OR contains(class, "example")) AND (contains(about, this.file.link) OR contains(class, "fuck"))
 > ```



