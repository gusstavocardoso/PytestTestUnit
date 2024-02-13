from src.string_operations import reverse_string, capitalize_string, count_vowels

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_capitalize_string():
    assert capitalize_string("hello") == "Hello"
    assert capitalize_string("python") == "Python"

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("python") == 1
