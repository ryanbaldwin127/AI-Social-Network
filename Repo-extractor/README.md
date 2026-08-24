# Repo Extractor

The GitHub Repo Extractor provides an expedient way to gather issue and PR data from GitHub repositories using the [GitHub REST API](https://docs.github.com/en/rest). See this repo's documentation for more information.

## Setup

1. Create and activate a virtual environment:

```sh
python -m venv .venv   # Only if the venv doesn’t exist yet
source .venv/bin/activate
```

2. install the correct version of Python, listed in `pyproject.toml`. Try [pyenv](https://github.com/pyenv/pyenv)!

3. Upgrade PIP: `python -m pip install --upgrade pip build`

4. Install your own project and therefore its dependencies: `python -m pip install -e .`

## Contributing

- Abide by the ["Conventional Commits"](https://www.conventionalcommits.org) specification for all commits.
- Using default settings for each, format and lint all Python contributions with [black](https://pypi.org/project/black/) and [pylint](https://pypi.org/project/pylint/) respectively.
