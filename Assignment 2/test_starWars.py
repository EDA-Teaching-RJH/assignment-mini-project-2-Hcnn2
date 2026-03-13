
import pytest
from starWars import (
    validate_force_id, validate_midichlorian_count, flexible_search,
    is_valid_rank_for_side, init_database
)

def test_validate_force_id():
    assert validate_force_id("FORCE-1234-L") == True
    assert validate_force_id("FORCE-9999-D") == True
    assert validate_force_id("force-0001-l") == False   # case sensitive
    assert validate_force_id("BAD-ID") == False
    assert validate_force_id("FORCE-12-L") == False     # wrong digits

def test_validate_midichlorian_count():
    assert validate_midichlorian_count("15000") == True
    assert validate_midichlorian_count("999") == False
    assert validate_midichlorian_count("abc123") == False
    assert validate_midichlorian_count("30000") == True

def test_flexible_search():
    assert flexible_search("ken", "Obi-Wan Kenobi", "Light", "FORCE-0001-L") == True
    assert flexible_search("dark", "Darth Sidious", "Dark", "FORCE-0006-D") == True
    assert flexible_search("xyz", "Yoda", "Light", "FORCE-0003-L") == False

def test_is_valid_rank_for_side():
    assert is_valid_rank_for_side("Jedi Master", "Light") == True
    assert is_valid_rank_for_side("Jedi Master", "Dark") == False
    assert is_valid_rank_for_side("Darth", "Dark") == True

def test_init_database():
    names, sides, ranks, midis, ids = init_database()
    assert len(names) == 10
    assert len(sides) == 10
    assert "Light" in sides and "Dark" in sides
    assert "FORCE-0001-L" in ids


#Run with: pytest