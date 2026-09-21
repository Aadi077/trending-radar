# 📈 Trending Radar

A daily archive of the fastest-rising **new** GitHub repositories (created in the last 7 days, ranked by stars), collected automatically by GitHub Actions.

**Last updated:** 2026-09-21 · **Days archived:** 8

## Today's top new repos

| # | Repo | ⭐ | Description |
|---|---|---|---|
| 1 | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 15,279 | Fastest and cheapest web agent |
| 2 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 9,349 |  |
| 3 | [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 5,906 | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and r... |
| 4 | [zai-org/ZCode](https://github.com/zai-org/ZCode) | 5,479 | Z.ai's coding agent harness. Powerful, intelligent, extensible. |
| 5 | [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | 4,297 | The Photoshop alternative for Mac |
| 6 | [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | 3,458 | Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M3 Max. No text ge... |
| 7 | [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) | 3,053 | Semantic ifs from open models, on a 3090 at home. Independent; not affiliated with Jev or TypeSafe. |
| 8 | [mcncarl/jianying-headless](https://github.com/mcncarl/jianying-headless) | 2,349 | Private source preview: native Jianying drafts, isolated editing/export, and standalone Agent Skill. |
| 9 | [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 2,212 | tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own |
| 10 | [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) | 1,800 | One AI trade decision every Monad block. Jev on Kuru MON-USDC. |

More languages: [`data/2026/09/2026-09-21.md`](data/2026/09/2026-09-21.md)

## How it works

- [`scripts/snapshot.py`](scripts/snapshot.py) queries the GitHub search API (stdlib only, no dependencies).
- [`.github/workflows/daily.yml`](.github/workflows/daily.yml) runs it every day and commits the results.
- Raw JSON snapshots live in [`data/`](data) for anyone who wants to analyze trends over time.
