#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit('PyYAML is required for validation: pip install pyyaml') from exc

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def require(path: str) -> Path:
    p = ROOT / path
    if not p.exists():
        error(f'missing required file: {path}')
    return p


def load_yaml(path: str):
    p = require(path)
    if not p.exists():
        return None
    try:
        return yaml.safe_load(p.read_text(encoding='utf-8'))
    except Exception as exc:
        error(f'invalid YAML {path}: {exc}')
        return None


def load_json(path: str):
    p = require(path)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception as exc:
        error(f'invalid JSON {path}: {exc}')
        return None


def validate_config() -> None:
    config = load_yaml('_config.yml')
    if not isinstance(config, dict):
        return
    expected = {
        'url': 'https://pedro-mejia-alvarez.github.io',
        'baseurl': '',
        'theme': 'al_folio_core',
    }
    for key, value in expected.items():
        if config.get(key) != value:
            error(f'_config.yml: {key!r} must be {value!r}')
    plugins = config.get('plugins', [])
    for plugin in ('al_folio_core', 'al_folio_cv', 'al_search', 'al_citations', 'jekyll-get-json', 'jekyll/scholar', 'jekyll-socials'):
        if plugin not in plugins:
            error(f'_config.yml: missing plugin {plugin}')
    al_folio = config.get('al_folio') or {}
    if al_folio.get('api_version') != 1:
        error('_config.yml: al_folio.api_version must be 1')
    if al_folio.get('style_engine') != 'tailwind':
        error('_config.yml: al_folio.style_engine must be tailwind')
    tailwind = al_folio.get('tailwind') or {}
    if not tailwind.get('version') or not tailwind.get('css_entry'):
        error('_config.yml: al_folio.tailwind version/css_entry must be configured')
    features = al_folio.get('features') or {}
    if not ((features.get('cv') or {}).get('enabled')):
        error('_config.yml: al_folio.features.cv.enabled must be true')
    json_loader = config.get('jekyll_get_json') or []
    if not any(isinstance(item, dict) and item.get('data') == 'resume' and item.get('json') == 'assets/json/resume.json' for item in json_loader):
        error('_config.yml: jekyll_get_json must load assets/json/resume.json as resume')
    if config.get('search_enabled') is not True:
        error('_config.yml: search_enabled must be true')


def validate_required_pages() -> None:
    for path in (
        '_pages/about.md',
        '_pages/research.md',
        '_pages/publications.md',
        '_pages/books.md',
        '_pages/projects.md',
        '_pages/software.md',
        '_pages/students.md',
        '_pages/teaching.md',
        '_pages/cv.md',
        '_pages/404.md',
    ):
        require(path)


def validate_navigation() -> None:
    expected = {
        '_pages/about.md': ('Home', 1),
        '_pages/research.md': ('Research', 2),
        '_pages/publications.md': ('Publications', 3),
        '_pages/books.md': ('Books', 4),
        '_pages/projects.md': ('Projects', 5),
        '_pages/software.md': ('Software', 6),
        '_pages/students.md': ('Students', 7),
        '_pages/teaching.md': ('Teaching', 8),
        '_pages/cv.md': ('CV', 9),
    }
    for path, (title, order) in expected.items():
        p = ROOT / path
        if not p.exists():
            continue
        text = p.read_text(encoding='utf-8')
        front = re.match(r'^---\n(.*?)\n---', text, flags=re.S)
        if not front:
            error(f'{path}: missing YAML front matter')
            continue
        try:
            data = yaml.safe_load(front.group(1)) or {}
        except Exception as exc:
            error(f'{path}: invalid front matter: {exc}')
            continue
        if data.get('title') != title:
            error(f'{path}: title must be {title!r}')
        if data.get('nav_order') != order:
            error(f'{path}: nav_order must be {order}')
        if data.get('nav') is not True:
            error(f'{path}: nav must be true')



def validate_home_identity() -> None:
    p = ROOT / '_pages/about.md'
    if not p.exists():
        return
    text = p.read_text(encoding='utf-8')
    required = (
        'Pedro Mejia-Alvarez',
        'Professor and Researcher in Artificial Intelligence, Real-Time Systems, and Software Engineering',
        'CINVESTAV',
    )
    for phrase in required:
        if phrase not in text:
            error(f'_pages/about.md: missing required identity phrase: {phrase}')
    front = re.match(r'^---\n(.*?)\n---', text, flags=re.S)
    if front:
        data = yaml.safe_load(front.group(1)) or {}
        profile = data.get('profile')
        if isinstance(profile, dict) and profile.get('image'):
            image = ROOT / 'assets' / 'img' / str(profile['image'])
            if not image.exists():
                error(f'_pages/about.md: profile image does not exist: assets/img/{profile["image"]}')



def validate_research() -> None:
    data = load_yaml('_data/research.yml')
    if data is None:
        return
    if not isinstance(data, list):
        error('_data/research.yml: expected a list')
        return
    ids = [item.get('id') for item in data if isinstance(item, dict)]
    if len(ids) != len(set(ids)):
        error('_data/research.yml: research ids must be unique')
    required = {
        'real-time-systems',
        'real-time-operating-systems',
        'energy-aware-computing',
        'real-time-cybersecurity',
        'artificial-intelligence',
        'software-engineering',
        'software',
        'embedded-dependable-systems',
        'real-time-databases',
    }
    missing = sorted(required - set(ids))
    if missing:
        error(f'_data/research.yml: missing required research ids: {missing}')
    for item in data:
        if not isinstance(item, dict):
            error('_data/research.yml: every item must be a mapping')
            continue
        for key in ('id', 'title', 'summary'):
            if not item.get(key):
                error(f'_data/research.yml: item missing {key}')



def validate_publications_and_books() -> None:
    bib = require('_bibliography/papers.bib')
    if bib.exists():
        text = bib.read_text(encoding='utf-8')
        entries = re.findall(r'^@(article|inproceedings|incollection|misc|book)\{([^,]+),', text, flags=re.M | re.I)
        keys = [key for _, key in entries]
        if len(entries) < 50:
            error(f'_bibliography/papers.bib: expected at least 50 scholarly entries, found {len(entries)}')
        if len(keys) != len(set(keys)):
            error('_bibliography/papers.bib: BibTeX keys must be unique')
        if sum(1 for kind, _ in entries if kind.lower() == 'article') < 18:
            error('_bibliography/papers.bib: expected at least 18 journal article entries')
        if sum(1 for kind, _ in entries if kind.lower() == 'inproceedings') < 35:
            error('_bibliography/papers.bib: expected at least 35 international conference entries')
        forbidden_spanish_titles = {
            'Tolerancia a Fallos en Sistemas de Tiempo Real',
            'Kernel de Tiempo Real Distribuido',
        }
        for title in forbidden_spanish_titles:
            if title in text:
                error(f'_bibliography/papers.bib: public title must be English: {title}')
    required_books = {
        '2018-interrupt-handling.md',
        '2022-main-memory-management.md',
        '2023-real-time-database-systems.md',
        '2024-exception-handling.md',
        '2025-integrated-circuit-design.md',
    }
    books_dir = ROOT / '_books'
    if not books_dir.exists():
        error('missing required directory: _books')
    else:
        missing = sorted(required_books - {p.name for p in books_dir.glob('*.md')})
        if missing:
            error(f'_books: missing required book records: {missing}')



def _ids_from_yaml(path: str) -> set[str]:
    data = load_yaml(path)
    if not isinstance(data, list):
        if data is not None:
            error(f'{path}: expected a list')
        return set()
    ids: list[str] = []
    for item in data:
        if not isinstance(item, dict) or not item.get('id'):
            error(f'{path}: every item must have an id')
            continue
        ids.append(str(item['id']))
    if len(ids) != len(set(ids)):
        error(f'{path}: ids must be unique')
    return set(ids)


def validate_projects_and_software() -> None:
    research_ids = _ids_from_yaml('_data/research.yml')
    project_ids = _ids_from_yaml('_data/projects.yml')
    software_ids = _ids_from_yaml('_data/software.yml')
    if not project_ids or not software_ids:
        return
    bib_path = ROOT / '_bibliography/papers.bib'
    bib_keys: set[str] = set()
    if bib_path.exists():
        bib_keys = set(re.findall(r'^@\w+\{([^,]+),', bib_path.read_text(encoding='utf-8'), flags=re.M))
    projects = load_yaml('_data/projects.yml') or []
    for item in projects:
        for key in ('title', 'dates', 'role', 'summary'):
            if not item.get(key):
                error(f'_data/projects.yml: {item.get("id")} missing {key}')
        for rid in item.get('research', []) or []:
            if rid not in research_ids:
                error(f'_data/projects.yml: {item.get("id")} references unknown research id {rid}')
        for sid in item.get('software', []) or []:
            if sid not in software_ids:
                error(f'_data/projects.yml: {item.get("id")} references unknown software id {sid}')
    software = load_yaml('_data/software.yml') or []
    for item in software:
        for key in ('name', 'purpose', 'status', 'research'):
            if not item.get(key):
                error(f'_data/software.yml: {item.get("id")} missing {key}')
        for rid in item.get('research', []) or []:
            if rid not in research_ids:
                error(f'_data/software.yml: {item.get("id")} references unknown research id {rid}')
        for pid in item.get('projects', []) or []:
            if pid not in project_ids:
                error(f'_data/software.yml: {item.get("id")} references unknown project id {pid}')
        for paper in item.get('papers', []) or []:
            if paper not in bib_keys:
                error(f'_data/software.yml: {item.get("id")} references unknown BibTeX key {paper}')
        if item.get('repository') == 'TBD':
            error(f'_data/software.yml: {item.get("id")} must not claim a TBD repository')



def validate_students_and_teaching() -> None:
    students = load_yaml('_data/students.yml')
    if students is not None:
        if not isinstance(students, dict):
            error('_data/students.yml: expected a mapping')
        else:
            phd = students.get('phd', []) or []
            msc = students.get('msc', []) or []
            postdoc = students.get('postdoctoral', []) or []
            if len(phd) < 3:
                error('_data/students.yml: expected at least 3 PhD supervision records')
            if len(msc) < 30:
                error('_data/students.yml: expected at least 30 MSc supervision records')
            if len(postdoc) < 2:
                error('_data/students.yml: expected at least 2 postdoctoral records')
            for group_name, group in students.items():
                if not isinstance(group, list):
                    error(f'_data/students.yml: {group_name} must be a list')
                    continue
                for item in group:
                    for key in ('name', 'title'):
                        if not item.get(key):
                            error(f'_data/students.yml: {group_name} entry missing {key}')
    teaching = load_yaml('_data/teaching.yml')
    if teaching is not None:
        if not isinstance(teaching, dict):
            error('_data/teaching.yml: expected a mapping')
        else:
            families = teaching.get('course_families', []) or []
            titles = {f.get('title') for f in families if isinstance(f, dict)}
            required = {'Real-Time Systems', 'Operating Systems', 'Software Engineering', 'Software Testing and Reliability'}
            missing = sorted(required - titles)
            if missing:
                error(f'_data/teaching.yml: missing required course families: {missing}')
            if len(teaching.get('history', []) or []) < 35:
                error('_data/teaching.yml: expected at least 35 detailed teaching-history records')



def validate_cv() -> None:
    data = load_json('assets/json/resume.json')
    if data is None:
        return
    if not isinstance(data, dict):
        error('assets/json/resume.json: expected a JSON object')
        return
    basics = data.get('basics') or {}
    if basics.get('name') != 'Pedro Mejia-Alvarez':
        error('assets/json/resume.json: basics.name must be Pedro Mejia-Alvarez')
    if 'CINVESTAV' not in str(basics.get('summary', '')):
        error('assets/json/resume.json: basics.summary must mention CINVESTAV')
    education = data.get('education') or []
    if len(education) < 4:
        error('assets/json/resume.json: expected at least 4 education/training records')
    work = data.get('work') or []
    if len(work) < 5:
        error('assets/json/resume.json: expected at least 5 professional/visiting appointment records')
    awards = data.get('awards') or []
    if len(awards) < 3:
        error('assets/json/resume.json: expected at least 3 award/distinction records')
    service = data.get('volunteer') or []
    if len(service) < 8:
        error('assets/json/resume.json: expected at least 8 professional-service records')
    custom = data.get('academicRecord') or {}
    for key in ('invitedTalks', 'collaborations', 'citationMetricsAsRecordedIn2025CV'):
        if not custom.get(key):
            error(f'assets/json/resume.json: academicRecord.{key} must be populated')



def validate_deployment_workflow() -> None:
    p = require('.github/workflows/deploy.yml')
    if not p.exists():
        return
    text = p.read_text(encoding='utf-8')
    required_fragments = (
        'branches: [main]',
        'python3 -m pip install',
        'pyyaml',
        'bundle exec jekyll build',
        'JamesIves/github-pages-deploy-action@v4',
        'branch: gh-pages',
    )
    lowered = text.lower()
    for fragment in required_fragments:
        if fragment.lower() not in lowered:
            error(f'.github/workflows/deploy.yml: missing deployment requirement: {fragment}')


def validate_gemfile_wiring() -> None:
    p = require('Gemfile')
    if not p.exists():
        return
    text = p.read_text(encoding='utf-8')
    required_gems = (
        'jekyll', 'jekyll-get-json', 'jekyll-scholar', 'jekyll-socials',
        'al_folio_core', 'al_folio_cv', 'al_citations', 'al_search',
    )
    for gem in required_gems:
        if not re.search(rf'gem\s+[\"\']{re.escape(gem)}[\"\']', text):
            error(f'Gemfile: missing required gem {gem}')

def main() -> int:
    validate_config()
    validate_gemfile_wiring()
    validate_deployment_workflow()
    validate_required_pages()
    validate_navigation()
    validate_home_identity()
    validate_research()
    validate_publications_and_books()
    validate_projects_and_software()
    validate_students_and_teaching()
    validate_cv()
    if ERRORS:
        print('CONTENT VALIDATION FAILED')
        for item in ERRORS:
            print(f'- {item}')
        return 1
    print('CONTENT VALIDATION PASSED')
    return 0


if __name__ == '__main__':
    sys.exit(main())
