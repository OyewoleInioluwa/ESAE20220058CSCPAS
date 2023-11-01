import re

def replace_pattern(input_string, pattern, replace_with):
    """
    Replaces all occurrences of a pattern in the input string with the replace_with string.
    :param input_string: string in which the pattern needs to be searched.
    :param pattern: string representing the pattern to be searched.
    :param replace_with: string that would replace the pattern found.
    :return: string with all occurrences of the pattern replaced.
    """
    # Create a pattern object
    p = re.compile(pattern)

    # Replace all occurrences of the pattern in the input string
    return p.sub(replace_with, input_string)

# Example usage:
input_string = "The cat is playing with the ball. The ball is blue. The cat is white."
pattern = r"\b(cat|ball)\b"
replace_with = "ANIMAL"

print(replace_pattern(input_string, pattern, replace_with))