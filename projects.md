---
layout: page
title: Projects
permalink: /projects/
nav: true
nav_order: 5
---

My research has included **national and international funded projects** as well as substantial **engineering and technological-development projects**. The selection below is derived from my 2025 CV. Historical funding amounts with ambiguous formatting in the source are intentionally not reproduced here until verified.

{% for project in site.data.projects %}
## {{ project.title }}

**Period:** {{ project.dates }}  
{% if project.funding %}**Funding / organization:** {{ project.funding }}  {% endif %}
**Role:** {{ project.role }}

{{ project.summary }}

{% if project.software and project.software.size > 0 %}
**Related software:**
{% for sid in project.software %}
{% assign sw = site.data.software | where: "id", sid | first %}
- {% if sw %}[{{ sw.name }}]({{ '/software/#' | append: sid | relative_url }}){% else %}{{ sid }}{% endif %}
{% endfor %}
{% endif %}

{% endfor %}
