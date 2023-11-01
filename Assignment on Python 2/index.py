import re

def find_and_match_pattern(input_string, pattern):
    # Use the findall method of the re module to find all matches of the pattern in the input_string
    matches = re.findall(pattern, input_string)
    
    # The findall method returns a list of all matches, so we iterate over each match
    for match in matches:
        # If the match is a string (and not a tuple, which would indicate a match with groups),
        # we print it as the result of the pattern match
        if isinstance(match, str):
            print(f"Pattern match found: {match}")
        # If the match is a tuple, we assume that the pattern contained groups,
        # so we print each element of the tuple as the result of a group match
        elif isinstance(match, tuple):
            for i, group_match in enumerate(match):
                print(f"Group match {i+1} found: {group_match}")

# Example usage:
input_string = "I have 2 apples, 3 oranges, and 5 bananas."
pattern = r"\d+ (\w+)"
find_and_match_pattern(input_string, pattern)


    