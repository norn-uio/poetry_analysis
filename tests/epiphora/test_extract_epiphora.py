from poetry_analysis.epiphora import extract_epiphora


def test_extract_epiphora_detects_repeated_words():
    # given
    input_texts = ["Så gjør vi så når vi vasker vårt tøy", "vasker vårt tøy", "vasker vårt tøy"]
    # when
    result = extract_epiphora(input_texts)

    assert result[1]["overlap"] == result[2]["overlap"] == "vasker vårt tøy"


def test_extract_epiphora_ignores_identical_punctuation():
    input_texts = ["Hello world!", "This is a different line!", "Another line with the same punctuation!"]

    result = extract_epiphora(input_texts)

    # The result should be an empty dict
    assert result == {}


def test_extract_epiphora_ignores_case():
    input_texts = ["This line ends in a word", "Here is a line with a WORD", "This one ends in a WoRd."]
    # when
    result = extract_epiphora(input_texts)

    assert result[1]["overlap"] == result[2]["overlap"] == "a word"
