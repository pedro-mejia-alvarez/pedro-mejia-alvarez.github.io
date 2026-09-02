# Adding Publications

Publications are stored in `_bibliography/papers.bib` and rendered by Jekyll Scholar/al-folio.

## Add one paper

Append a valid BibTeX record. Example:

```bibtex
@article{mejia2026example,
  author = {Mejia-Alvarez, Pedro and Example, Alice},
  title = {Example Research Article},
  journal = {Example Journal},
  year = {2026},
  volume = {1},
  number = {2},
  pages = {1--15},
  doi = {10.0000/example},
  bibtex_show = {true}
}
```

Use the real BibTeX key in software relationships. For example, a software item may contain:

```yaml
papers:
  - mejia2026example
```

## Optional al-folio fields

Useful optional fields include:

- `doi` — only when verified.
- `pdf` — local PDF filename/path when you are permitted to publish it.
- `code` — public code/repository URL.
- `website` — project or publication webpage.
- `preview` — image in `assets/img/publication_preview/`.
- `selected = {true}` — show the item among selected publications on the home page.

Do not invent DOI values, URLs, volume/issue data, or code links. If the source does not contain them, leave them absent until verified.
