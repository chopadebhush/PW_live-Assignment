### string manipulations
def String_Manipulations(input_user, operation):
    ## argument has been taken
    if(operation == "reverse"):
        return input_user[::-1]
    elif(operation == "capitalize"):
        return input_user.capitalize()
    else:
        print("Input incorrect")