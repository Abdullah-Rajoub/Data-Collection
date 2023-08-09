import json
import csv

path = "C:/Users/kinga/Desktop/scripts/psu_all.json"
# Open the output.json file for reading
with open(
    path,
    "r",
    encoding="UTF-8",
) as infile:
    # Load the JSON data from the file
    data = json.load(infile)

    # Extract the prompt and completion fields from each JSON object in the array
    filtered_data = [
        {
            "prompt": d.get("prompt"),
            "completion": d.get("completion"),
            "URL": d.get("URL"),
            "pageType": d.get("pageType"),
            "date": d.get("date"),
        }
        for d in data
    ]

# Open the output.csv file for writing
with open("psu_all.csv", "w", newline="", encoding="utf-8") as outfile:
    # Create a CSV writer object
    writer = csv.DictWriter(
        outfile, fieldnames=["prompt", "completion", "URL", "pageType", "date"]
    )

    # Write the header row to the CSV file
    writer.writeheader()

    # Write each JSON object as a row in the CSV file
    for d in filtered_data:
        writer.writerow(d)
