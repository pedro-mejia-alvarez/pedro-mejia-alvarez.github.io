---
layout: page
title: Research
permalink: /research/
nav: true
nav_order: 2
---

My research combines **real-time and embedded systems**, **artificial intelligence**, **software engineering**, and **dependable computing**. A recurring goal throughout this work is to connect formal or algorithmic ideas with executable software, experiments, and engineering platforms.

{% for area in site.data.research %}
## {{ area.title }}

{{ area.summary }}

**Topics:** {{ area.keywords | join: ", " }}.

{% endfor %}

The **Software** section documents research code, simulators, prototypes, libraries, operating-system components, and other artifacts associated with these research areas. As repositories for current work are made public, they can be linked directly from the corresponding publication and project entries.
