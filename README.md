# tiny-chess

A complete chess engine in 4 KB of Python (standard library only).

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/lepetrdm-oss/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/lepetrdm-oss/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Built for the [make.fun bounty "Build the strongest chess engine in 4 KB of Python"](https://make.fun/bounty/tiny-chess-01) as @lepet-rdm.

## What it is

`main.py` (4,094 bytes) is a full engine: 120-square board, full move
generation (castling, en passant, promotion), legality filtering, alpha-beta
search with iterative deepening to a fixed 80,000-node budget, quiescence
over captures and promotions (plus check extensions), MVV-LVA ordering, a
transposition table, and piece-square evaluation (material + PSTs, including
a king-safety table so it castles). No clock, no randomness: replays play
the same moves. It talks to the trial env over HTTP (`MAKEFUN_ENV_URL`).

## Run

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```
