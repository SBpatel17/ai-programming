"""
test_agent.py - Deterministic tests for the campus resource tool (Lab 4)

These tests call get_campus_resource_info directly. No LLM, API key,
or network is involved, so the same input always gives the same result.

The spec's examples use "library" and "tutoring", but our verified JCC
data (campus_resources.json) has no Library or Tutoring Center entry.
Each test below checks the same behavior using a resource we do have.

Run with:  python -m pytest test_agent.py -v
     or:   python test_agent.py

Author: Sameer Patel
Course: AI Programming
"""

from agent import get_campus_resource_info


def test_name_lookup():
    # Spec TEST 1: look up a resource by its official name
    result = get_campus_resource_info("health center")
    assert result["status"] == "success"
    assert result["name"] == "Health Center"


def test_alias_lookup():
    # Spec TEST 2: "advising" is an alias, not the official name
    result = get_campus_resource_info("advising")
    assert result["status"] == "success"
    assert result["name"] == "Academic Advising"


def test_case_insensitive():
    # Spec TEST 3: uppercase input should still match
    result = get_campus_resource_info("HEALTH CENTER")
    assert result["status"] == "success"
    assert result["name"] == "Health Center"


def test_resource_not_found():
    # Spec TEST 4
    result = get_campus_resource_info("dental office")
    assert result["status"] == "error"
    assert "error_message" in result
    assert "Available resources" in result["error_message"]


def test_list_all_resources():
    # Spec TEST 5
    result = get_campus_resource_info("all")
    assert result["status"] == "success"
    assert "available_resources" in result
    assert isinstance(result["available_resources"], list)
    assert len(result["available_resources"]) >= 4


if __name__ == "__main__":
    # Plain-Python runner so the file also works without pytest
    tests = [
        test_name_lookup,
        test_alias_lookup,
        test_case_insensitive,
        test_resource_not_found,
        test_list_all_resources,
    ]
    failed = 0
    for test in tests:
        try:
            test()
            print(f"PASS  {test.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {test.__name__}  {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} tests passed")
    raise SystemExit(1 if failed else 0)
