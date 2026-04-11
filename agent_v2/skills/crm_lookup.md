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

ALIAS RESOLUTION — when the task uses informal/indirect references instead of exact names:
- Read ALL entity files to understand relationships, kinds, aliases, and roles
- Match by relationship field (e.g. "wife", "consulting_client", "co-founder"), kind field (e.g. "system", "person", "pet"), or description
- For comparative references ("older one", "younger one") — compare relevant fields (birthdays, dates) across entities
- For role-based references ("the founder", "ops lead") — search relationship and description fields
- For system/object references ("the printer", "house AI") — search kind and alias fields
- Do NOT clarify if you can resolve the reference by reading entities — exhaust all files first

FINANCE QUERIES — "how much did X charge in total":
- Find ALL purchases from that counterparty (search_text for counterparty name in 50_finance/)
- Read each matching bill, find the requested line item
- SUM the line_eur values across ALL matching bills
- "How much did I pay to X in total?" → sum total_eur from ALL bills with that counterparty

COUNTING RULES (for "how many" questions):
- Use search_text to find all matches across relevant folders
- ALWAYS set limit=2000 to get all results
- Count the results carefully
- Do NOT count mentally from reading — use search_text
- If you searched exhaustively and found ZERO matches → the answer is "0" with OUTCOME_OK
- NEVER clarify just because the count is zero — "0" IS a valid answer
- For "how many X projects involve Y": search ALL project READMEs for Y, count matches. No matches = "0"

FORMAT RULES:
- "Return only the email/date/number" → message = ONLY the raw value, nothing else
- "Return names sorted alphabetically" → one name per line, sorted, nothing else
- "Answer with a number only" → message = ONLY the digit(s)

GROUNDING RULES — CRITICAL (missing ANY ref = FAIL):
grounding_refs MUST include the EXACT path of EVERY file you read to derive the answer.
Ask yourself before completing: "Did I include the path of every file I read?" If not, add them.
</SKILL_CRM_LOOKUP>
