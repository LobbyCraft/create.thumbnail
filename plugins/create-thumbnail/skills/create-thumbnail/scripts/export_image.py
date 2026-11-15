#!/usr/bin/env python3
"""Export approved artwork as correctly sized PNG and/or JPEG downloads."""
import argparse
from pathlib import Path
from PIL import Image, ImageColor, ImageOps

SIZES = {"thumbnail": (1920, 1080), "game-icon": (512, 512)}

def export_image(source, output_dir, kind, file_format="both", background="#FFFFFF"):
    size = SIZES[kind]
    output_dir = Path(output_dir)
    with Image.open(source) as opened:
        master = ImageOps.exif_transpose(opened).convert("RGBA")
    if master.width * size[1] != master.height * size[0]:
        raise ValueError("Aspect ratio differs from target; reframe the master before exporting.")
    if master.width < size[0] or master.height < size[1]:
        raise ValueError("Master is smaller than target; provide a higher-resolution master.")
    colour = ImageColor.getrgb(background)
    if len(colour) != 3:
        raise ValueError("Background must be an opaque RGB colour.")
    scaled = master.resize(size, Image.Resampling.LANCZOS)
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(source).stem
    paths = []
    for fmt in (("png", "jpeg") if file_format == "both" else (file_format,)):
        path = output_dir / (stem + "." + fmt)
        if path.resolve() == Path(source).resolve():
            raise ValueError("Export would overwrite the source master; choose another output directory.")
        if fmt == "png":
            scaled.save(path, format="PNG")
        else:
            flattened = Image.new("RGB", size, colour)
            flattened.paste(scaled, mask=scaled.getchannel("A"))
            flattened.save(path, format="JPEG", quality=95, subsampling=0, optimize=True)
        with Image.open(path) as check:
            if check.size != size or check.format != fmt.upper():
                raise ValueError("Export verification failed.")
        paths.append(path)
    return paths

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--kind", required=True, choices=SIZES)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--format", default="both", choices=("both", "png", "jpeg"))
    parser.add_argument("--background", default="#FFFFFF")
    args = parser.parse_args()
    try:
        for path in export_image(args.source, args.output_dir, args.kind, args.format, args.background):
            print(path.resolve())
    except (ValueError, OSError) as exc:
        parser.error(str(exc))

if __name__ == "__main__":
    main()
