<SKILL_EMAIL_OUTBOUND>
This task asks you to send an email.

WORKFLOW:
1. Orient: list_directory_tree "/" and read /AGENTS.md to learn workspace structure
2. Resolve the recipient:
   - If direct email given → use it directly
   - If name given → search entity files (10_entities/cast/ or /contacts/) for name match, get primary_contact_email
   - If account/project given → search projects or entities for the match, find contact
   - If descriptive → iterate entity/account files, match by relationship, description fields

3. Find the outbox folder (60_outbox/, /outbox/, etc.) — read its AGENTS.MD or README.MD for format
4. Read seq.json to get the current sequence number
5. Create email file in outbox following the format rules
6. Update seq.json
7. Verify by reading the created file back

CONTACT RESOLUTION STRATEGY:
- Entity files in 10_entities/cast/ contain: alias, kind, relationship, primary_contact_email, birthday
- Search by name, alias, or relationship
- NEVER clarify if you haven't searched all entity files yet. Exhaust the search first.

If contact truly cannot be resolved after checking ALL files → OUTCOME_NONE_CLARIFICATION

submit_answer with grounding_refs including outbox files, entity files, and any other files read.
</SKILL_EMAIL_OUTBOUND>
