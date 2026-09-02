# Adding Research Software

Research software is a first-class scholarly output in this site. The catalog lives in `_data/software.yml`.

Software may be:

- source code used to obtain results in a paper;
- a simulator or experimental framework;
- an operating-system component or library;
- a testing, debugging, or automated-repair tool;
- a prototype developed in a funded project;
- a public GitHub repository accompanying current research.

## Add an item

Example:

```yaml
- id: example-scheduler
  name: Example Real-Time Scheduler
  purpose: Experimental scheduler used to evaluate a scheduling method.
  status: research prototype
  platform: Linux
  research:
    - real-time-systems
    - software
  papers:
    - mejia2026example
  projects:
    - example-project-id
  repository: https://github.com/pedro-mejia-alvarez/example-scheduler
  documentation: https://github.com/pedro-mejia-alvarez/example-scheduler/blob/main/README.md
```

## Relationship rules

- Every value in `research` must match an `id` in `_data/research.yml`.
- Every value in `papers` must match a BibTeX key in `_bibliography/papers.bib`.
- Every value in `projects` must match an `id` in `_data/projects.yml`.
- A repository link is included only when the repository is actually public and known.

Run:

```bash
python3 scripts/validate_content.py
```

The validator reports broken research/project/paper relationships before deployment.
