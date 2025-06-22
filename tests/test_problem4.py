import importlib.util
import os
import pytest

answer: str = "Qleeoh" # This is the encrypted answer for Nibbler, the name of the double agent

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
    result = await student_code.search_and_encrypt_workflow.run()
    # If result is an AgentOutput with a .response attribute:
    assert answer in str(getattr(result, "response", result))
