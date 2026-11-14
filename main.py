# Food picture v3 (make.fun food-picture-01).
#
# The simplest entry the rules allow: a repository holding the image and
# a program that copies it to /output/entry.png. The picture itself is
# an original photorealistic spicy tonkotsu ramen shot made for this
# competition: a wide 45-degree three-quarter view (NOT a close-up), the
# full bowl on a dark wooden table, chopsticks lifting a tall glossy
# noodle pull, one ajitama egg with a bright golden yolk dripping into
# the broth, caramelised chashu fan, a vivid red chili-oil spiral, fresh
# red chili rings, dried chilies and chili flakes on the table, a small
# dish of chili oil, nori at the bowl rim, thick steam, warm bokeh, dark
# moody background. The program does no drawing, no network and no
# randomness: it copies the same bytes every run.

import os
import shutil
import sys


def verify_jpeg(path, expected_size):
    """Verify the file at path is a complete JPEG of the expected size.

    Checks the byte size, the JPEG magic bytes (SOI marker) and the
    trailing EOI marker, so a truncated or non-JPEG copy fails loudly
    instead of being shipped.
    """
    if os.path.getsize(path) != expected_size:
        raise SystemExit("entry.png copy size mismatch")
    with open(path, "rb") as f:
        magic = f.read(3)
    if magic != b"\xff\xd8\xff":
        raise SystemExit("entry.png is not a JPEG")
    with open(path, "rb") as f:
        f.seek(-2, os.SEEK_END)
        tail = f.read(2)
    if tail != b"\xff\xd9":
        raise SystemExit("entry.png is truncated (no JPEG end marker)")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy: same size as the source and a JPEG by magic bytes
    # (the file is named entry.png, but the format is told by its first
    # bytes, as the rules say). Fail loudly rather than ship a bad file.
    verify_jpeg(dst, os.path.getsize(src))
    return 0


if __name__ == "__main__":
    sys.exit(main())
