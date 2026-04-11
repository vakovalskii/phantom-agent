<SKILL_EMAIL_OUTBOUND>
This task asks you to send an email.

WORKFLOW:
1. Orient: list_directory_tree "/" and read /AGENTS.md to learn workspace structure
2. Resolve the recipient:
   - If direct email given → use it directly
   - If name given → search entity files (10_entities/cast/ or /contacts/) for name match, get primary_contact_email
   - If account/project given → search projects or entities for the match, find contact
   - If descriptive → iterate entity/account files, match by relationship, description fields

3. Find the outbox folder (60_outbox/, /outbox/, etc.) — read ALL nested AGENTS.MD files for format rules
4. Read the outbox subfolder AGENTS.MD for the exact email format (field names, required fields)
5. Create email file following the format EXACTLY as documented
6. Verify by reading the created file back
YAML FRONTMATTER RULES:
- Quote ALL string values that contain colons, special chars, or could be misinterpreted
- Subject lines MUST be quoted: subject: "Re: Invoice copy needed"
- File paths in attachments MUST be quoted: - "50_finance/invoices/filename.md"
- Dates should be quoted: sent_at: "2026-03-30T10:47:00Z"

CONTACT RESOLUTION STRATEGY:
- Entity files in 10_entities/cast/ contain: alias, kind, relationship, primary_contact_email, birthday
- Search by name, alias, or relationship
- NEVER clarify if you haven't searched all entity files yet. Exhaust the search first.

If contact truly cannot be resolved after checking ALL files → OUTCOME_NONE_CLARIFICATION

submit_answer with grounding_refs including outbox files, entity files, and any other files read.
</SKILL_EMAIL_OUTBOUND>
