# Editing the Academic Website

This site is intentionally content-driven. Most routine updates require editing one Markdown, YAML, BibTeX, or JSON file; they do not require editing HTML templates.

## Content map

| What you want to change | File or directory |
| --- | --- |
| Home biography | `_pages/about.md` |
| Research areas | `_data/research.yml` |
| Publications | `_bibliography/papers.bib` |
| Books | `_books/` |
| Projects | `_data/projects.yml` |
| Research software | `_data/software.yml` |
| Student supervision | `_data/students.yml` |
| Teaching | `_data/teaching.yml` |
| Structured CV | `assets/json/resume.json` |
| Navigation order | front matter in `_pages/*.md` |
| Site width / navbar / dark mode / search | `_config.yml` |
| GitHub profile cards | `_data/repositories.yml` |
| Contact/social links | `_data/socials.yml` |

## Safe editing workflow

1. Edit the source file on the `main` branch.
2. Keep YAML indentation unchanged: use spaces, not tabs.
3. Run `python3 scripts/validate_content.py` if you are editing locally.
4. Commit and push the change.
5. GitHub Actions rebuilds the site automatically and writes the generated website to the `gh-pages` branch.

Do not edit the generated `gh-pages` branch by hand. It is overwritten by each deployment.

## Add a new page

Create a Markdown file in `_pages/`. A navigation page needs front matter such as:

```yaml
---
layout: page
title: New Section
permalink: /new-section/
nav: true
nav_order: 10
---
```

Then write the page in Markdown below the front matter.

## Add a profile photograph later

Place the photograph at `assets/img/prof_pic.jpg`, then add this block to `_pages/about.md` front matter before `selected_papers`:

```yaml
profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p>CINVESTAV, Guadalajara</p>
    <p>Mexico</p>
```

The first release intentionally has no placeholder photograph, so it cannot display a broken or invented image.

## Historical source policy

The 2025 CV is the canonical source for established historical facts in this release. When a new fact is known to be current, update the corresponding structured file. Do not silently convert an old expected date into a completed event unless completion is verified.
