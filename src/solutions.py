from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from memory_profiler import profile
from typing import List, Tuple
import emoji
import json

@profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """ The function examines a json file containing tweets and returns the top 10 dates with the 
    most tweets and the user with the most posts for each of those days. Time optimized function.
 
    Params
    ----------
    file_path : str
        Path to json file.

    Returns
    -------
    list
        Returns a list with the top ten tuples with date and the username with the most published 
        tweets on that day.
    """

    tweet_count_by_date_user = Counter()
    top_dates = []
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date_str = tweet['date'].split('T')[0]
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            username = tweet['user']['username']
            tweet_count_by_date_user[(date, username)] += 1

    top_date_user_combinations = tweet_count_by_date_user.most_common(10)
    return [(date, user) for (date, user), _ in top_date_user_combinations]

@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """ The function examines a json file containing tweets and returns the top 10 dates with the 
    most tweets and the user with the most posts for each of those days. Memory optimized function.
 
    Params
    ----------
    file_path : str
        Path to json file.

    Returns
    -------
    list
        Returns a list with the top ten tuples with date and the username with the most published 
        tweets on that day.
    """
    tweet_count_by_date_user = {}
    top_dates = []
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date_str = tweet['date'].split('T')[0]
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            username = tweet['user']['username']

            if date in tweet_count_by_date_user:
                if username in tweet_count_by_date_user[date]:
                    tweet_count_by_date_user[date][username] += 1
                else:
                    tweet_count_by_date_user[date][username] = 1
            else:
                tweet_count_by_date_user[date] = {username: 1}

    for date, user_counts in tweet_count_by_date_user.items():
        top_user = max(user_counts, key=user_counts.get)
        top_dates.append((date, top_user))

    top_dates.sort(key=lambda x: sum(tweet_count_by_date_user[x[0]].values()), reverse=True)
    return top_dates[:10]


@profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """ The function examines a json file containing tweets and returns the top 10 with the 
    most used emojis and the count of each one. Optimized function at time.
 
    Params
    ----------
    file_path : str
        Path to json file.

    Returns
    -------
    list
        Returns a list with the top ten tuples with most used emojis and the number of occurences.
    """
    emoji_counts = Counter() 

    def process_line(line):
        import emoji
        tweet = json.loads(line)
        content = tweet['content']
        emoji_list = emoji.emoji_list(content)
        return [emoji_data['emoji'] for emoji_data in emoji_list]

    with open(file_path, 'r') as file:
        lines = file.readlines()

        with ThreadPoolExecutor() as executor:
            emojis_lists = list(executor.map(process_line, lines))

        for emoji_list in emojis_lists:
            for emoji in emoji_list:
                emoji_counts[emoji] += 1 

    top_10_emojis = emoji_counts.most_common(10)
    return top_10_emojis

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """ The function examines a json file containing tweets and returns the top 10 with the 
    most used emojis and the count of each one. Memory optimized function.
 
    Params
    ----------
    file_path : str
        Path to json file.

    Returns
    -------
    list
        Returns a list with the top ten tuples with most used emojis and the number of occurences.
    """
    emoji_count = Counter()
    all_emojis = emoji.distinct_emoji_list('')
    emoji_set = set(all_emojis)

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet['content']
            emojis = [char for char in content if char in emoji_set]
            emoji_count.update(emojis)

    top_emojis = emoji_count.most_common(10)
    return top_emojis


@profile
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """ The function examines a json file containing tweets and returns the top 10 most influential
    users based on the number of received mentions. Time optimized function.
 
    Params
    ----------
    file_path : str
        Path to json file.

    Returns
    -------
    list
        Returns a list with the top ten tuples with username and number of mentions.
    """
    mentions_counts = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            mentioned_users = tweet.get('mentionedUsers')
            if mentioned_users:
                for user_info in mentioned_users:
                    user = user_info.get('username')
                    if user:
                        mentions_counts[user] += 1

    top_10_users = mentions_counts.most_common(10)
    return top_10_users

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """ The function examines a json file containing tweets and returns the top 10 most influential
    users based on the number of received mentions. Memory optimized function.
 
    Params
    ----------
    file_path : str
        Path to json file.

    Returns
    -------
    list
        Returns a list with the top ten tuples with username and number of mentions.
    """
    mentions_counts = {}

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            mentioned_users = tweet.get('mentionedUsers')
            if mentioned_users:
                for user_info in mentioned_users:
                    user = user_info.get('username')
                    if user:
                        if user in mentions_counts:
                            mentions_counts[user] += 1
                        else:
                            mentions_counts[user] = 1

    top_10_users = sorted(mentions_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_10_users