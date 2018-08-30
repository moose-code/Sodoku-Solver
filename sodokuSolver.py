# Jonathan Clark
# 19 April 2013
# program to solve soduku grid


def grid():  # function used to enter the list into becoming a 2D array
    grid = []
    lin = []

    for i in range(0, 9):
        row = input('')
        lin = []
        for x in range(0, 9):
            num = int(row[x])
            lin.append(num)
        grid.append(lin)
    return grid


def solution(box):  # MY SOLVER!!!!!!!
    chilling = 0
    for i in range(9):  # i and p symbolise coordinates of the grid
        for p in range(9):
            if int(box[i][p]) != 0:  # if part of the grid is a number already, nothing happens
                chilling = 0
            else:

                possible = []  # Here is the magic
                for j in range(1, 10):  # If it a zero on the grid, my solver runs through number 1 to 9 and if one is a possible solution, it appends it to a possible solution list for that block, my list length is then checked and if the block has only one possible solution it fills that solution into the block. Grid is returned and function is run again :)

                    if box[i].count(j) >= 1:
                        row = 20  # meaning fail
                    else:
                        row = 30  # meaning pass

                    cols = []
                    for lk in range(9):  # i check for possible solutions by creating a list of colums, rows and three by three blocks pertaining to that specific block, then use count function to check that number doesnt occour
                        cols.append(box[lk][p])
                    if cols.count(j) >= 1:
                        colum = 20
                    else:
                        colum = 30

                    angel = []

                    if 0 <= i <= 2 and 0 <= p <= 2:
                        for t in range(3):
                            ang = box[t]
                            for u in range(3):
                                angel.append(ang[u])

                    elif 0 <= i <= 2 and 3 <= p <= 5:
                        for t in range(3):
                            ang = box[t]
                            for u in range(3, 6):
                                angel.append(ang[u])

                    elif 0 <= i <= 2 and 6 <= p <= 8:
                        for t in range(3):
                            ang = box[t]
                            for u in range(6, 9):
                                angel.append(ang[u])

                    elif 3 <= i <= 5 and 0 <= p <= 2:
                        for t in range(3, 6):
                            ang = box[t]
                            for u in range(3):
                                angel.append(ang[u])

                    elif 3 <= i <= 5 and 3 <= p <= 5:
                        for t in range(3, 6):
                            ang = box[t]
                            for u in range(3, 6):
                                angel.append(ang[u])

                    elif 3 <= i <= 5 and 6 <= p <= 8:
                        for t in range(3, 6):
                            ang = box[t]
                            for u in range(6, 9):
                                angel.append(ang[u])

                    elif 6 <= i <= 8 and 0 <= p <= 2:
                        for t in range(6, 9):
                            ang = box[t]
                            for u in range(3):
                                angel.append(ang[u])

                    elif 6 <= i <= 8 and 3 <= p <= 5:
                        for t in range(6, 9):
                            ang = box[t]
                            for u in range(3, 6):
                                angel.append(ang[u])

                    elif 6 <= i <= 8 and 6 <= p <= 8:
                        for t in range(6, 9):
                            ang = box[t]
                            for u in range(6, 9):
                                angel.append(ang[u])

                    if angel.count(j) >= 1:
                        block = 20
                    else:
                        block = 30

                    if row == 30 and colum == 30 and block == 30:
                        possible.append(j)
                if len(possible) == 1:
                    box[i][p] = possible[0]
                    return box


def more():  # function created to keep running the solver until grid is completely solved
    box = grid()
    newbox = solution(box)
    l = 1
    for q in range(9):
        for d in range(9):
            if newbox[q][d] == 0:
                l = 0

    while l == 0:
        l = 1
        newbox = solution(newbox)
        for q in range(9):
            for d in range(9):
                if newbox[q][d] == 0:
                    l = 0

    for i in range(9):
        for j in range(9):
            print(newbox[i][j], sep="", end="")
        print()


# winning
more()    # (did more bugging than an anthropologist)
