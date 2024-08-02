import pandas as pd
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv

def reddit_pipeline(file_name: str,
                    subreddit: str,
                    time_filter: str = 'day',
                    limit: int = None):
    
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)

    # transformation
    post_df = transform_data(pd.DataFrame(posts))

    # loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path 