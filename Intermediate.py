#Task- QA- Best Conjugation
#Find out how many different words you can make,
#  from smaller valid sub-words.



def wordlist():
    file = open("wordlist.txt","r")
    with open("wordlist.txt","r") as f:
        length= len(f.readlines())  # This would give length of files. 
    
    for i in range (0, length):
        words.append(file.readline())

    f.close()
    file.close()
    return words
words =[]

words = wordlist()

bigword = input("Enter a word to see if it can be formed with smaller words : " )

word = words[16579]
word.replace(' ','')

Found = []
Foundat = []

for i in range(0, len(words)):
    if(len(words[i].rstrip() )> 1 ):

        if (bigword.find(words[i].rstrip()) != -1):
            print(bigword.find(words[i].rstrip()))
            print(words[i].rstrip())
            Found.append(words[i].rstrip)
            Foundat.append(bigword.find(words[i].rstrip()))



         
       


