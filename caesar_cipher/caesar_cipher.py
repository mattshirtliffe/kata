import string
import collections

def cipher(offset,word):
    alpha = string.ascii_lowercase    
    d = collections.deque([],len(alpha))
    for i in alpha:
        d.append(i)
    d.rotate(offset)
    alpha = list(alpha)
    d = list(d)
    
    new_word = ""
    for letter in word:
        new_word += d[alpha.index(letter)]
    return new_word


if __name__ == "__main__":
    print cipher(-13,'abcdefghijklmnopqrstuvwxyz')
    
