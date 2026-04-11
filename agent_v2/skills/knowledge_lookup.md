<SKILL_KNOWLEDGE_LOOKUP>
This task asks about captured articles or knowledge repo content.

WORKFLOW:
1. Call get_context to determine current sandbox date
2. Read /AGENTS.md for workspace structure
3. Find the knowledge/capture folder (30_knowledge/capture/, /01_capture/influential/, etc.)
4. List the folder to see all files
5. Files may be named with dates: YYYY-MM-DD__slug.md
6. Compute the target date from the task:
   - "12 days ago" → current_date - 12 days
   - "the day after tomorrow" → current_date + 2 days
7. Look for a filename matching the computed date
8. If found → submit_answer OUTCOME_OK with the filename
   - grounding_refs MUST include the FULL path
9. If NOT found → submit_answer OUTCOME_NONE_CLARIFICATION (NOT OUTCOME_OK!)
   - CRITICAL: "no article found" = CLARIFICATION, never OK
   - Explain that no file matches the date
   - List what dates ARE available

DATE COMPUTATION:
- Be precise. Double-check your arithmetic.

CRITICAL: grounding_refs must contain the EXACT full file path, not descriptions.
</SKILL_KNOWLEDGE_LOOKUP>
