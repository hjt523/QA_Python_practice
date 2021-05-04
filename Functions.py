#This file contains the functions practice material, commented out.
'''
def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)

print(added_number + 20)
'''

H = float(input("your homework score : " ))
ass = float(input("your assessment score : "))
final = float(input("your final exam score : " ))

def letter(perc):
    if(perc >= 90):
        return( 'A' )
    elif( 90 > perc >=80):
        return( 'B' )
    elif( 80 > perc >= 70):
        return ( 'C')
    elif(70 > perc >= 60):
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



