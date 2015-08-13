import string
import collections

def rot13(word):
    
    alpha = string.ascii_lowercase + string.ascii_uppercase
    d = collections.deque([],len(alpha))
    for i in alpha:
        d.append(i)
    d.rotate(13)
    alpha = list(alpha)
    d = list(d)
    
    new_word = ""
    for letter in word:
        new_word += d[alpha.index(letter)]
    return new_word


if __name__ == "__main__":
    print rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    
