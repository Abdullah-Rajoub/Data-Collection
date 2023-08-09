import json

# Open the output.json file for reading with UTF-8 encoding
with open("psu_all.json", "r", encoding="utf-8") as infile:
    # Load the JSON data from the file
    data = json.load(infile)

    # Extract the prompt and completion fields from each JSON object in the array
    filtered_data = [
        {"prompt": d["prompt"], "completion": d["completion"]} for d in data
    ]

# Open a new file for writing
with open("filtered_output.json", "w") as outfile:
    # Write the filtered data to the new file
    json.dump(filtered_data, outfile)
