#http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/

# [::-1]

def reverseThatString(theString):
    reversedString = ""
    lenOfString = len(theString)
    for i,j in enumerate(theString):
        lenOfString -= 1
        reversedString += theString[lenOfString]
    return reversedString


def number_of_vowels(a_string):
    count = 0
    vowels = ['a','e','i','o','u']
    for charz in a_string:
        if charz in vowels:
            count+=1
    return count

    

if __name__ == "__main__":
    print number_of_vowels("piiiiiig")
    
