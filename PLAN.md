# Plan: research-engineer-curriculum

The **concepts track**: a build-first path from data/AI engineer to frontier-lab **Research Engineer / Member of Technical Staff** depth (Research Scientist kept open), on a Lenovo ThinkStation PGX (GB10, 128 GB unified memory).

Agreed 2026-11-23 through a structured interview, and split out of `local-model-maaxxing` the same day. **It starts once the stack track (`local-model-maaxxing`) is done.** That repo's `questions.md` is the first input here: answer those questions before (or while) following the syllabus below. Change this plan deliberately: edit this file and note why in `log/`.

## Goals

| | |
|---|---|
| Target role | Research Engineer / MTS; Research Scientist kept open |
| Payoff, now | The go-to person for local and private LLMs at work (day job can be used freely) |
| Payoff, later | A frontier lab role, or an own product |
| Starting level | 1–2 out of 5 on maths, raw PyTorch, transformer internals and paper reproduction |
| Time | 10–15 h/week, 12–18 months (after the stack track) |
| Style | Build first, pair-building with Claude, theory as needed plus a scheduled maths thread |
| Visibility | Fully public: GitHub, write-ups, posts |

## Scope: T-shaped

- **Backbone:** optimization, generalization, scaling laws, evals.
- **Deep vertical:** LLMs (pretraining → post-training → inference).
- **Second pillar:** reinforcement learning (post-training, reasoning, agents).
- **Breadth modules:** diffusion and flow matching; state-space models and hybrids; multimodal.
- **Optional side branch:** recommender systems, when work calls for it.

## Specialization (provisional, confirm at month 6)

**Evals** as the entry point, growing into **post-training and RL**, with **interpretability** on the side.

## Weekly routine (~12 h)

| Block | Hours | What |
|---|---|---|
| Maths | 3 | 3Blue1Brown → Strang 18.06 → Stat 110 → matrix calculus (first 4–6 months) |
| Build | 6 | Pair-building with Claude; work projects count here |
| Paper | 2 | One paper a week, read closely |
| Log | 1 | Learning log in `log/` |

A public post every 2–3 weeks.

## Reinforcement, not gates

- **Flashcards:** after each session, Claude writes an Anki deck (`flashcards/`, imported with FSRS scheduling).
- **Break-it drills:** monthly, a subtly broken training run or eval to diagnose without help (`drills/`).
- Checkpoints test whether you can debug and modify things on your own, not verbatim recall.

## Checkpoints (months from the start of this track)

| Month | Checkpoint |
|---|---|
| 3 | GPT trained from scratch (nanoGPT, GPT-2-small reproduction) and every line explained; backprop through attention derived on paper |
| 6 | One paper replicated with a public write-up; specialization confirmed |
| 9 | One small original result; a multi-GPU training exercise (cloud, ~$50–150/month from month 6) |
| 12 | A research-style report (LessWrong or arXiv-quality); fellowship applications sent (MATS, Anthropic Fellows and similar) |

## Projects

- **Small fine-tune** (months 4–6). A small model that takes over one paid API job (extraction or classification), with a business case.
- The work eval harness and research feed are separate repos; see `local-model-maaxxing/PLAN.md`.

## Community

EleutherAI and GPU MODE Discords, LessWrong and the Alignment Forum now; fellowships around months 9–12.

## Start

1. Work through `local-model-maaxxing/questions.md`.
2. micrograd from scratch (`curriculum/00-foundations/micrograd/`, already started on 2026-11-23: derivatives and the `Value` graph are done; backprop is next).
