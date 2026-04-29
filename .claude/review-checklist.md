# Review Checklist — reasons-qagent

Project-specific review criteria. Used by the /review skill.

## Security
- [ ] No hardcoded credentials, API keys, or tokens
- [ ] No unsafe eval(), exec(), or os.system() with user input
- [ ] Temp files cleaned up after runs
- [ ] No sensitive data in error messages or logs

## Project Rules (from CLAUDE.md)
- [ ] tests/agent_test.py is the agent core, NOT a test file
- [ ] CLI conventions match existing patterns
- [ ] Minimum viable diff — no drive-by refactors

## Quality
- [ ] No debug print() statements left in
- [ ] No commented-out code blocks
- [ ] Error handling covers failure paths
- [ ] Step JSON output is valid and parseable
