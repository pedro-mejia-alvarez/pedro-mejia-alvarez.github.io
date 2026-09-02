# Site Content Source Notes

This file documents the provenance and deliberate normalization decisions used to build the first English version of Pedro Mejia-Alvarez's academic website.

## Primary source

**Curriculum Vitae 2025 — Dr. Pedro Mejia Alvarez** (`CV-PedroMejia-2025.doc`) is the canonical historical source for established education, publications, books, technological development, teaching, student supervision, reviewing/service, distinctions, funded projects, visiting appointments, invited talks, collaborations, and the citation metrics recorded in that document.

## Secondary source

The recovered historical website at `https://pedro-mejia-alvarez.github.io/web-page/` is a secondary reference. It should remain available during the transition and may be removed later after the new site has been checked.

## English-only normalization

The public website is written in English. Descriptive CV material and thesis/course/project descriptions were translated into English while preserving the source meaning. Official institution, publisher, conference, and product names are retained when they function as proper names.

The 1997 journal item recorded in the CV as **“Tolerancia a Fallos en Sistemas de Tiempo Real”** is displayed in the website bibliography as **“Fault Tolerance in Real-Time Systems”** to satisfy the English-only site requirement. This is a site translation of the title recorded in the source CV.

The 2005 conference item recorded in the CV as **“Kernel de Tiempo Real Distribuido”** is displayed as **“Distributed Real-Time Kernel”** for the same English-only presentation rule. This is also a site translation of the title recorded in the source CV.

## Deliberately unverified records

The 2025 CV uses an *expected graduation* date rather than a confirmed graduation date for several MSc entries. The site therefore marks these completion statuses as unverified:

- Jhonatan Alexander Gomez Gamboa — expected August 2024 in the source CV.
- Pedro Eduardo Torres Jimenez — expected November 2014 in the source CV.
- Francisco Javier Zuluaga Ramirez — expected November 2005 in the source CV.

No completion claim is made for these records until a confirmed date is supplied.

## Software availability

Historical software documented in the CV is described as research/engineering output, but the site does **not** claim that source code is publicly available unless a real public repository or download URL is supplied. This applies to SOPCO-family operating systems, MSB monitoring/debugging systems, LIBES libraries, SEDEL/GRAFCO/IAPSOPC work, and other historical tools.

Current or future paper-specific software can be added to `_data/software.yml` and linked to BibTeX paper keys and project IDs. Repository URLs are added only when verified.

## Research taxonomy

The site research taxonomy combines the historical record with the research identity and topics explicitly approved for the new website, including Artificial Intelligence, Real-Time Systems, Software Engineering, Software, and cybersecurity for real-time/cyber-physical systems. These taxonomy labels organize the public site; they are not intended to reproduce the headings of the 2025 CV verbatim.

## Historical citation metrics

The CV records the following values: 2,938 total citations; h-index 19; i10-index 30, with separate “since 2020” values. The structured CV stores them under `citationMetricsAsRecordedIn2025CV`. They are historical values from the source document and are not presented as live Google Scholar statistics.
