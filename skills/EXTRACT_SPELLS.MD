# Skill: Extract Spells and Practices

This skill defines the process for extracting magical rituals, spells, yogic techniques, and esoteric practices from the PDF corpus and synthesizing them into the `lore/spells_and_practices/` directory.

## Workflow

When asked to research or extract a spell (e.g., "Mojo Hand", "Crossroads Ritual", "Love Drawing"):

1. **Run the Extraction Tool:**
   Execute the `extract_spells.py` tool from the terminal with the requested topic. This will query the vector database and retrieve the top 15 chunks, dumping them into a scratch file.
   ```bash
   python tools/extract_spells.py "Mojo Hand creation"
   ```

2. **Read the Raw Output:**
   Locate the resulting markdown file in the `scratch/` directory (e.g., `scratch/raw_spell_extract_Mojo_Hand_creation.md`). Read this file to review all the fragmented context from the corpus.

3. **Synthesize and Format:**
   Using the raw context, synthesize a unified, cohesive markdown file for the practice. Write this new file to the `lore/spells_and_practices/` directory using the standard format defined below. Resolve any conflicting instructions by noting variations, and apply the appropriate thematic persona (ANTIGRAVITY or CERNUNNOS) to the "Lore & Context" section.

## Standard Output Format

All extracted spells must follow this exact markdown structure. You MUST also utilize the `PRESERVE_LINEAGE.MD` skill to populate the "Source Lineage" section with exact passages. See `lore/spells_and_practices/PROTOTYPE_SPELL.md` for a complete example.

```markdown
# [Name of Spell/Practice]

**Purpose:** A concise, 1-2 sentence summary of what the spell does.

## Components
- List of ingredients
- Tools required
- Optimal time/environment (if mentioned)

## The Ritual
1. Step-by-step instructions.
2. Keep it clear and actionable.

## Lore & Context
Include cultural background, notes on variations, and thematic persona commentary here.

## Source Lineage
In accordance with the `PRESERVE_LINEAGE.MD` skill, include exact quoted passages of the source material here to preserve intent and prevent the loss of important details.

> "Exact passage copied verbatim from the source text describing the ritual."
> *(Hoodoo Conjuration Witchcraft & Rootwork Vol [X], Page [Y])*

## Sources
- *Hoodoo Conjuration Witchcraft & Rootwork Vol [X], Page [Y]*
```
