#!/usr/bin/env python3
"""
Script to analyze the number of words and paragraphs in the corebook documents
and calculate the estimated number of pages for an A5 book with two columns.
"""

import os
import re
import glob

# Configuration
COREBOOK_DIR = "corebook"
WORDS_PER_PAGE = 700  # Estimated words per A5 page with two columns (38-39 lines each, ~10 words/line)

def count_words_and_paragraphs(text):
    """Count words and paragraphs in the given text."""
    # Split into paragraphs (blocks separated by blank lines)
    paragraphs = re.split(r'\n\s*\n', text.strip())
    # Filter out empty paragraphs
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    num_paragraphs = len(paragraphs)
    
    # Count words
    words = re.findall(r'\b\w+\b', text)
    num_words = len(words)
    
    return num_words, num_paragraphs

def main():
    # Find all numbered corebook files (e.g., 01-*.md, 02-*.md, etc.)
    pattern = os.path.join(COREBOOK_DIR, "[0-9][0-9]-*.md")
    files = glob.glob(pattern)
    
    # Also include any future numbered files like 00-*.md if they exist
    pattern_future = os.path.join(COREBOOK_DIR, "[0-9]-*.md")
    files.extend(glob.glob(pattern_future))
    
    # Remove duplicates
    files = list(set(files))
    files.sort()
    
    total_words = 0
    total_paragraphs = 0
    
    print("Analyzing corebook documents:")
    print("=" * 50)
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        words, paragraphs = count_words_and_paragraphs(content)
        total_words += words
        total_paragraphs += paragraphs
        
        file_name = os.path.basename(file_path)
        print(f"{file_name}: {words} words, {paragraphs} paragraphs")
    
    print("=" * 50)
    print(f"Total words: {total_words}")
    print(f"Total paragraphs: {total_paragraphs}")
    
    # Calculate estimated pages
    estimated_pages = total_words / WORDS_PER_PAGE
    print(f"Estimated pages: {estimated_pages:.1f}")
    
    # Assuming generous margins and sizable font as described
    print("\nAssumptions:")
    print("- A5 page size")
    print("- Two columns per page")
    print("- Each column has 38-39 lines of text")
    print("- Estimated 10 words per line on average")
    print("- Generous margins accounted for in word density")

if __name__ == "__main__":
    main()