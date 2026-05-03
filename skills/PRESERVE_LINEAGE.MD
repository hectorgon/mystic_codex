# Skill: Preserve Lineage

This skill defines the process for preserving the lineage and exact source material of extracted rituals, spells, entities, and practices. By preserving the raw text passages, we empower ourselves and the reader to infer original intent and ensure that no crucial details from the corpus are left out or distorted by modern synthesis.

## The Principle of the "Mirroring Bridge"

Drawing inspiration from techniques like the Dream Interview Method (DIM), the core of preserving lineage is **mirroring the exact words** of the corpus before applying any interpretation or summarization. 

When compiling entries (such as spells or beings) from the corpus, you must build a "Bridge" back to the source text by extracting and presenting the exact passages that informed your synthesis. 

### Why is this important?
- **Prevents Dilution:** Summarizing can accidentally remove specific, strange, or highly contextual details that are essential to the practice.
- **Maintains Authenticity:** It honors the original voices, informants, and historical context.
- **Allows Independent Analysis:** It provides the raw "dream images" (the actual text) so that others can draw their own conclusions about meaning and intent.

## Workflow: Building the Source Bridge

When utilizing an extraction skill (like `EXTRACT_SPELLS.MD` or a future `EXTRACT_BEINGS.MD`), incorporate this lineage preservation process:

### 1. Extract Exact Passages (The "Mirror")
When reviewing the raw chunks retrieved from the corpus, identify the most critical paragraphs or sentences that define the core of the practice, entity, or ritual. Do not summarize or paraphrase them—copy them exactly as they appear in the source text. 

### 2. Contextualize the Snippets
Ensure each extracted snippet is clearly associated with its specific source (e.g., Volume, Page Number, Informant). This provides the necessary context for the raw material.

### 3. Integrate into the Final Document
In the standardized output format of the extraction, include a dedicated **"Source Lineage"** section. This section should contain the direct quotes, allowing the reader to compare the synthesized instructions with the raw historical text.

## Standard Lineage Format

When generating the final markdown document, use blockquotes to present the extracted passages. Always append the source citation directly below the quote.

Here is a concrete example derived from `scratch/raw_spell_extract_Fiery_Wall_of_Protection.md`:

```markdown
## Source Lineage

> "Well, the protection from that [spell] in hoodoo is to take and burn a black candle in [your] back shed, back out in the open where the air can hit it and [it can] go into the dark corners, and that [going into dark corners] drives the evil away from you anywhere."
> *(Hoodoo Conjuration Witchcraft & Rootwork Vol 1, Page 918)*

> "Take sulphur and a little lard and spread 'cross your door - doorstep every .arning [morning], and it'll harm you... if somebody did that to my door or - something to harm me..."
> *(Hoodoo Conjuration Witchcraft & Rootwork Vol 5, Page 699)*
```

## Integrating with Other Skills
- **Extract Spells:** Use this skill to pull the exact instructions or ingredients described by the rootworker to ensure no steps or nuanced conditions are missed.
- **Extract Beings:** Use this skill to pull the exact descriptions, adjectives, and feelings associated with the entity in the text, avoiding "prefabricated interpretations".
