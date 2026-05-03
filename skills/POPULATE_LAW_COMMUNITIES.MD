# Skill: Populate Law Communities and Teachers

This skill defines the process for populating the `lore/communities_and_teachers/` directory with a specific focus on the parts of the corpus that discuss the law, court systems, policing, and the individuals operating within or against these structures.

## Objective
To record information about historical lineages, informants, and key figures (both mundane and magical) who navigated, challenged, or operated within the legal and penal systems documented in the corpus. This ensures that the human elements and communities driving these practices are preserved.

## Workflow

When asked to populate or expand on a teacher/community related to law and order:

1. **Identify Key Figures and Communities:**
   While performing law and order extractions (via `EXTRACT_LAW_AND_ORDER.MD`) or when directly queried, identify specific rootworkers, informants, communities, or notable figures (e.g., a specific judge or sheriff mentioned frequently) related to legal matters.

2. **Run Targeted Extractions:**
   Use the extraction tool to gather specific information about these figures or communities from the corpus.
   ```bash
   python tools/extract_spells.py "Informant name court system"
   ```

3. **Synthesize into Community Profiles:**
   Create or update a markdown file in the `lore/communities_and_teachers/` directory for the identified figure or group. 

## Standard Output Format

All entries must follow this exact markdown structure. You MUST also utilize the `PRESERVE_LINEAGE.MD` skill to populate the "Source Lineage" section.

```markdown
# [Name of Teacher, Community, or Figure]

**Role:** A concise summary of who they were and their relationship to the law/community.

## Background
- Location/Region
- Known associations
- Specialty or reputation (e.g., "Known for getting people out of jail")

## Legal and Magical Encounters
Detail their specific interactions with the court system, police, or jails, and the magical practices they employed in these situations. How did they interact with the law?

## Lore & Context
Thematic persona commentary on their legacy, resilience, and impact on the tradition's legal defense methods.

## Source Lineage
In accordance with the `PRESERVE_LINEAGE.MD` skill, include exact quoted passages.

> "Exact passage copied verbatim."
> *(Hoodoo Conjuration Witchcraft & Rootwork Vol [X], Page [Y])*
```
