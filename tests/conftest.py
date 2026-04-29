import os

# Allow agent_test.py to be imported without a real API key — unit tests never call the API.
if "ANTHROPIC_API_KEY" not in os.environ:
    os.environ["ANTHROPIC_API_KEY"] = "sk-ant-unit-test-placeholder"
