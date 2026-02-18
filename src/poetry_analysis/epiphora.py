"""Epiphora, or epistrophe, is the repetition of the same word or phrase at the end
of successive clauses in a line, or of successive lines in a stanza.
"""

from poetry_analysis.utils import normalize, strip_redundant_whitespace


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
    previous_text = None
    for idx, text in enumerate(text_sequence):
        current = normalize(text, split_tokens=False)
        if idx == 0:
            previous_text = current
            continue

        previous = previous_text
        overlap = strip_redundant_whitespace(shared_ending_substring(previous, current))
        if overlap:
            epiphora[idx] = {"previous_text": previous, "current_text": current, "overlap": overlap}
        previous_text = current
    print(epiphora)
    return epiphora
