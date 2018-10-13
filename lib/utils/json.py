import json

def json_to_dict(str):
    """Parse a JSON string and load it to a dict

    :param str: JSON string
    :return: an object containing the keys and values in the JSON
    """
    return json.loads(str)

def dict_to_json(dict):
    """Convert a dict to a JSON string

    :param dict: a dict
    :return: a JSON string containing the (key, value) pairs in the dict
    """
    return json.dumps(dict)
