import pytest
#This file contains the functions practice material, commented out.
#Task: Write code to add numbers using functions
'''
def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)

print(added_number + 20)
'''
#Task: write code to calc grade percent and letter using functions
'''
H = float(input("your homework score : " ))
ass = float(input("your assessment score : "))
final = float(input("your final exam score : " ))

def letter(perc):
    if(perc >= 70):
        return( 'A' )
    elif( 70 > perc >=60):
        return( 'B' )
    elif( 60 > perc >= 50):
        return ( 'C')
    elif(50> perc >= 40):
        return ('D')
    else :
        return ('F')

def grades(H,ass,final):
    H = (H /25)*100
    hletter = letter(H)
    ass = (ass /50)*100
    assletter = letter(ass)
    final = final
    finalletter = letter(final)
    return H,hletter, ass,assletter, final,finalletter

print(f"Homework, assessment and final exam Percentages : {grades(H,ass,final)}")
'''
#Task Near - Additional tasks

#Create a fn that when given two strings of letters, determines whether the 2nd can be made from the first by removing one letter
'''
def near(a,b):
    trial=""
    yasss = False
    for j in range(0, len(a)):
        for i in range(0,len(a)):
            if i != j:
                trial= trial + a[i]
        if (trial == b):
            yasss = True
        trial =""
    return yasss

print("Find out if removing a letter from string1 makes string2!")
print( "String1 should be larger than string 2 for this to work")
a = input("string1 : ")
b = input("string2 : ")

print(near(a,b))

'''
#Task QA practice, timestables
#  Formatting is ugly, further work could be adaptive spacing.
'''
def timestables(num):
    length = num
    for i in range(1,num + 1):
        rowstring = ''
        for j in range(1, num + 1):
            ij =i*j
            if(ij < 10):
                rowstring = rowstring + '  '+ str(ij)
            else:
                rowstring = rowstring + ' ' + str(ij)

        print(rowstring)

    return 'done!'

num = int( input("Input a number to get the timestables of:" ))

print(timestables(num))

'''
