# Enter your code here. Read input from STDIN. Print output to STDOUT
phoneBook = {}
n = int(input())
for i in range (0,n) :
    strTemp = list (input().split(' '))
    phoneBook[strTemp[0]] = strTemp[1]

while True:
    try:
        strTemp = input()
        strPhone = str(phoneBook.get(strTemp))
        if strPhone == 'None' : print ('Not found')
        else : print(strTemp + '=' + strPhone )
    except:
        break


