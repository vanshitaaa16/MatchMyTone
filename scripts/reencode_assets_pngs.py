from __future__ import annotations

from pathlib import Path

from PIL import Image


def reencode_png(path: Path) -> None:
    img = Image.open(path)
    img.load()
    print(f"{path}: mode={img.mode} size={img.size} info={sorted(img.info.keys())}")

    # Re-encode to a simple, Android-safe PNG.
    # This removes problematic metadata/profiles and normalizes to 8-bit RGBA.
    out = img.convert("RGBA")
    out.save(path, format="PNG", optimize=True)

    img2 = Image.open(path)
    img2.load()
    print(f"  -> saved: mode={img2.mode} size={img2.size} info={sorted(img2.info.keys())}")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    targets = [
        root / "assets" / "color1.png",
        root / "assets" / "matchmytone-logo.png",
        root / "assets" / "splash-icon.png",
        root / "assets" / "normal.png",
    ]

    for p in targets:
        if not p.exists():
            print("MISSING", p)
            continue
        reencode_png(p)

    print("DONE")


if __name__ == "__main__":
    main()

