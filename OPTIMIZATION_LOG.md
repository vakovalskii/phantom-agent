# Optimization Log

## Goal: 100% on PAC1-DEV without overfitting

## Progress
| Iter | Run | Score | Passed | Changes |
|---|---|---|---|---|
| 0 | 52b80699 | 69.8% | 30/43 | Baseline: skills + regex |
| 1 | feb0a3ac | 67.4% | 29/43 | GPT-OSS prompt (too abstract) REGRESSION |
| 2 | f1ba1efb | 62.8% | 27/43 | temp=0.4 REGRESSION (empty outputs) |
| 3 | 07e634a9 | 67.4% | 29/43 | temp=1.0 recovery |
| 4 | b1ff9670 | 79.1% | 34/43 | inbox security + clarification rules |
| 5 | a8e95fd2 | 67.4% | 29/43 | email JSON fix (unstable) |
| 6 | 504f03ea | 79.1% | 34/43 | cross-account + inbox rules |

## Stability Analysis (iter4 vs iter6)
- Always pass: 27 tasks
- Always fail: t21, t23, t40 (3 tasks = hard problems)
- Unstable: 13 tasks (random at temp=1.0)

## Always-fail Analysis
- t21: minimal workspace → should CLARIFY but agent says OK
- t23: multiple Dennis Bender contacts → should pick right one but agent CLARIFYs
- t40: missing manager contact in grounding_refs

## Key Learnings
- temp < 1.0 breaks GPT-OSS (empty outputs from Harmony format)
- "Reasoning: high" may hurt (conflicting with vLLM inference)
- Concrete procedures (EMAIL_PROCEDURE) essential — abstract goals lose detail
- Security: subtle injection (social engineering) harder than obvious markers
- Cross-account verification helps catch invoice fraud
- 79% appears to be stability ceiling at temp=1.0
