<SKILL_KNOWLEDGE_CLEANUP>
This task asks you to remove cards, threads, or knowledge artifacts.

WORKFLOW:
1. Read /AGENTS.md for workspace rules
2. Identify what to delete:
   - "Remove all captured cards and threads" → find and delete distill artifacts
   - "Discard thread X" → delete specific thread file
   - "Delete files containing X" → search for matching files and delete them

3. Find the relevant folders:
   - Knowledge: 30_knowledge/ (capture/, notes/, threads/) or /02_distill/
   - Cards: 02_distill/cards/ or similar
   - Threads: 02_distill/threads/ or 30_knowledge/threads/

4. For bulk delete:
   a. List the target directory — get ALL filenames
   b. Delete each file INDIVIDUALLY (skip AGENTS.MD files)
   c. After all deletes, list directory again to VERIFY clean

5. For single delete:
   a. Delete the specific file
   b. Verify it's gone

CRITICAL: List ALL files first. Then delete EACH ONE. Then verify.
Do NOT skip any file. AGENTS.md files are kept.
This is a VALID operation — do NOT clarify. Just delete and report.

submit_answer OUTCOME_OK with grounding_refs listing all deleted paths.
</SKILL_KNOWLEDGE_CLEANUP>
