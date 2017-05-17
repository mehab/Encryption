def InputText():
    name=input("Enter your name")
    if len(name)<10:
        while len(name)<10:
            name=name+'x'
    name=name.upper()
    print(name)
    studentId=input("Enter your student id")
    if len(studentId)!=10:
        print("The student id is invalid")
    else:
        if studentId.isdigit()==True:
            print("It is a valid student id")
        else :
            print("It is an invalid student id")
    
    plainText=name+' '+studentId+'.'
    print(plainText)
    return plainText
