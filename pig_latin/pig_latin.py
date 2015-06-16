#http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/

# [::-1]

def reverseThatString(theString):
    reversedString = ""
    lenOfString = len(theString)
    for i,j in enumerate(theString):
        lenOfString -= 1
        reversedString += theString[lenOfString]
    return reversedString


def pig_latin(a_string):
    
    
    param_string = a_string.lower()
    param_string_len = len(param_string)
    pig_latin_string = ""
    vowels = ['a','e','i','o','u']
    if param_string[0] not in vowels:
        first_char =  param_string[0]
        if first_char == 'g' and param_string[1] == 'l':
            first_char = (param_string[0] + param_string[1])
            temp = param_string[2:] + first_char
        else:
        #last_char = param_string[param_string_len-1] #last char
            temp = param_string[1:] + first_char
        pig_latin_string += temp
        pig_latin_string += "ay" 
        return pig_latin_string
    else:
        return param_string + "way"



if __name__ == "__main__":
    print pig_latin("pig")
    print pig_latin("banana")
    print pig_latin("trash")
    print pig_latin("happy")
    print pig_latin("duck")
    print pig_latin("glove")
    print pig_latin("egg")
    
