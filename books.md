---
layout: page
title: Books
permalink: /books/
nav: true
nav_order: 4
---

I have authored and co-authored books on **operating systems, database systems, exception handling, and integrated-circuit design**. The records below are maintained independently so cover images, descriptions, software links, and related research material can be added without changing the page layout.

{% assign sorted_books = site.books | sort: "year" | reverse %}
{% for book in sorted_books %}
## [{{ book.title }}]({{ book.url | relative_url }})

**{{ book.authors }}**  
{{ book.publisher }}, {{ book.year }}.  
{% if book.isbn %}ISBN: {{ book.isbn }}. {% endif %}{% if book.doi %}DOI: [{{ book.doi }}](https://doi.org/{{ book.doi }}).{% endif %}

{{ book.content | markdownify }}
{% endfor %}
