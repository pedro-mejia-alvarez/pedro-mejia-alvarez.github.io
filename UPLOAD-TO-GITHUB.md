# Uploading This Site to GitHub Pages

The target repository is `pedro-mejia-alvarez.github.io` and the public address is:

`https://pedro-mejia-alvarez.github.io/`

## First installation

1. Download and extract the website package on your computer.
2. Open the GitHub repository `pedro-mejia-alvarez.github.io`.
3. Keep the existing `web-page/` folder for now. It is the recovered old site and will continue to be available at `/web-page/` during the transition.
4. Upload the **contents of the extracted package** to the repository root. Do not upload the ZIP file itself.
5. Make sure the hidden `.github/` folder is uploaded. It contains the automatic deployment workflow.
6. Commit the upload to the `main` branch.
7. Open the repository's **Actions** tab and open **Build and deploy academic site**. The workflow should validate the content, install the al-folio/Jekyll dependencies, build the site, and publish `_site` to the `gh-pages` branch.
8. Open **Settings → Pages**. If GitHub Pages is not already configured for the generated branch, select **Deploy from a branch**, choose `gh-pages`, choose `/(root)`, and save.
9. Open `https://pedro-mejia-alvarez.github.io/` and inspect the new site.
10. Check the major sections: Research, Publications, Books, Projects, Software, Students, Teaching, and CV.
11. Only after the new site has been checked should the old `web-page/` folder be deleted.

## Normal updates later

Edit the source file for the content you want to change and commit it to `main`. GitHub Actions will rebuild and republish the website automatically.

Common files:

- Home biography: `_pages/about.md`
- Research areas: `_data/research.yml`
- Publications: `_bibliography/papers.bib`
- Books: `_books/`
- Projects: `_data/projects.yml`
- Software: `_data/software.yml`
- Students: `_data/students.yml`
- Teaching: `_data/teaching.yml`
- CV: `assets/json/resume.json`
- Navigation/site settings: `_config.yml`
- Social/contact links: `_data/socials.yml`

See `docs/EDITING.md`, `docs/ADDING-PUBLICATIONS.md`, `docs/ADDING-SOFTWARE.md`, and `docs/STYLE-CUSTOMIZATION.md` for detailed instructions.

## Important Git rule

Edit and commit source files on `main`. Do not edit the generated `gh-pages` branch by hand because the deployment workflow replaces it on every successful build.
