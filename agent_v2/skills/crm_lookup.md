<SKILL_CRM_LOOKUP>
This task asks you to find information in workspace records.

LOOKUP TYPES:
1. Entity/person info: search entity files (10_entities/cast/ or /contacts/) for name, return requested field
2. Birthday: read entity file, find birthday field
3. Project info: search project folders (40_projects/ or equivalent) for project by name/person
4. Account/relationship info: search entities by relationship, return requested field
5. Last message: search entity files or knowledge files for recorded messages from a person
6. Finance info: search finance folder (50_finance/ or /my-invoices/) for amounts, dates, counterparties

SEARCH STRATEGY:
- First: list_directory_tree of the relevant folder to see all files
- For names: search_text for the name across relevant folders
- For entities: read files in 10_entities/cast/ — each file represents a person, pet, or system
- For projects: explore 40_projects/ — each subfolder has a README.MD with project details
- For finance: explore 50_finance/ — may have invoices/ and purchases/ subfolders
- Name matching is case-insensitive, try BOTH "First Last" and "Last" orderings
- NEVER guess — always verify by reading the actual file

COUNTING RULES (for "how many" questions):
- Use search_text to find all matches across relevant folders
- ALWAYS set limit=2000 to get all results
- Count the results carefully
- Do NOT count mentally from reading — use search_text

FORMAT RULES:
- "Return only the email/date/number" → message = ONLY the raw value, nothing else
- "Return names sorted alphabetically" → one name per line, sorted, nothing else
- "Answer with a number only" → message = ONLY the digit(s)

GROUNDING RULES — CRITICAL (missing ANY ref = FAIL):
grounding_refs MUST include the EXACT path of EVERY file you read to derive the answer.
Ask yourself before completing: "Did I include the path of every file I read?" If not, add them.
</SKILL_CRM_LOOKUP>
