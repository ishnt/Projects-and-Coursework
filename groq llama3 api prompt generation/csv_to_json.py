import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Convert CSV data to a list of dictionaries
        data = []
        for row in csv_reader:
            # Remove leading/trailing whitespaces and newline characters from each field
            cleaned_row = {key: value.strip().replace('\n', '').replace('\r', '') for key, value in row.items()}
            data.append(cleaned_row)
    
    # Write the JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Example usage
csv_file_path = 'E:\internship taks\groq llama3 api prompt generation\Copy of Copy of AI Project Data Training Sheet - Data Sheet.csv'  # Replace with your CSV file path
json_file_path = 'E:\internship taks\groq llama3 api prompt generation\Copy of Copy of AI Project Data Training Sheet - Data Sheet.json'  # Replace with your desired JSON file path

csv_to_json(csv_file_path, json_file_path)

