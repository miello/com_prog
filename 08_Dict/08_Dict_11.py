def reverse(d):
    new_dict = dict()
    for key, val in d.items():
        new_dict[val] = key
    return new_dict


def keys(d, v):
    arr = []
    for key, val in d.items():
        if v == val:
            arr.append(key)
    return arr


exec(input().strip())
