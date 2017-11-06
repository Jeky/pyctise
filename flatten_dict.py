#
# Flatten a dict to a list. All the keys will be the first elements in tuples in the flattened list while the values will be the second ones in tuples.
# dict = {
#     'a' : 1,
#     'b' : 2
# }
# will be flattened to:
# flattened_list = [('a', 1), ('b', 2)]

def flatten_dict(dic: dict, recursive: bool = True) -> list:
    """Flatten a dict to a list
    """
    if not recursive:
        return list(dic.items())
    else:
        flattened_list = []
        for k, v in dic.items():
            if type(v) == dict:
                flattened_list.append((k, flatten_dict(v)))
            else:
                flattened_list.append((k, v))

        return flattened_list


if __name__ == '__main__':
    dic = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'special' : {
            'aaa' : 111,
            'bbb' : 222
        }
    }

    print(flatten_dict(dic))
