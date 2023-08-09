import json
import re

# Open the output.json file for reading
with open("data/output.json", "r", encoding="UTF-8") as infile:
    # Load the JSON data from the file
    data = json.load(infile)

    # Extract the completion field from each JSON object in the array
    completions = [d["completion"] for d in data]

    # Compute the maximum, minimum, and average length of the completions
    max_len = max(len(c) for c in completions)
    min_len = min(len(c) for c in completions)
    avg_len = sum(len(c) for c in completions) / len(completions)

    # Print the results
    print(f"Maximum completion length: {max_len}")
    print(f"Minimum completion length: {min_len}")
    print(f"Average completion length: {avg_len}")
# Extract the completion field from each JSON object in the array
completions = [d["completion"] for d in data]

# Split the completion string into words and compute the maximum, minimum, and average number of words
max_words = max(len(re.findall(r"\w+", c)) for c in completions)
min_words = min(len(re.findall(r"\w+", c)) for c in completions)
avg_words = sum(len(re.findall(r"\w+", c)) for c in completions) / len(completions)

# Print the results
print(f"Maximum completion length (in words): {max_words}")
print(f"Minimum completion length (in words): {min_words}")
print(f"Average completion length (in words): {avg_words}")
