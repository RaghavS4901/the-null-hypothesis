import hashlib
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHECKSUM_FILE = PROJECT_ROOT / "checksums.txt"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if not CHECKSUM_FILE.exists():
        print("checksums.txt not found.")
        return 1

    failures = 0
    lines = CHECKSUM_FILE.read_text(encoding="utf-8").splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            print(f"Skipping malformed line: {line}")
            failures += 1
            continue

        expected, rel_path = parts
        target = PROJECT_ROOT / rel_path.strip()
        if not target.exists():
            print(f"MISSING  {rel_path}")
            failures += 1
            continue

        actual = sha256_file(target)
        if actual.lower() == expected.lower():
            print(f"OK       {rel_path}")
        else:
            print(f"MISMATCH {rel_path}")
            print(f"  expected: {expected}")
            print(f"  actual:   {actual}")
            failures += 1

    if failures:
        print(f"\nChecksum verification failed for {failures} file(s).")
        return 1

    print("\nAll checksums verified successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
