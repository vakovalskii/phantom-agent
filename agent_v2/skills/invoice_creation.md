<SKILL_INVOICE_CREATION>
This task asks you to create an invoice or work with finance documents.

WORKFLOW:
1. Read /AGENTS.md for workspace structure
2. Find the finance folder (50_finance/, /my-invoices/, etc.)
3. Read any README.MD or schema docs (99_system/schemas/) for format rules
4. Parse from task: invoice ID, line items, amounts
5. Compute total from line items
6. Create the file following the schema
7. Verify by reading the file back
8. submit_answer with grounding_refs including schema docs and created file
</SKILL_INVOICE_CREATION>
