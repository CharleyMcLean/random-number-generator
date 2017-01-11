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

    # make the request
    r = requests.get(url, params=payload, headers=headers)

    # returns a list of random ints but in string format
    rand_ints = (str(r.text.rstrip())).strip().split('\n')

    # returns a list of random ints in integer format
    return [int(num) for num in rand_ints]
