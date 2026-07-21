"""Sample code. It exists so scc has real source to measure."""

import re
from collections import Counter

WORD = re.compile(r"[a-z']+")

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "if",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "to",
    "was",
    "were",
    "with",
}


def words(text):
    return WORD.findall(text.lower())


def word_count(text):
    return len(words(text))


def unique_words(text):
    return set(words(text))


def frequencies(text, skip_stop_words=True):
    counts = Counter(words(text))
    if skip_stop_words:
        for stop in STOP_WORDS:
            counts.pop(stop, None)
    return counts


def most_common(text, limit=10):
    return frequencies(text).most_common(limit)


def average_word_length(text):
    found = words(text)
    if not found:
        return 0.0
    return sum(len(word) for word in found) / len(found)


def sentences(text):
    parts = re.split(r"[.!?]+", text)
    return [part.strip() for part in parts if part.strip()]


def average_sentence_length(text):
    found = sentences(text)
    if not found:
        return 0.0
    return sum(word_count(part) for part in found) / len(found)


def lexical_diversity(text):
    total = word_count(text)
    if total == 0:
        return 0.0
    return len(unique_words(text)) / total


def summarize(text):
    return {
        "words": word_count(text),
        "unique": len(unique_words(text)),
        "sentences": len(sentences(text)),
        "average_word_length": round(average_word_length(text), 2),
        "average_sentence_length": round(average_sentence_length(text), 2),
        "lexical_diversity": round(lexical_diversity(text), 3),
        "top_words": most_common(text, 5),
    }
