import os
import sys


def count_words(words):
    """Count occurrences of each word using a plain dictionary."""
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def preprocess_lines(lines):
    """Preprocess lines by normalizing and cleaning text."""
    return [line.lower().strip() for line in lines]


def read_all_lines(input_folder):
    """Read all lines from all files in the input folder."""
    lines = []
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines


def split_into_words(lines):
    """Split lines into individual words and clean punctuation."""
    words = []