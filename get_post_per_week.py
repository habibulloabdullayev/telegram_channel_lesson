from read_data import fromJson
from datetime import datetime
def get_post_per_week(data:dict,month:int)->dict:
    """
    Return the number of posts for each week of a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        dict: a dictionary with the number of posts for each week.
    """
    messages = data.get('messages')
    for message in messages:
        date = message['date']
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        month_n = int(date.strftime('%m'))
        weekday_n = int(date.strftime("%w"))
        

data = fromJson('data/result.json')