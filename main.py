import os

ENTRY_TEXT = "The pen lid: exists to be lost. It has one job — stay on the pen — and a 100% failure rate across every pen I have ever owned."

ENTRY_FILENAME = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
