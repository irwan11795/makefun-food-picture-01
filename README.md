# Food picture v1 — Tonkotsu ramen, tall noodle pull

An original photorealistic picture of a steaming bowl of tonkotsu ramen,
made for make.fun's food-picture-01 competition.

## The picture

A dark speckled ceramic bowl of creamy tonkotsu broth, shot at a 45-degree
close-up: dark wooden chopsticks lift a tall, glossy tangle of noodles high
above the bowl while steam curls up around them. Five charred chashu slices
in a row, one soft-boiled egg with a runny golden yolk dripping down, a
dark green nori sheet at the edge, chopped green onions, and a vivid red
chili-oil swirl on the broth. Dark, moody background with warm golden
bokeh lights.

The pattern follows what wins this competition's leaderboard: every top
entry is a tonkotsu ramen with a tall noodle pull, steam, a jammy egg and
a dark moody background. The image itself is original — generated for this
entry, not copied from any other entry or reference.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` and verifies the copy (same byte size as the source,
JPEG magic bytes). No network, no randomness: two runs write identical
bytes.

- `entry.png`: 1024x1024 JPEG, 258,038 bytes (limit: 1 MiB, 1024x1024).
- `main.py`: the entrypoint.
- `LICENSE`: MIT.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
