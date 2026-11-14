# Food picture v1 (make.fun food-picture-01).
#
# The simplest entry the rules allow: a repository holding the image and
# a program that copies it to /output/entry.png. The picture itself is
# an original photorealistic tonkotsu ramen shot (tall noodle pull,
# steam, chashu, runny egg, chili oil, dark moody background) made for
# this competition. The program does no drawing, no network and no
# randomness: it copies the same bytes every run.

import os
import shutil
import sys


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
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if dst_size != src_size:
        raise SystemExit("entry.png copy size mismatch")
    with open(dst, "rb") as f:
        magic = f.read(3)
    if magic != b"\xff\xd8\xff":
        raise SystemExit("entry.png is not a JPEG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
