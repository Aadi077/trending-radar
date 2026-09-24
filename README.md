# 📈 Trending Radar

A daily archive of the fastest-rising **new** GitHub repositories (created in the last 7 days, ranked by stars), collected automatically by GitHub Actions.

**Last updated:** 2026-09-24 · **Days archived:** 11

## Today's top new repos

| # | Repo | ⭐ | Description |
|---|---|---|---|
| 1 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 22,664 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any te... |
| 2 | [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 6,698 | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and r... |
| 3 | [zai-org/ZCode](https://github.com/zai-org/ZCode) | 6,692 | Z.ai's coding agent harness. Powerful, intelligent, extensible. |
| 4 | [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 6,678 | Jev-like family of decision models built on top of Qwen3.5/3.8 you can train and run on your own |
| 5 | [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | 6,184 | Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M3 Max. No text ge... |
| 6 | [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 5,965 | 装在手机上的对话副驾：在 QQ / X / 飞书里读懂对方、给出候选回复、一键填入输入框，发不发由你。非侵入，只读屏幕，不 hook 不改包。 |
| 7 | [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | 2,187 | A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline. |
| 8 | [unreallabsai/unreal-agent](https://github.com/unreallabsai/unreal-agent) | 1,863 | Async-first agent harness |
| 9 | [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) | 1,723 | Local typed decisions, contrastive data curation, and model evaluation. |
| 10 | [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | 1,605 | A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's Sys... |

More languages: [`data/2026/09/2026-09-24.md`](data/2026/09/2026-09-24.md)

## How it works

- [`scripts/snapshot.py`](scripts/snapshot.py) queries the GitHub search API (stdlib only, no dependencies).
- [`.github/workflows/daily.yml`](.github/workflows/daily.yml) runs it every day and commits the results.
- Raw JSON snapshots live in [`data/`](data) for anyone who wants to analyze trends over time.
