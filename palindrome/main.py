#http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/

# [::-1]



def isPalindrome(theString):
    reversedString = ""
    lenOfString = len(theString)
    for i,j in enumerate(theString):
        lenOfString -= 1
        reversedString += theString[lenOfString]
    return reversedString == theString




if __name__ == "__main__":
    print isPalindrome("lol")
    
