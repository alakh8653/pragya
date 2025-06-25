"""Natural language processing utilities."""

import re
from collections import Counter
from typing import List


def word_frequencies(text: str) -> Counter:
    """Return word frequency counts from a string."""
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words)


def top_keywords(texts: List[str], n: int = 5) -> List[str]:
    counts = Counter()
    for t in texts:
        counts.update(word_frequencies(t))
    return [w for w, _ in counts.most_common(n)]
