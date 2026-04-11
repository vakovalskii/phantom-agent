<SKILL_FOLLOWUP_RESCHEDULE>
This task asks you to reschedule a follow-up date or update reminders.

WORKFLOW:
1. Read /AGENTS.md for workspace structure
2. Identify the entity/account (by name or description)
3. Search entity files (10_entities/cast/ or /accounts/) to find the match
4. Find reminders folder (20_work/reminders/ or /reminders/)
5. Read the entity file — find follow-up date field
6. Compute the new date:
   - "in two weeks" → get current date from get_context, add 14 days
   - "move to 2026-12-15" → use that exact date
7. Update the entity file with new follow-up date (keep all other fields!)
8. Find and update matching reminder if it exists
9. Verify BOTH files by reading them back
10. submit_answer with grounding_refs including BOTH file paths

CRITICAL: You must update BOTH the entity AND the reminder if both exist. Missing one = fail.

ERROR HANDLING:
- If entity not found → OUTCOME_NONE_CLARIFICATION
- Read the FULL file before writing — preserve all existing fields, only change the date field
</SKILL_FOLLOWUP_RESCHEDULE>
