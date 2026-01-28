"""Epiphora or epistrophe is the repetition of the same word or phrase at the end
of successive clauses in a line, or of successive lines in a stanza.
"""

# TODO: Implement a function taking a list as input, and comparing the last element in each item of the list


def shared_ending_substring(string1: str, string2: str) -> str:
    """Find the shared substring at the end of two strings."""
    min_length = min(len(string1), len(string2))

    for i in range(1, min_length + 1):
        if string1[-i] != string2[-i]:
            final_substring = string1[-i + 1 :] if i > 1 else ""
            return final_substring
    return string1[-min_length:] if min_length > 0 else ""


def extract_epiphora(text_sequence: list[str]) -> dict:
    """Iterate over a list of strings in `text_sequence` and extract overlapping segments in successive strings."""
    epiphora = {}
    previous_texts = []
    for idx, current in enumerate(text_sequence):
        if idx == 0:
            previous_texts.append(current)
            continue

        previous = previous_texts[idx - 1]
        overlap = shared_ending_substring(previous, current)
        if overlap:
            epiphora[idx] = {"previous_text": previous, "current_text": current, "overlap": overlap}
        previous_texts.append(current)
    print(epiphora)
    return epiphora


def test_extract_epiphora_detects_repeated_words():
    # given
    input_texts = ["Så gjør vi så når vi vasker vårt tøy", "vasker vårt tøy", "vasker vårt tøy"]
    # when
    result = extract_epiphora(input_texts)

    assert result[1]["overlap"] == result[2]["overlap"] == "vasker vårt tøy"


test_extract_epiphora_detects_repeated_words()
