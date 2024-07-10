value=[]
train=[]
teddad_vagon=input()
def move (player):
 
 for i in range (n):
    if train[i]==player[1] :
     place=i
    if player  [2] == "left":
        train [i-1] = train[i]
        train .pop(i)
    if player [2] == "right":
        train [i-1] = train[i]
        train .pop(i)

def upddown (player):
    if player  [3] =="up":
       player  [3]="down"
    if player  [3] =="doen":
       player  [3] ="up"

def  turn ( player):
    if player  [2] == "right":
        player [2] ="left"
    if player  [2] == "left":
        player [2] = "right"

 
def shoot (player):
    for i in range (n):
        if train[i]==player[1] :
            place=i
    if player [2] =="left":
        for j in range(i, 0, -1):
            if player [5]:"stand"
            player [5] ="sleep"
            break 
        if player [2] == "right":
            for k in range (i , teddad_vagon):
                if player [5] =="stand" :
                    player [5] = "sleep"
                    break

 