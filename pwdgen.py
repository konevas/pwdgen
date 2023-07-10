import random
from collections import deque
from argparse import ArgumentParser
from typing import Iterable
import string


SYMBOLS = (string.ascii_letters + string.digits + string.punctuation)


def contain(data: deque, letter_set: list) -> bool:
    return any(item in data for item in letter_set)


def get_pwd(key: str, pwd_len: int) -> Iterable:
    random.seed(key)
    res = deque(maxlen=pwd_len)
    while (len(res) < pwd_len
            or not contain(res, string.ascii_lowercase)
            or not contain(res, string.ascii_uppercase)
            or not contain(res, string.digits)
            or not contain(res, string.punctuation)):
        res.append(SYMBOLS[random.randint(0, len(SYMBOLS) - 1)])
    yield from res


if __name__ == "__main__":
    argparser = ArgumentParser(
        description="Generate password")
    argparser.add_argument(
        '-k',
        '--keyword',
        type=str,
        help='Keyword')
    argparser.add_argument(
        '-l',
        '--length',
        type=int,
        default=16,
        help='Generated password length')

    parsed_args = argparser.parse_args()

    print(''.join(get_pwd(parsed_args.keyword, parsed_args.length)))
