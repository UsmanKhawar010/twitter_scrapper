import json

def filter_duplicates(json_file_path):
    unique_tweets = set()
    unique_records = []
    
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for tweet in data:
        tweet_text = tweet['tweet_text']
        # Check if the tweet text is not already in the set of unique tweets
        if tweet_text not in unique_tweets:
            unique_tweets.add(tweet_text)
            unique_records.append(tweet)
    
    return unique_records

if __name__ == "__main__":
    json_file_path = "./final files singular/singular_combined_tweets.json"  # Replace with the path to your JSON file
    unique_records = filter_duplicates(json_file_path)
    
    # Write the unique records to a new JSON file
    output_file_path = "./final files singular/filter_singular_combined_tweets.json"
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(unique_records, file, indent=2)
