import os
import pytest

from surf_spot_finder.agents.openai import run_openai_agent

INTEGRATION_MODEL = "gpt-4o-mini"
API_KEY_VAR = "OPENAI_API_KEY"


@pytest.mark.skipif(
    "INTEGRATION_TESTS" not in os.environ,
    reason="Integration tests require INTEGRATION_TESTS env var",
)
def test_openai_real_execution():
    """
    Tests the actual execution of the agent against real APIs.

    WARNING: This will make actual API calls and incur costs.
    Only run when explicitly needed for full system testing.

    Requires:
    - OPENAI_API_KEY in environment variables
    - INTEGRATION_TESTS env var to be set
    """
    from agents import RunResult, ToolCallItem

    result = run_openai_agent(
        INTEGRATION_MODEL,
        "What will be the best surf spot around Vigo, in a 2 hour driving radius, tomorrow?",
        api_key_var=API_KEY_VAR,
    )

    assert isinstance(result, RunResult)
    assert any(isinstance(item, ToolCallItem) for item in result.new_items)
