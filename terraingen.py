from ursina import *
from math import *
from time import *

terrainy= [[0]*30 for _ in range(30)]
for x in range(30):
    for z in range(30):
        terrainy[x][z]="*"

#Lrow=0
Lrow=random.randint(0,15)
#Lcol=0
Lcol=random.randint(0,15)
#Hrow=10
Hrow=random.randint(15,30)
#Hcol=10
Hcol=random.randint(15,30)
#Hpoint=10
Hpoint=random.randint(-15,0)
#Lpoint=0
Lpoint=random.randint(-30,-15)
mid=(Hpoint+Lpoint)/2
def ClosestTo(Lrow,Lcol,Hrow,Hcol,Mrow,Mcol):
  dmtL=math.sqrt(abs((Lrow-Mrow)*(Lrow-Mrow))+abs((Lcol-Mcol)*(Lcol-Mcol))) 
  dmtH=math.sqrt(abs((Hrow-Mrow)*(Hrow-Mrow))+abs((Hcol-Mcol)*(Hcol-Mcol))) 
 # print(dmtH,"<dmtH   dmtL>",dmtL)
  if dmtL>dmtH:
      if dmtL:
          return "is Low"
      else:
        return "Closest to Low"
  elif dmtH>dmtL:
      if dmtH==0:
          return "is High"
      else:
        return "Closest to High"
  else:
    return "Equidistant"
def OnBoard(row, col):
    if 0 <= row < 30 and 0 <= col < 30:
        return True
    else:
        return False
def RandomHeight(list, row, col, mid):
    if not OnBoard(row, col):
        return
    print(Hpoint,"<Hpoint-----Lpoint>",Lpoint)
    if list[row][col] == "*":
       # print(ClosestTo(Lrow, Lcol, Hrow, Hcol, row, col))
        if ClosestTo(Lrow, Lcol, Hrow, Hcol, row, col) == "Closest to Low":
            list[row][col] = mid - 1
            Npoint=mid-1
        elif ClosestTo(Lrow, Lcol, Hrow, Hcol, row, col) == "Closest to High":
            list[row][col] = mid + 1
            Npoint=mid+1
        elif ClosestTo(Lrow, Lcol, Hrow, Hcol, row, col) == "is High":
            list[row][col]=Hpoint
            Npoint=Hpoint
        elif ClosestTo(Lrow, Lcol, Hrow, Hcol, row, col) == "is Low":
            list[row][col]=Lpoint
            Npoint=Lpoint
        else:
            list[row][col] = mid
            Npoint=mid
    else:
        return
     
