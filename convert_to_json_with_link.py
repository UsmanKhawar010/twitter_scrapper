import re
import json

def parse_tweets(file_path):
    tweets = []
    with open(file_path, 'r', encoding='utf-8') as file:
        tweet_link = ""
        tweet_text = ""
        for line in file:
            line = line.strip()
            if line.startswith("https://") or line.startswith("http://"):
                if tweet_link and tweet_text:
                    tweets.append({"tweet_link": tweet_link.strip(), "tweet_text": tweet_text.strip()})
                    tweet_text = ""
                tweet_link = line
            else:
                tweet_text += line + " "
        if tweet_link and tweet_text:
            tweets.append({"tweet_link": tweet_link.strip(), "tweet_text": tweet_text.strip()})
    return tweets

def save_as_json(tweets, json_file_path):
    with open(json_file_path, 'a', encoding='utf-8') as json_file:
        json.dump(tweets, json_file, indent=2)

if __name__ == "__main__":
    input_file_paths = ["tweets_from_advanced_search.txt"]  # List of input file paths
    output_file_path = "tweets_from_advanced_search_Section.json"
    
    for input_file_path in input_file_paths:
        tweets = parse_tweets(input_file_path)
        save_as_json(tweets, output_file_path)

    print("Data appended to:", output_file_path)
