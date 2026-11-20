from __future__ import annotations

import json
import shutil
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ADDON = ROOT / "addon"
DIST = ROOT / "dist"
VERSION = "1.0.0"
OUTPUT = DIST / f"sort_by_due-{VERSION}.ankiaddon"
EXCLUDED_DIRS = {"__pycache__"}
EXCLUDED_SUFFIXES = {".pyc"}


def should_include(path: Path) -> bool:
    return not any(part in EXCLUDED_DIRS for part in path.parts) and (
        path.suffix not in EXCLUDED_SUFFIXES
    )


def build() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    manifest = json.loads((ADDON / "manifest.json").read_text(encoding="utf-8"))
    manifest["mod"] = int(time.time())

    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(ADDON.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(ADDON)
            if not should_include(relative):
                continue
            if relative.name == "manifest.json":
                archive.writestr(
                    "manifest.json", json.dumps(manifest, indent=2) + "\n"
                )
            else:
                archive.write(path, relative.as_posix())

    print(OUTPUT)


if __name__ == "__main__":
    build()
