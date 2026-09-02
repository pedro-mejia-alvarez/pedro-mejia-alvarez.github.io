---
layout: page
title: Teaching
permalink: /teaching/
nav: true
nav_order: 8
---

My teaching record spans graduate courses in real-time systems, operating systems, software engineering, software testing and reliability, and related advanced topics. The detailed history below is translated from my 2025 curriculum vitae.

## Main course areas

{% for family in site.data.teaching.course_families %}
### {{ family.title }}

{{ family.description }}

{% endfor %}

## Teaching history

| Course | Period | Institution | Hours |
| --- | --- | --- | ---: |
{% for item in site.data.teaching.history %}| {{ item.course }} | {{ item.period }} | {{ item.institution }}{% if item.category %} ({{ item.category }}){% endif %} | {{ item.hours }} |
{% endfor %}

The historical record preserves the course periods and contact hours stated in the source CV. It is intended as an academic record rather than a list of currently offered courses.
