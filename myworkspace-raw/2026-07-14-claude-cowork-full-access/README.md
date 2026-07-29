# Claude Cowork Full Access

- Creation date: 2026-07-14
- Topic: Change Claude Cowork to full access
- Purpose: Record the steps and outcome of configuring Claude Cowork permissions.
- Finding: Claude Cowork has no single full-disk access switch. The current admin setting leaves allowed workspace folders unset, which means unrestricted folder selection; each task still needs an explicitly attached folder.
- Outcome: Claude rejected `/Users/yangqi` as a trusted folder because Home, root, protected locations, and invalid paths cannot be added. The more specific folder `/Users/yangqi/Documents/Claude` was added successfully as a trusted Cowork folder.
