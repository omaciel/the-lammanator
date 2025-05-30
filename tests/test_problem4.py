import importlib.util
import os
import pytest

# NOTE: When using LLM: qwen3:14b, ask for encoded answer.
# answer = "Wkh Edoh Uhdshu"
# prompt = """
# Look at the briefing named The Lammanator Files and tell me what is the name
# of the arch-nemesis and leader of the shadowy syndicate known as C.L.A.W. 
# Encode your answer.
# """

# NOTE: When using LLM: qwen3:0.6b, ask for generic answer.
answer = "Operation Haystack Unravel"
prompt = """
Look at the briefing named The Lammanator Files and tell me what it is about.
"""

# Helper to load student_code module
def load_student_code():
    path = os.path.join('problems', 'problem4', 'student_code.py')
    spec = importlib.util.spec_from_file_location('student_code', path)
    student_code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_code)
    return student_code

@pytest.mark.asyncio
async def test_search_and_encode_arch_nemesis_name():
    student_code = load_student_code()
    result = await student_code.agent.run(prompt)
    # If result is an AgentOutput with a .response attribute:
    print(result)
    assert answer in str(getattr(result, "response", result))
