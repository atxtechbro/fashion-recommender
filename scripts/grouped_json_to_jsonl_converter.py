import json

# Configuration for file paths
config = {
    "input_file_path": "/path/to/your/input_clothing_items.json",
    "output_file_path": "path/to/your/output_grouped_items.jsonl"
}

# Load your large JSON file
with open(config["input_file_path"], 'r') as f:
    data = json.load(f)

# Group items by a specific category, for example, 'type'
grouped_data = {}

for item in data:
    category = item['type']  # Use 'type' or any other category to group by
    if category not in grouped_data:
        grouped_data[category] = []
    grouped_data[category].append(item)

# Write to a JSONL file
with open(config["output_file_path"], 'w') as f:
    for category, items in grouped_data.items():
        json_line = json.dumps({category: items})
        f.write(json_line + '\n')
