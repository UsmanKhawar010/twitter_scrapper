import json

def count_records(json_file_path):
    # Load the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Count the number of records
    num_records = len(data)
    
    return num_records

if __name__ == "__main__":
    json_file_path = "./final files singular/lensassaman_filter_singular_combined_tweets.json"  # Replace with the path to your JSON file
    num_records = count_records(json_file_path)
    
    print("Number of records in the JSON file:", num_records)
