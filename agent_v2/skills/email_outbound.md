<SKILL_EMAIL_OUTBOUND>
This task asks you to send an email.

WORKFLOW:
1. Orient: list_directory_tree "/" and read /AGENTS.md to learn workspace structure
2. Resolve the recipient:
   - If direct email given → use it directly
   - If name given → search entity files (10_entities/cast/ or /contacts/) for name match, get primary_contact_email
   - If account/project given → search projects or entities for the match, find contact
   - If descriptive → iterate entity/account files, match by relationship, description fields

3. Find the outbox folder (60_outbox/, /outbox/, etc.) — read ALL nested AGENTS.MD files
4. Read 99_system/workflows/sending-email.md for the EXACT email format and frontmatter schema
5. Create email file following the documented format EXACTLY
6. Verify by reading the created file back
YAML FRONTMATTER — MUST be valid YAML:
- Quote ALL string values that contain colons: subject: "Re: Invoice copy"
- Quote file paths in attachments: - "50_finance/invoices/filename.md"
- Quote timestamps: created_at: "2026-03-30T10:47:00Z"
- Use the exact field names from the schema (record_type, created_at, send_state, to, subject, attachments, related_entities, related_projects)
- Filename format: eml_YYYY-MM-DDTHH-MM-SSZ.md (colons replaced with dashes in filename only)

CONTACT RESOLUTION STRATEGY:
- Entity files in 10_entities/cast/ contain: alias, kind, relationship, primary_contact_email, birthday
- Search by name, alias, or relationship
- NEVER clarify if you haven't searched all entity files yet. Exhaust the search first.

If contact truly cannot be resolved after checking ALL files → OUTCOME_NONE_CLARIFICATION

submit_answer with grounding_refs including outbox files, entity files, and any other files read.
</SKILL_EMAIL_OUTBOUND>
