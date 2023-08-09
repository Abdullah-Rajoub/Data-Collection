import json

# Open the input file for reading
with open(
    "C:/Users/kinga/Desktop/scripts/psu_gpt.json", "r", encoding="UTF-8"
) as infile:
    # Load the JSON data from the file
    data = json.load(infile)

    # Extract the prompt and completion fields from each JSON object in the array
    filtered_data = [
        {"prompt": d["prompt"], "completion": d["completion"]} for d in data
    ]

# Open a new file for writing
with open("psu_gpt_no_array.json", "w") as outfile:
    # Write each object to a new line in the output file
    for d in filtered_data:
        outfile.write(json.dumps(d, separators=(",", ": ")) + "\n")
