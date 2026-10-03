"""Verify every file recorded in SHA256SUMS.txt."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


failures = []
for line in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    expected, relative = line.split("  ", 1)
    path = ROOT / relative
    actual = digest(path) if path.exists() else "MISSING"
    if actual != expected:
        failures.append((relative, expected, actual))

if failures:
    raise SystemExit(f"Integrity verification failed: {failures}")
print("SUBMISSION INTEGRITY VERIFIED")
