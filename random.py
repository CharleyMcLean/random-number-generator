import requests


def generate_rand_ints(num, mini, maxi, col, base, email, format='plain',
                       rnd='new', url='https://www.random.org/integers/'):
    # all inputs need to be in string format
    payload = {'num': num,
               'min': mini,
               'max': maxi,
               'col': col,
               'base': base,
               'format': format,
               'rnd': rnd}

    headers = {'user-agent': email}

    r = requests.get(url, params=payload, headers=headers)

    # split on the new line
    return r.text.split('\n')
