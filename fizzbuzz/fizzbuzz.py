

def fizz_buzz():
    for i in range(0,100):
        fizzy_bizzy = ""
        if i % 3 == 0:
            fizzy_bizzy += "Fizz"
        if i % 5 == 0:
            fizzy_bizzy += "Buzz"
        
        if fizzy_bizzy == "":
            fizzy_bizzy += str(i)

        print fizzy_bizzy


def fizz_buzzy(i):

    fizzy_bizzy = ""
    if i % 3 == 0:
        fizzy_bizzy += "Fizz"
    if i % 5 == 0:
        fizzy_bizzy += "Buzz"
    if fizzy_bizzy == "":
        fizzy_bizzy += str(i)

    return fizzy_bizzy
    

if __name__ == "__main__":
    #fizz_buzz()
    print fizz_buzzy(90)
