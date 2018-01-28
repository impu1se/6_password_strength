import argparse
import re
from getpass import getpass


def get_black_list(file_list):
    with open(file_list, 'r') as f:
        black_list = f.read().split()
        return black_list


def get_user_password():
    return getpass('Input your password: ')


def get_password_strength(password, black_list):
    score = 0
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[$#@!%^&*]', password):
        score += 2
    if len(password) >= 8:
        score += 2
    if len(password) == len(set(password)):
        score += 3
    if password in black_list:
        score = 2
    return score


def main():
    parser = argparse.ArgumentParser(
        description='Show to how much your password is reliable')
    parser.add_argument('-f', dest='file',
                        help='Indicate file for black list')
    args = parser.parse_args()
    password = get_user_password()
    if password and args.file:
        black_list = get_black_list(args.file)
        score = get_password_strength(password, black_list)
        print('Your score is: {score}'.format(score))
    else:
        print("""You didn't input password or file with black list.
            For help enter the password_strength.py -h""")


if __name__ == '__main__':
    main()
