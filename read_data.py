import json


def fromJson(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    f = open(file_path, 'r', encoding='utf8')
    x = f.read()
    return json.loads(x)
path = 'data/result.json'
#print(fromJson(path))