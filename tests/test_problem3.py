import importlib.util
import os
import pytest

from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")
file_name: str = "drop.txt"
message: str = f"The target will arrive at checkpoint Bravo exactly at {current_time} hours."

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
    result = await student_code.agent.run(f"Save the following message: {message}")
    assert file_name in str(getattr(result, "response", result))

    # Check that the message appears in the last line of drop.txt
    with open(file_name, 'r') as f:
        lines = f.readlines()
        last_line = lines[-1].strip()
    assert message in last_line
