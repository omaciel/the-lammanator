import importlib.util
import os
import pytest

double_agent_name: str = "Qleeoh" # This is the encrypted answer for Nibbler, the name of the double agent
arch_nemesis_name: str = "Wkh Edoh Uhdshu" # This is the encrypted answer for The Bale Reaper, the name of our arch-nemesis

# Helper to load student_code module
def load_student_code():
    path = os.path.join('problems', 'problem4', 'student_code.py')
    spec = importlib.util.spec_from_file_location('student_code', path)
    student_code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_code)
    return student_code

@pytest.mark.asyncio
async def test_search_and_encode_double_agent_name():
    student_code = load_student_code()
    result = await student_code.search_and_encrypt_workflow.run(query="What is the name of the double agent?")
    assert double_agent_name in str(getattr(result, "response", result))

@pytest.mark.asyncio
async def test_search_and_encode_arch_nemesis():
    student_code = load_student_code()
    result = await student_code.search_and_encrypt_workflow.run(query="What is the name of our arch-nemesis?")
    assert arch_nemesis_name in str(getattr(result, "response", result))