import random
import string


upper=list(string.ascii_uppercase)
lower=list(string.ascii_lowercase)
digits=list(string.digits)
punctuation=list(string.punctuation)
cont=True
while(cont):
    num_char=input("enter the number of letters :")
    while(True):
        try:
            num_char=int(num_char)
            if(num_char>=6 and num_char<=26):
                break
            else:
                print("It should be between 6 - 26 letters ")
                num_char=input("enter the number of letters again :")
        except:
            print("please enter a number !")
            num_char=input("enter the number of letters :")
            
    random.shuffle(upper)
    random.shuffle(lower)
    random.shuffle(digits)
    random.shuffle(punctuation)


    part1=round(num_char*(30/100))
    part2=round(num_char*(20/100))

    password=[]
    for i in range(part1):
        password.append(lower[i])
        password.append(digits[i])

    for i in range(part2):
        password.append(upper[i])
        password.append(punctuation[i])
    random.shuffle(password)
    string=''.join(password)
    print(f"Your password is : {string}")
    plate=input("You need your password for what? ")
    try:
        file = open("-----Your file path here---","a")
        file.write(f"{plate} : \n")
        file.write(f"{string} \n")
        file.write("-------------------\n")
    except:
        print("File not found")
    request=input("Do you want to continue Y/N ?")
    if(request=='Y' or request=='y'):
        cont=True
    elif(request=='N' or request=='n'):
        cont=False
        print("--Goodbye--")
    else:
        print("Wrong input!!")
        print("--Am out--")
        cont=False
