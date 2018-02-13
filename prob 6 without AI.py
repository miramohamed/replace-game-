arr1=['b','c','a','q','z','f','e','b','z','d','e','t','q','m','c','f','m','t','d','a']
arr2=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]

score1=0
score2=0

changer=1

def printfunction():
    for x in arr2:
        print(x,end=" ")
    print()


print ("this game has a rule you aren't allowed to choose the same no. in a one turn else you will be deprived from your turn")
print("choose players")

changer=1
print ("player 1 please enter your name : ")
f= str (input())
print ("player 2 please enter your name : ")
k= str (input())


while True:
    if(changer == 1):
        print ("welcome :")
        printfunction()
        print (f , "score" , score1)
        numbers = input ("please enter 2 numbers")
        i,j =numbers.split (",")
        i=int(i)
        j=int(j)
        changer = 2
    elif(changer == 2):
        print ("welcome :")
        printfunction()
        print(k , "score" , score2)
        numbers = input ("please enter 2 numbers")
        i,j =numbers.split (",")
        i=int(i)
        j=int(j)
        changer = 1
    if arr1[i-1]!=arr1[j-1]:
        temp1=arr2[i-1]
        temp2=arr2[j-1]
        arr2[i-1]=arr1[i-1]
        arr2[j-1]=arr1[j-1]
        printfunction()
        arr2[i-1] = temp1
        arr2[j-1] = temp2
    else :
        arr2[i-1]=arr1 [i-1]
        arr2[j-1]=arr1 [j-1]
        printfunction()
        arr2[i-1]='*'
        arr2[j-1]='*'
        
        if (changer == 2):
            score1 += 1
        else :
            score2 += 1
    if score1 + score2 ==10:
        if score1==score2:
            print("DRAW")
            break
        elif (score1> score2):
            print (f, "wins")
            break
        elif (score2>score1):
            print(k, " wins")
            break
        
                

