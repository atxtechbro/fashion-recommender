import requests
import json
import os

# Configuration for file paths and API endpoint
config = {
    "input_json_file": "sample_clothing_items.json",
    "api_base_url": "http://localhost:8000/api/v1/clothing-items/",
    "output_log_file": "insertion_log.txt"  # Optional: Log the results to a file
}

def load_clothing_items(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r') as file:
        content = file.read()
        
        if not content:
            raise ValueError(f"The file {file_path} is empty.")
        
        items = json.loads(content)
    
    return items

def insert_clothing_item(item, api_url, log_file=None):
    response = requests.post(api_url, json=item)
    
    log_message = ""
    if response.status_code == 200:
        log_message = f"Successfully inserted item: {item['type']} with primary color {item['color_primary_name']}\n"
    else:
        log_message = f"Failed to insert item: {item['type']}, status code: {response.status_code}, response: {response.text}\n"
    
    print(log_message.strip())
    
    if log_file:
        with open(log_file, 'a') as lf:
            lf.write(log_message)

def main():
    # Resolve paths dynamically based on the script's location
    script_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(script_dir, config["input_json_file"])
    log_file_path = os.path.join(script_dir, config["output_log_file"])
    
    print(f"Loading clothing items from: {json_file_path}")
    items = load_clothing_items(json_file_path)

    for item in items:
        insert_clothing_item(item, config["api_base_url"], log_file_path)

if __name__ == "__main__":
    main()
