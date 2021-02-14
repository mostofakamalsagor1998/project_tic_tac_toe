#......................................................Tic-Tac-Toe.....................................................


def main():
    global c
    c = ["X", "O"]  # crosses,noughts
    player_1(input("\n Player 1 : enter your name...! \n" ) )
    player_2(input("\n Player 2 : enter your name...! \n" ) )
    choice()
    profile(1)

def player_1(n):
    global n1
    n1=n
    global g1
    g1=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    global p1
    p1=[]

def player_2(n):
    global n2
    n2=n
    global g2
    g2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    global p2
    p2 = []

def choice():
    s = int(input(n1.upper() + " : please enter your choice...[ \"X\" -> 1 | \"O\" -> 2 ] \n"))

    if s == 1:
        p1.extend(c[s - 1])
        p2.extend(c[1])#Auto choice for player-02

    elif s == 2:
        p1.extend(c[s - 1] )
        p2.extend(c[0] )#Auto choice for player-02

def profile(t):
    print("\n\t\t\t\t\t ### Player\'s Profile ### ")
    print("\n\t\t\t\t\t\t\t\tPlayer-01 : " + n1.upper() +" - Choice : " + "".join(p1))
    print("\n\t\t\t\t\t\t\t\tPlayer-02 : " + n2.upper() +" - Choice : " + "".join(p2) + "\n" )
    start(t)#Priority

def start(t):
    print("\t\t\t\t\t\t Let's start the game : Tic-Tac-Toe! \n")
    startgrid()

def startgrid():#3X3
    print("\t\t\t\t\t\t\t\t      |   |    ")
    print("\t\t\t\t\t\t\t\t  -------------")
    print("\t\t\t\t\t\t\t\t      |   |   ")
    print("\t\t\t\t\t\t\t\t  -------------")
    print("\t\t\t\t\t\t\t\t      |   |   \n")
    # status()
    global g
    g=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
    count=0
    while True:
            #Player-01
            if check(2)!=1:
                help()
                count = count + 1
                print(count)
                set(int(input("\n "+n1.upper()+" please enter box no : [ 1 - 9 ] ")), 1, count)
                if check(1) == 1:
                    break
            #Player-02
            if check(1)!=1 and count<9:
                help()
                count = count + 1
                print(count)
                set(int(input("\n "+n2.upper()+" please enter box no : [ 1 - 9 ] ")), 2, count)
                if check(2 ) == 1:
                    break
            else:
                break
    result()

def set(b, p, t):
    if p==1 and t<=9:
        g1[b-1]=1
        changegrid(1)
        # status()
    elif p==2 and t<=9:
        g2[b-1]=1
        changegrid(2)
        # status()
    else:
        result()

def changegrid(p):
    for x in range(9):
        if g1[x]==1 and p==1:
            g[x]=p1[0]
        elif g2[x]==1 and p==2:
            g[x]=p2[0]
    printgrid()

def result():
    if check(1)==0 and check(2)==0:
        print("\n Match is drawn...! \n")
        say = input("\n Want to play again ? [ Y | N ]" )
        if say.upper() == "Y":
            main()
        else:
            print("\n Thanks for playing " + n1.upper() + " and " + n2.upper() + " ...! \n" )
    else:
        if check(1)==1:
            print(n1.upper()+" is the winner...! \n")
            say = input("\n Want to play again ? [ Y | N ]" )
            if say.upper()=="Y":
                main()
            else:
                print("\n Thanks for playing "+n1.upper()+" and "+n2.upper()+" ...! \n")
        elif check(2)==1:
            print(n2.upper()+" is the winner...! \n")
            say = input("\n Want to play again ? [ Y | N ]" )
            if say.upper() == "Y":
                main()
            else:
                print("\n Thanks for playing " + n1.upper() + " and " + n2.upper() + " ...! \n" )


def check(p):
    if row(p)==1 or col(p)==1 or cor(p)==1:
        return 1
    else:
        return 0

def row(p):
    if p==1:#Player-01
        if g1[0]==1 and g1[1]==1 and g1[2]==1:  #row01 [0-1-2]
            return 1
        elif g1[3]==1 and g1[4]==1 and g1[5]==1:#row02 [3-4-5]
            return 1
        elif g1[6]==1 and g1[7]==1 and g1[8]==1:#row03 [6-7-8]
            return 1
        else:
            return 0
    elif p==2:#Player-02
        if g2[0]==1 and g2[1]==1 and g2[2]==1:  #row01 [0-1-2]
            return 1
        elif g2[3]==1 and g2[4]==1 and g2[5]==1:#row02 [3-4-5]
            return 1
        elif g2[6]==1 and g2[7]==1 and g2[8]==1:#row03 [6-7-8]
            return 1
        else:
            return 0

def col(p):
    if p == 1:#Player-01
        if g1[0]==1 and g1[3]==1 and g1[6]==1:#col01 [0-3-6]
            return 1
        elif g1[1]==1 and g1[4]==1 and g1[7]==1:#col02 [1-4-7]
            return 1
        elif g1[2]==1 and g1[5]==1 and g1[8]==1:#col03 [2-5-8]
            return 1
        else:
            return 0
    elif p==2:#Player-02
        if g2[0]==1 and g2[3]==1 and g2[6]==1:#col01 [0-3-6]
            return 1
        elif g2[1]==1 and g2[4]==1 and g2[7]==1:#col02 [1-4-7]
            return 1
        elif g2[2]==1 and g2[5]==1 and g2[8]==1:#col03 [2-5-8]
            return 1
        else:
            return 0

def cor(p):
    if p == 1:#Player-01
        if g1[0]==1 and g1[4]==1 and g1[8]==1:#cor01 [0-4-8]
            return 1
        elif g1[2]==1 and g1[4]==1 and g1[6]==1:#cor02 [2-4-6]
            return 1
        else:
            return 0
    elif p == 2:#Player-02
        if g2[0]==1 and g2[4]==1 and g2[8]==1:#cor01 [0-4-8]
            return 1
        elif g2[2]==1 and g2[4]==1 and g2[6]==1:#cor02 [2-4-6]
            return 1
        else:
            return 0

def printgrid():
    print("\t\t\t\t\t\t\t\t   "+g[0]+"  |  "+g[1]+"  |  "+g[2])
    print("\t\t\t\t\t\t\t\t -----------------")
    print("\t\t\t\t\t\t\t\t   "+g[3]+"  |  "+g[4]+"  |  "+g[5])
    print("\t\t\t\t\t\t\t\t -----------------")
    print("\t\t\t\t\t\t\t\t   "+g[6]+"  |  "+g[7]+"  |  "+g[8]+"\n")

# def status():
#     print(n1.upper() + " : "+"".join(p1))
#     print(g1)
#     print(n2.upper() + " : "+"".join(p2))
#     print(g2)

def help():
    print("\t\t\t\t\t\t\t\t  [1] | [2] | [3]  ")
    print("\t\t\t\t\t\t\t\t -----------------")
    print("\t\t\t\t\t\t\t\t  [4] | [5] | [6] ")
    print("\t\t\t\t\t\t\t\t -----------------")
    print("\t\t\t\t\t\t\t\t  [7] | [8] | [9] \n")

if __name__=="__main__":
    main()