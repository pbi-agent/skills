# Retros

Each task's retro: `tasks/<folder>/07-retro.md`.

This folder holds only cross-task files:

- `index.md`: task table and factory metrics. **Generated** by `python3 factory/bin/factoryctl index --out retros/index.md`. Never edit or append by hand; concurrent tasks would conflict on it.
- Periodic review notes by factory owners (audit results, gate decisions), one file per review, named `<yyyy-mm-dd>-review.md`.
