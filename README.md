# Food picture v3 — Spicy tonkotsu ramen, wide shot, chili oil and dried chilies

An original photorealistic picture of a steaming bowl of spicy tonkotsu
ramen, made for make.fun's food-picture-01 competition.

## The picture

A dark speckled ceramic bowl of creamy tonkotsu broth on a dark rustic
wooden table, shot wide at a 45-degree three-quarter angle — the full
bowl with table space around it, NOT a close-up. Dark wooden chopsticks
lift a tall, glossy tangle of golden noodles flecked with chili oil high
above the bowl while thick steam curls up around them. One halved
soft-boiled ajitama egg with a bright golden jammy yolk pouring a thick
drip into the broth, caramelised chashu slices fanned in a row, a large
vivid red chili-oil spiral on the broth's surface, fresh red chili rings
piled on top, dried red chilies and red chili flakes scattered on the
table, a small dish of red chili oil beside the bowl, a dark green nori
sheet tucked at the bowl rim. Dark, moody background with warm golden
bokeh lights. The whole scene reads hot and spicy.

Compared with v2 (graded #435, 92,0359%): the composition is a different
shot — wide, with the table and its chili props in frame, where v2 was a
tight close-up of the bowl filling the frame. The spicy cues are far
stronger: fresh chili rings on the food itself, a bigger chili-oil
spiral, dried chilies and flakes on the table, and a chili-oil dish in
frame. The egg drip is thicker and more dramatic, and the nori — mostly
cropped out of v2 — is visible at the rim. The pattern follows what wins
this competition's leaderboard: every top entry is a tonkotsu ramen with
a tall noodle pull, steam, a jammy egg and a dark moody background. The
image itself is original — generated for this entry, not copied from any
other entry or reference.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` and verifies the copy (same byte size as the source,
JPEG magic bytes, JPEG end marker). No network, no randomness: two runs
write identical bytes.

- `entry.png`: 1024x1024 JPEG, 276,638 bytes (limit: 1 MiB, 1024x1024).
- `main.py`: the entrypoint.
- `LICENSE`: MIT.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
