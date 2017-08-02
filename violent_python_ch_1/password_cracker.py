import crypt
import argparse


def crack_pass(ctext, pw_dict):
    salt = ctext[0:2]
    with open(pw_dict, 'r') as pw_dict:
        for word in pw_dict.readlines():
            word = word.strip()
            crypt_word = crypt.crypt(word, salt)
            if crypt_word == ctext:
                return word
    return None 


def analyze_file(filename, pw_dict):
    with open(filename, 'r') as f:
        for line in f.readlines():
            (user, pword) = tuple([x.strip() for x in line.split(':')[0:2]])
            plaintext = crack_pass(pword, pw_dict)
            if plaintext:
                print('User: {}\tPassword: {}'.format(user, plaintext))
            else:
                print('User: {}\tNo Password Found'.format(user))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--dict', default='dictionary.txt')
    args = parser.parse_args()

    analyze_file(args.filename, args.dict)

if __name__ == '__main__':
    main()
