---
layout: page
title: Students
permalink: /students/
nav: true
nav_order: 7
---

Graduate supervision has been an important part of my academic work. The records below are translated and structured from my 2025 curriculum vitae. Entries whose source records only an *expected* graduation date are explicitly marked as unverified rather than being presented as completed degrees.

## PhD supervision

{% for student in site.data.students.phd %}
**{{ student.name }}**  
*{{ student.title }}*  
{% if student.institution %}{{ student.institution }} · {% endif %}{{ student.completion }}{% if student.co_supervisors %} · Co-supervision: {{ student.co_supervisors | join: ", " }}{% endif %}

{% endfor %}

## MSc supervision

{% for student in site.data.students.msc %}
**{{ student.name }}**  
*{{ student.title }}*  
{% if student.institution %}{{ student.institution }} · {% endif %}{% if student.completion %}{{ student.completion }}{% endif %}{% if student.co_supervisors %} · Co-supervision: {{ student.co_supervisors | join: ", " }}{% endif %}{% if student.status == "unverified" %} · **Status note:** completion not verified in the source CV{% endif %}  
{% if student.note %}{{ student.note }}{% endif %}{% if student.source_note %}{{ student.source_note }}{% endif %}

{% endfor %}

## Undergraduate thesis supervision

{% for student in site.data.students.undergraduate %}
**{{ student.name }}** — *{{ student.title }}*  
{{ student.institution }}{% if student.completion %} · {{ student.completion }}{% endif %}

{% endfor %}

## Postdoctoral researchers

{% for researcher in site.data.students.postdoctoral %}
**{{ researcher.name }}** — {{ researcher.title }}  
{{ researcher.institution }} · {{ researcher.period }}  
{% if researcher.note %}{{ researcher.note }}{% endif %}

{% endfor %}
