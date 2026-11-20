# Repository Guidelines

## Versioning

- Releases use SemVer-style tags: `vMAJOR.MINOR.PATCH` with two-digit zero-padded components, for example `v00.01.00`.
- Strict SemVer forbids leading zeros; this repository intentionally uses the zero-padded form above. Keep the same width in every release.
- Current version: `00.01.00`.
- Bump rules:
  - **MAJOR**: breaking change, such as removing or renaming a config option.
  - **MINOR**: backward-compatible feature, such as a new sortable column.
  - **PATCH**: backward-compatible bug fix.

Before tagging, update the version in all of these places:

- `addon/manifest.json` → `human_version`
- `scripts/build.py` → `VERSION`
- `CHANGELOG.md` → new heading
- `README.md` → generated `.ankiaddon` filename

Then commit on `main` and push an annotated tag:

```bash
git tag -a v00.01.00 -m "Release 00.01.00"
git push origin main --follow-tags
```

Pushing a `v*` tag triggers `.github/workflows/release.yml`, which builds the `.ankiaddon` and publishes the GitHub Release automatically. Do not upload the artifact manually and do not edit a published tag — create a new PATCH tag instead.

## Project layout

- `addon/` → contents placed at the root of the `.ankiaddon` archive.
- `scripts/build.py` → build script; excludes `__pycache__` and `.pyc` files.
- `.github/workflows/release.yml` → release workflow.
- `AGENTS.md` → this file.

## Validation

```bash
python3 scripts/build.py
python3 -m json.tool addon/manifest.json
python3 -m json.tool addon/config.json
```

After building, check that the archive contains `__init__.py`, `manifest.json`, `config.json` and `config.md` at the root, with no `__pycache__` folder. Then install it in Anki and verify all four column headers, subdeck grouping and the direction indicator.
