# Skill: Extract Law and Order

This skill defines the process for extracting discussions, accounts, spells, and practices related to the court system, policing systems, and jails from the PDF corpus. These extractions are crucial for understanding the sociopolitical realities and defensive magics recorded in the text.

## Workflow

When asked to research or extract law and order topics (e.g., "Court cases", "Police encounters", "Jail time"):

1. **Run the Extraction Tool:**
   Execute the `extract_spells.py` tool from the terminal with the requested topic. This will query the vector database and retrieve the top chunks, dumping them into a scratch file.
   ```bash
   python tools/extract_spells.py "Court case judge"
   ```
   *(Note: The `extract_spells.py` tool queries the corpus for any topic based on semantic similarity, making it suitable for these extractions.)*

2. **Read the Raw Output:**
   Locate the resulting markdown file in the `scratch/` directory (e.g., `scratch/raw_spell_extract_Court_case_judge.md`). Read this file to review all the fragmented context from the corpus.

3. **Synthesize and Format:**
   Using the raw context, synthesize a unified, cohesive markdown file for the topic. Write this new file to the `lore/law_and_order/` directory (creating the directory if it doesn't exist) using the standard format defined below. Apply the appropriate thematic persona to the "Lore & Context" section.

## Standard Output Format

All extracted law and order topics must follow this exact markdown structure. You MUST also utilize the `PRESERVE_LINEAGE.MD` skill to populate the "Source Lineage" section with exact passages.

```markdown
# [Topic Name]

**Summary:** A concise, 1-2 sentence summary of the law and order dynamic or situation described.

## Elements of the Account
- Key figures involved (e.g., Judge, Sheriff, Informant)
- Methods used (legal or magical)
- Outcomes

## The Narrative / Practice
1. Detail the specific events, spells, or interactions as described.
2. Keep it clear and focused on the historical/magical reality.

## Lore & Context
Include historical background, power dynamics, and thematic persona commentary here. Focus on the intersection of mundane law and spiritual authority.

## Source Lineage
In accordance with the `PRESERVE_LINEAGE.MD` skill, include exact quoted passages of the source material here to preserve intent and prevent the loss of important details.

> "Exact passage copied verbatim from the source text describing the court case or jail."
> *(Hoodoo Conjuration Witchcraft & Rootwork Vol [X], Page [Y])*
```
