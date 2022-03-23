def plateau_simple(n):
    p = []
    for i in range (n-1):
        for j in range (n-1):
            p.append((i,j))
    return p

def plateau_pond(n):
   p = dict()
   # création de l'echequier qu'on initialise à 8
   for i in range (n+1):
       for j in range (n+1):
           p[i,j] = 8
 
   # on initialise les 6
   for i in range (n+1):
       for j in range (n+1):
           if  i==1 or j==1 or i==n-1 or j==n-1:
              p[i,j] = 6

   # on initialise les 4
   for i in range (n+1):
       for j in range (n+1):
           if  i==0 or j==0 or i==n or j==n:
              p[i,j] = 4
   p[1,1] = 4
   p[n-1,1] = 4
   p[1,n-1] = 4
   p[n-1,n-1] = 4

   # on initialise les coins 2
   p[0,0] = 2
   p[0,n] = 2
   p[n,0] = 2
   p[n,n] = 2

   # on initialise les 3
   p[0,1] = 3
   p[1,0] = 3
   p[0,n-1] = 3
   p[1,n] = 3
   p[n-1,0] = 3
   p[n,1] = 3
   p[n,n-1] = 3
   p[n-1,n] = 3

   return p    

def deplacement(x,y):
    return  tuple(map(lambda i, j: i + j, x, y))

def compare(a, n):
    min = 0
    max = n
    if(a[0]>=min and a[0]<=max):
        if(a[1]>=min and a[1]<=max):
            return True
    return False
   

def Cavalier(pion, n):
    Sauts = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    echequier = plateau_pond(n)
    Avisiter = plateau_simple(n)
    parcours = []
    pond = 10 #plus que 8
    print(pion)
    while (Avisiter != []):
        parcours.append(pion)
        Avisiter.remove(pion)
        Avisiter.clear()
        for i in range (8):
            print(i)
            if (deplacement(pion, Sauts[i]) == True):
                print("test")
                pond = echequier.get(deplacement(pion, Sauts[i]))
    print(pond)
    print(parcours)
    return parcours


Cavalier((0,0), 9)

for i in range (8):
    pion = (0,0)
    Sauts = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    print(i)
    print(deplacement(pion, Sauts[i]))


    
