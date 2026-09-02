# Pedro Mejia-Alvarez — Academic Website

Source for **https://pedro-mejia-alvarez.github.io/**.

This repository uses the al-folio v1.x architecture and keeps content separate from presentation so the site can be expanded or restyled later without rebuilding it.

## Main sections

**Home · Research · Publications · Books · Projects · Software · Students · Teaching · CV**

All public-facing website content is written in English. Research software is treated as a scholarly output and can be linked to the papers and projects that use it.

## Where to edit

- Biography/home: `_pages/about.md`
- Research areas: `_data/research.yml`
- Publications: `_bibliography/papers.bib`
- Books: `_books/`
- Projects: `_data/projects.yml`
- Software: `_data/software.yml`
- Students: `_data/students.yml`
- Teaching: `_data/teaching.yml`
- CV: `assets/json/resume.json`
- Site settings/navigation/width: `_config.yml`
- Contact/profile links: `_data/socials.yml`

Detailed editing instructions are in `docs/EDITING.md`, `docs/ADDING-PUBLICATIONS.md`, `docs/ADDING-SOFTWARE.md`, and `docs/STYLE-CUSTOMIZATION.md`.

## Automatic GitHub Pages deployment

Every push to `main` triggers `.github/workflows/deploy.yml`. The workflow validates the academic content, builds the Jekyll site, and publishes the generated website to the `gh-pages` branch.

For the first deployment in GitHub:

1. Keep your existing `web-page/` folder in the repository during the transition.
2. Copy these new site-source files into the **root** of `pedro-mejia-alvarez.github.io`.
3. Commit the files to the `main` branch.
4. Open **Actions** and confirm that **Build and deploy academic site** completes successfully.
5. Open **Settings → Pages** and choose **Deploy from a branch** if necessary.
6. Select branch **`gh-pages`** and folder **`/(root)`**, then save.
7. Open `https://pedro-mejia-alvarez.github.io/` after GitHub Pages publishes the build.

After that one-time setup, normal edits require only a commit to `main`; deployment is automatic.

## Preserving the recovered old site

The recovered historical site under `/web-page/` can remain in the source repository during transition. Jekyll treats it as static content and carries it into the generated website unless you explicitly delete or exclude it. Remove it only after the new root site has been checked.
