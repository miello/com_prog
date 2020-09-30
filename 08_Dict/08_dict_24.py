button = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}


def text2keys(text):
    text = text.lower()
    ans = []
    for p in text:
        for key, val in button.items():
            if p in val:
                idx = val.find(p)
                t = ''
                for l in range(idx + 1):
                    t += str(key)
                ans.append(t)
                break
    return ' '.join(ans)


def keys2text(keys):
    keys = keys.split()
    text = ''
    for p in keys:
        t = p[0]
        plen = len(p) - 1
        text += button[t][plen]
    return text


exec(input().strip())
