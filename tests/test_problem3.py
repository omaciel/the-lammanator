import importlib.util
import os
import pytest

codewords = ['ansible', 'automation', 'platform']
default_codewords = ['eagle', 'package', 'extraction']

# Helper to load student_code module
def load_student_code():
    path = os.path.join('problems', 'problem3', 'student_code.py')
    spec = importlib.util.spec_from_file_location('student_code', path)
    student_code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_code)
    return student_code

@pytest.mark.asyncio
async def test_log_message_to_file():
    student_code = load_student_code()
    result = await student_code.agent.run("The target will arrive at checkpoint Bravo by 0900 hours.")
    assert "drop.txt" in str(getattr(result, "response", result))
        