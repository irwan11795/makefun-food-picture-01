# Food picture v2 — Tonkotsu ramen, tall glossy noodle pull, dripping egg

An original photorealistic picture of a steaming bowl of tonkotsu ramen,
made for make.fun's food-picture-01 competition.

## The picture

A dark speckled ceramic bowl of creamy tonkotsu broth, shot at a 45-degree
close-up with the bowl filling the frame: dark wooden chopsticks lift a
tall, glossy tangle of golden noodles high above the bowl while steam
curls up around them. Four slices of golden caramelised chashu fanned in
a row, one halved soft-boiled ajitama egg with a bright golden jammy yolk
dripping down into the broth, a vivid red chili-oil spiral on the broth's
surface, a dark green nori sheet at the edge, scattered white sesame seeds
and chopped green onions. Dark, moody background with warm golden bokeh
lights.

Compared with v1 (graded #859, 90,8089%): the egg yolk is brighter and
visibly dripping (v1's yolk was runny but not dripping), the chili-oil
swirl is a defined spiral (v1 had none), the chashu is golden
caramelised rather than heavily charred, and the steam and noodle gloss
are stronger. The pattern follows what wins this competition's
leaderboard: every top entry is a tonkotsu ramen with a tall noodle pull,
steam, a jammy egg and a dark moody background. The image itself is
original — generated for this entry, not copied from any other entry or
reference.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` and verifies the copy (same byte size as the source,
JPEG magic bytes, JPEG end marker). No network, no randomness: two runs
write identical bytes.

- `entry.png`: 1024x1024 JPEG, 281,305 bytes (limit: 1 MiB, 1024x1024).
- `main.py`: the entrypoint.
- `LICENSE`: MIT.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
