import importlib.util
import os
import pytest

name = "Mario"

# Helper to load student_code module
def load_student_code():
    path = os.path.join('problems', 'problem1', 'student_code.py')
    spec = importlib.util.spec_from_file_location('student_code', path)
    student_code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_code)
    return student_code

@pytest.mark.asyncio
async def test_encode_name_caesar():
    student_code = load_student_code()
    result = student_code.encode_name_caesar(name)
    assert result == "Pdulr"

@pytest.mark.asyncio
async def test_encode_name_caesar_with_shift():
    student_code = load_student_code()
    result = await student_code.agent.run("What is your name?")
    # If result is an AgentOutput with a .response attribute:
    assert "Pdulr" in str(getattr(result, "response", result))
