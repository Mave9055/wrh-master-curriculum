# What Really Happened™ — WRH Master Curriculum

> **Non-clinical education. No required disclosure. Clear safety boundaries.**

WRH is a structured psychoeducational curriculum focused on survival literacy, system logic, nervous-system adaptation, practical language-building, and facilitator consistency. It is not therapy, diagnosis, medical advice, or a replacement for licensed care.

## Live site

The redesigned GitHub Pages site is available at **[daniel-lingar.github.io/wrh-master-curriculum](https://daniel-lingar.github.io/wrh-master-curriculum/)**.

The homepage is an orientation layer. The **[Curriculum Map](https://daniel-lingar.github.io/wrh-master-curriculum/curriculum/)** explains the four-part architecture, while the **[Session Explorer](https://daniel-lingar.github.io/wrh-master-curriculum/curriculum/session-viewer.html)** provides searchable reading access to all 77 source Markdown records.

## What changed in the redesign

The site now uses a dark editorial design system with responsive navigation, accessible focus states, reading-progress feedback, a branded partner mark, stronger page hierarchy, and a dedicated session-reading experience. The session explorer loads a generated static catalog, preserves the original source files, supports title/content search, provides previous/next navigation, and saves the last-read session locally in the browser.

The source folders currently contain **77 Markdown session files** across four parts. The source material includes two records labeled Session 12; the explorer keeps both records distinct by using part-plus-filename identifiers rather than silently renumbering or deleting content.

## Repository map

| Path | Purpose |
| --- | --- |
| `index.html` | Homepage, scope boundary, entry points, and curriculum map preview |
| `curriculum/index.html` | Four-part curriculum map and implementation entry points |
| `curriculum/session-viewer.html` | Searchable reader for the generated 77-record catalog |
| `curriculum/part-1.html` through `part-4.html` | Part-level overview pages |
| `Part-I/` through `Part-IV/` | Original source Markdown session content; source of truth |
| `assets/css/styles.css` | Global dark-mode design system and responsive component styles |
| `assets/js/main.js` | Navigation, progress tracking, session reader, search, and local reading state |
| `assets/data/sessions.json` | Generated static session catalog consumed by the explorer |
| `scripts/build_session_catalog.py` | Rebuilds `sessions.json` from the original Part-I through Part-IV Markdown |
| `docs/` | Safety, implementation, and supporting documentation |
| `404.html`, `robots.txt`, `sitemap.xml` | GitHub Pages error handling and SEO support |
| `Privacy_Policy.md`, `Terms_of_Use.md`, `LICENSE` | Repository-level legal and licensing documents |

## Local development

The site is intentionally static and can be previewed with any static HTTP server. From the repository root:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/`. The session explorer uses `fetch()` to load `assets/data/sessions.json`, so preview it through HTTP rather than opening the HTML file directly from the filesystem.

If source Markdown files change, rebuild the browser catalog:

```bash
python3 scripts/build_session_catalog.py
```

The build script uses Python-Markdown to generate HTML fragments and compact metadata. It does not modify the original Markdown files.

## Program architecture

| Part | Focus | Intended use |
| --- | --- | --- |
| **Part I** | Survival wiring and trauma literacy | Foundational pattern recognition and nervous-system language |
| **Part II** | Institutional systems and reentry | Practical navigation, advocacy, and systems friction |
| **Part III** | Resilience and autonomy | Agency, identity, sustainable change, and integrated models |
| **Part IV** | Facilitation and crisis management | Delivery standards, safety protocols, escalation, and implementation |

## Safety and scope

WRH is educational. Facilitators should review local crisis contacts, stop criteria, referral pathways, and site-specific policies before delivery. If someone is in immediate danger or acute crisis, pause the curriculum and use the local emergency or clinical support pathway defined by the program site.

See the [Safety and Escalation guide](docs/safety-and-escalation.html), [Implementation Guide](docs/implementation-guide.html), [Privacy Policy](privacy-policy.html), and [Terms of Use](terms-of-use.html) for additional context.

## About Capitol Contracts LLC

Capitol Contracts LLC develops structured, non-clinical psychoeducational materials and training frameworks for implementation partners.

- **UEI:** HH77KN5AV5X7
- **CAGE:** 9ZFJ6
- **Primary NAICS:** 611710 — Educational Support Services
- **Contact:** [capitolcontracts@outlook.com](mailto:capitolcontracts@outlook.com)

© 2026 Capitol Contracts LLC. What Really Happened™ is a trademark of Capitol Contracts LLC.
