import json

def extract_tweet_text(json_file_path, output_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for idx, tweet in enumerate(data, start=1):
            tweet_text = tweet['tweet_text']
            # Write the tweet text to the output file
            output_file.write(f"{tweet_text}\n\n")

if __name__ == "__main__":
    json_file_path = "./final files singular/Tweets_without_RT.json"  # Replace with the path to your JSON file
    output_file_path = "./final files singular/Tweets_without_RT.txt"  # Replace with the desired output text file path
    extract_tweet_text(json_file_path, output_file_path)
