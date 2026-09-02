# Style and Format Customization

The site uses al-folio v1.x. Content is deliberately separated from appearance, so format changes do not require moving publications, projects, software, teaching, or CV data.

## Easy changes in `_config.yml`

These are the safest visual controls:

```yaml
navbar_fixed: true
footer_fixed: false
back_to_top: true
max_width: 1050px
enable_darkmode: true
enable_search: true
```

For example, changing `max_width` changes the reading width without touching any page content.

## Navigation

Each page in `_pages/` has:

```yaml
nav: true
nav_order: 5
```

Change `nav_order` to reorder menu items. Set `nav: false` to hide a page from the menu without deleting it.

## Colors and typography in al-folio v1.x

al-folio v1.x keeps its default style pipeline inside the `al_folio_core` gem. For a site-specific color or typography change, use a **local Sass override** under `_sass/` only when you actually need the change. Local files with the same path/name as the theme partial override the gem-owned default.

Because a local override shadows the upstream theme file, do not copy theme internals merely to make a small change. Start with `_config.yml` controls. When a Sass override is necessary, compare against the version supplied by the pinned `al_folio_core` gem and document the change.

After future dependency upgrades, use the al-folio override audit commands when available:

```bash
bundle exec al-folio upgrade overrides audit
```

## Layout changes

Default layouts and includes are provided by al-folio gems in v1.x. A file added locally under `_layouts/` or `_includes/` with the same path becomes a site-specific override. Use this only when a format change cannot be expressed through configuration or content.

## `assets/css/site-overrides.scss`

This repository contains `assets/css/site-overrides.scss` as a site-owned staging/documentation location for future small rules. It is intentionally not loaded in the first release because al-folio v1.x owns the CSS pipeline in the core gem. When a real visual customization is selected, migrate the rule into the appropriate local `_sass/` override rather than editing gem files.
