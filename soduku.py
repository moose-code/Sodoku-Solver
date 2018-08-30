print("soduku solver")


def grid():     #function used to enter the list into becoming a 2D array
   grid = []  
   lin  = []
   
   for i in range(0,9): 
      row = input('')
      lin = []
      for x in range(0,9):
         num = int(row[x])
         lin.append(num)
      grid.append(lin)
   return grid


print(grid())

