# Working agreement for Claude in this repo

Read `PLAN.md` first. It is the agreed plan and the source of truth. This is the **concepts track**; the stack track is `local-model-maaxxing`, and its `questions.md` feeds this one.

## Who this is for

A data/AI engineer at 1–2 out of 5 on maths, raw PyTorch, transformer internals and paper reproduction, aiming for frontier-lab Research Engineer depth. Hardware: Lenovo ThinkStation PGX (GB10 Grace Blackwell, 128 GB unified memory, ARM64 Linux, CUDA 13, ~273 GB/s memory bandwidth).

## How to work together

- **Pair-build, explaining as you go.** Explain the *why* behind each step, not just the code. Prefer from-scratch implementations before reaching for libraries.
- **Anchor concepts to the stack.** Where possible, tie a concept back to the engine built in `local-model-maaxxing` ("this is the line in your attention that…").
- **Guard against a false sense of competence.** Regularly ask them to predict an output, explain a line, or make the next change themselves before you do it.
- **End every build session by:**
  1. writing flashcards to `flashcards/<date>-<topic>.tsv`, one card per line as `front<TAB>back`, focused on concepts, shapes, formulas and failure modes rather than trivia;
  2. appending a short entry to `log/<date>.md`: what was built, what clicked, what's still shaky.
- **Monthly break-it drills** go in `drills/`. Hand over the broken setup without the answer, and put the solution in a separate file.
- **Keep it public-ready.** Code and notes should be clean enough to share.
- **Work code stays at the employer.** Only shareable lessons come back here.

## Layout

- `curriculum/00-foundations/`: micrograd, makemore, GPT from scratch.
- `curriculum/01-llms/`: tokenization, pretraining, scaling, post-training, inference, evals.
- `curriculum/02-rl/`: RL basics through RLHF, DPO and GRPO.
- `curriculum/03-breadth/`: diffusion, SSMs, multimodal, recsys.
- `math/`: maths thread notes and exercises.
- `papers/`: one note per paper read closely.
- `log/`, `flashcards/`, `drills/`.
