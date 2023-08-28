from read_data import fromJson
import datatime

def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """  
    msgs = data.get('messages')
    answer = {}
    for msg in msgs:
        date = msg['date']
        date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        year = date.year
        d = date.day
        month = date.month
        answer.setdefault(month, {})
        month_day: dict = answer[month]
        month_day['day'] = day
        count = month_day.setdefault('count', 0)
        if day == d:
            month_day['count'] += 1
    return print(answer)
print(get_post_per_month(fromJson('data/result.json')))