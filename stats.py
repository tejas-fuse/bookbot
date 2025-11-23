def get_num_words(text: str) -> int:
    """Return the number of words in `text` by splitting on whitespace."""
    return len(text.split())


def get_char_counts(text: str) -> dict:
    """Return a dictionary mapping each lowercase character to its count.

    Counts every character in `text` (including punctuation and spaces).
    Characters are converted to lowercase with `str.lower()` to avoid
    duplicates between upper/lower forms.
    """
    counts: dict = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def sort_char_counts(char_counts: dict) -> list:
    """Convert the char_counts dict into a sorted list of dicts.

    Each element in the returned list is a dict with keys:
      - "char": the character (string)
      - "num": the count (int)

    Only characters for which `char.isalpha()` is True are included.
    The list is sorted in-place from greatest to least by the "num" value
    using a helper function and the `.sort()` method.
    """

    # build list of dictionaries for alphabetical characters only
    items = [{"char": ch, "num": cnt} for ch, cnt in char_counts.items() if ch.isalpha()]

    # helper for sort key
    def _get_num(entry: dict) -> int:
        return entry["num"]

    # sort from greatest to least
    items.sort(key=_get_num, reverse=True)
    return items