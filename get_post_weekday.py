from read_data import fromJson
import datetime 
def get_post_weekday(data:dict,weekday:int)->dict:
    """
    Return the number of posts for each weekday
    args:
        data: a dictionary of posts
    returns: a dictionary with the number of posts for each weekday
    """
    messages = data.get('messages')
    answer = {
        weekday:0
    }
    for message in messages:
        date = message['date']
        date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        weekday_n = int(date.strftime("%w"))
        s = answer.get(weekday_n)
        if s != None:
            answer[weekday_n] += 1
    return answer
data = fromJson('data/result.json')
print(get_post_weekday(data, 1))