import importlib.util
import os
import pytest

codewords = ['ansible', 'automation', 'platform']
default_codewords = ['eagle', 'package', 'extraction']

# Helper to load student_code module
def load_student_code():
    path = os.path.join('problems', 'problem2', 'student_code.py')
    spec = importlib.util.spec_from_file_location('student_code', path)
    student_code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_code)
    return student_code

@pytest.mark.asyncio
@pytest.mark.parametrize("text,expected", [
    ("The eagle tripped over the package during extraction and blamed the squirrel.", ['eagle', 'package', 'extraction']),
    ("The ansible tripped over the package during extraction and blamed the squirrel.", ['package', 'extraction']),
    ("The automation tripped over the ansible during extraction and blamed the squirrel.", ['extraction']),
])
async def test_extract_codewords(text, expected):
    student_code = load_student_code()
    result = student_code.extract_codewords(text)
    assert str(expected) in str(result)
    

@pytest.mark.asyncio
async def test_extract_codewords_with_agent():
    student_code = load_student_code()
    result = await student_code.agent.run("The eagle tripped over the package during extraction and blamed the squirrel.")
    for word in default_codewords:
        assert word in str(getattr(result, "response", result))

@pytest.mark.asyncio
@pytest.mark.parametrize("message,expected_codewords", [
    (
        "The ansible and automation platform are ready for deployment.",
        ['ansible', 'automation', 'platform']
    ),
    (
        "Prepare the eagle and the package for extraction at dawn.",
        ['eagle', 'package', 'extraction']
    ),
    (
        "No codewords here.",
        []
    ),
])
async def test_extract_codewords_with_agent_param(message, expected_codewords):
    student_code = load_student_code()
    result = await student_code.agent.run(message)
    response_str = str(getattr(result, "response", result))
    # Optionally, try to parse a list from the response if your agent outputs a list
    # Otherwise, just check for presence of each expected codeword
    for word in expected_codewords:
        assert word in response_str
