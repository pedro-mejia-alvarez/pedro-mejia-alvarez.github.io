---
layout: page
title: Software
permalink: /software/
nav: true
nav_order: 6
---

Software is an integral part of my research and engineering work. This page includes **research software used in papers**, **software developed in funded projects**, **historical engineering software**, and **new open research artifacts** as they become available on GitHub.

A software item is not described as open source or publicly downloadable unless a real repository or download link is available.

{% for sw in site.data.software %}
<a id="{{ sw.id }}"></a>
## {{ sw.name }}

**Status:** {{ sw.status }}{% if sw.platform %}  
**Platform / toolchain:** {{ sw.platform }}{% endif %}

{{ sw.purpose }}

{% if sw.paper_titles and sw.paper_titles.size > 0 %}
**Related publication(s):**
{% for title in sw.paper_titles %}
{% assign idx = forloop.index0 %}
- [{{ title }}]({{ '/publications/#' | append: sw.papers[idx] | relative_url }})
{% endfor %}
{% endif %}

{% if sw.projects and sw.projects.size > 0 %}
**Related project(s):**
{% for pid in sw.projects %}
{% assign pr = site.data.projects | where: "id", pid | first %}
- {% if pr %}{{ pr.title }}{% else %}{{ pid }}{% endif %}
{% endfor %}
{% endif %}

{% if sw.repository %}**Repository:** [GitHub / source]({{ sw.repository }})  
{% else %}**Public repository:** not currently linked.  
{% endif %}
{% if sw.documentation %}**Documentation:** [documentation]({{ sw.documentation }})  
{% endif %}
{% if sw.note %}_{{ sw.note }}_{% endif %}

{% endfor %}
