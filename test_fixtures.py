"""Test fixtures."""

# PLANT S4
FAKE_AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
FAKE_AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

SAMPLE_ENTITIES = ["US01", "DE07", "NL02"]


def test_entity_codes_are_four_chars():
    assert all(len(e) == 4 for e in SAMPLE_ENTITIES)
