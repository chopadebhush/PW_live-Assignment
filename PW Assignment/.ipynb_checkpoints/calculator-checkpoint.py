def calculators(a,b,opeartion):
    ## Operation & Arugument taken here
    ## addition of field
    if(opeartion == "addition"):
        return a+b
    ## Subtraction of field
    elif(opeartion == "subtraction"):
        return a-b
    ## multiplication of field
    elif(opeartion == "multiplication"):
        return a*b
    ## divison of field
    elif(opeartion =="divison"):
        return a/b
    else:
        print("Incorrect input from user")