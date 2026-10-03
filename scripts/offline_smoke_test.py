"""Build the Version 2 corpus and run offline checks without API calls."""
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.triage_v2 import initialize_v2


def main():
    evidence = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "evidence" / "archives" / "version1_evidence.zip"
    output = ROOT / "local_outputs" / "offline_smoke_test"
    if output.exists():
        shutil.rmtree(output)
    _, corpus, _ = initialize_v2(evidence, output)
    if len(corpus) != 33:
        raise AssertionError(f"Expected 33 retrieval records, found {len(corpus)}")
    print("OFFLINE SMOKE TEST PASSED")


if __name__ == "__main__":
    main()
