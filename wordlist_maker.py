import itertools

# Configuration
keywords = ["Enter", "Keywords", "Here"]
specials = ["", "!", "@", "#", "$"]  # Includes empty string for no special char
number_range = range(0, 100)  # 0-99
min_number_length = 1  # Skip pure 0 (e.g., "0" but keep "01")

def format_number(n):
    """Convert numbers to string with leading zeros when needed"""
    return str(n) if n >= 10 else f"0{n}"

with open("super_wordlist.txt", "w") as f:
    # Two-word combinations with numbers
    for word1, word2 in itertools.permutations(keywords, 2):
        for special in specials:
            for num in number_range:
                num_str = format_number(num)
                
                # Pattern: word1+special+word2+number
                f.write(f"{word1}{special}{word2}{num_str}\n")
                
                # Pattern: word1+special+number+word2
                f.write(f"{word1}{special}{num_str}{word2}\n")
                
                # Pattern: number+word1+special+word2
                f.write(f"{num_str}{word1}{special}{word2}\n")

    print(f"Generated super_wordlist.txt with 2-word+number combinations!")