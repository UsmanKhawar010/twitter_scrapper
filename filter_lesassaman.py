import re

def filter_tweets(file_path, username, output_file_path):
    lensassaman_tweets = []
    with open(file_path, 'r', encoding='utf-8') as file:
        tweet_url = None
        tweet_text = None
        for line in file:
            if line.startswith("https://twitter.com/" + username + "/status/"):
                # If a tweet URL is found, store it
                tweet_url = line.strip()
            elif tweet_url is not None:
                # If text follows the tweet URL, store the tweet
                tweet_text = line.strip()
                lensassaman_tweets.append({"tweet_url": tweet_url, "tweet_text": tweet_text})
                # Reset tweet URL for the next tweet
                tweet_url = None
                
    # Append the filtered tweets to the existing file
    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        for tweet in lensassaman_tweets:
            output_file.write(tweet["tweet_url"] + "\n" + tweet["tweet_text"] + "\n\n")

if __name__ == "__main__":
    input_file_path = "combined.txt"
    output_file_path = "combined_filtered_tweets.txt"
    username = "lensassaman"
    filter_tweets(input_file_path, username, output_file_path)
    print("Filtered tweets appended to:", output_file_path)
