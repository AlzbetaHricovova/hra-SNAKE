"""
Cielom je naprogramovat hru kde macka (hlava macky oznacena "H", telo "o") zerie mysi
(oznacenie "M"). Ked macka mys zozerie zvacsi sa o 1 ("o"). Macka sa ovlada WSAD (hore, dole, dolava, doprava).
Na zaciatku sa vygeneruje plan hry o zadanych rozmeroch  a pocte mysi - pociatocna pozicia macky a misy je nahodna.
game(10,7, 7) - 10(sirka)x7(vyska), 7 pocet misy.
Deadline: 15.11.2018 17:00
"""
import random

#generate empty board with walls
def create_board(width, height):
    board=[]
    for h in range(height+1, -1, -1):
        row=[]
        for w in range (width+2):
            if h==0 or h==(height+1):
                if w==0 or w==(width+1):
                    row.append(".")
                else:
                    row.append(w%10)

            else:
                if w==0 or w==(width+1):
                    row.append(h%10)
                else:
                    row.append(" ")
        board.append(row)
    return(board)
create_board(10, 7)

#print board with items
def print_board(board):
    for row in board:
        for item in row:
            print(item, end="")
        print()


#set cell in board with coordinates pos =(x,y) to value (character)
def set_item(board, pos, value):
    x,y=pos
    y=len(board)-1-y
    board[y][x]= value
    return(board)


#return character on pos in board
def get_item(board, pos):
    x,y=pos
    y=len(board)-1-y
    return(board[y][x])


#rand position inside(except edge) board
def rand_pos(board):
    width=len(board[0])-2
    height=len(board)-2
    x=random.randint(1,width)
    y=random.randint(1,height)
    pos=(x,y)
    return(pos)


#return rand position on empty place
def rand_item(board):
    while True:
        pos=rand_pos(board)
        if get_item(board, pos)==" ":
            return(pos)


#generate number of items on empty places - mice character = "M"
def gen_items(board, number):
    for num in range(number):
        set_item(board, rand_item(board), "M")
    return(board)


#generate random initial position of cat head - "H"
def gen_cat(board):
    pos_H= rand_item(board)
    return(pos_H)


#ask for user choice (W,S,A,D or w,s,a,d) and return new position of cat head
def cat_move(head_pos):
    x, y = head_pos
    choice=input("Your move:")
    if choice=="w" or choice=="W":
        new_head_pos=(x,y+1)
        return(new_head_pos)

    elif choice=="a" or choice=="A":
        new_head_pos = (x-1,y)
        return (new_head_pos)

    elif choice == "s" or choice == "S":
        new_head_pos = (x,y-1)
        return (new_head_pos)

    elif choice == "d" or choice == "D":
        new_head_pos = (x+1,y)
        return (new_head_pos)


#change the move according to cat move and  change list (cat) according to movement
#return True or False - whether cat hit the wall or eat itself
def mouse_move(cat, board):
    pos_H=cat[0]
    new_pos=cat_move(pos_H)                     #4 options in matrix ("M", " ", "o", edge)

    if get_item(board, new_pos)=="M":
        cat.insert(0, new_pos)

        set_item(board, new_pos, "H")
        for item in range(1, len(cat)):
            set_item(board, cat[item], "o")

    elif get_item(board, new_pos)==" ":
        if len(cat)==1:
            cat[0]=new_pos
            set_item(board, new_pos, "H")
            set_item(board, pos_H, " ")

        else:
            old_o=cat[-1]
            cat.insert(0, new_pos)
            cat.pop()

            set_item(board, new_pos, "H")
            set_item(board, old_o, " ")
            for item in range(1, len(cat)):
                set_item(board, cat[item], "o")

    elif get_item(board, new_pos) == "o":
        if new_pos==cat[-1] and len(cat)>2:
            cat.pop()
            cat.insert(0, new_pos)

            set_item(board, new_pos, "H")
            for item in range(1, len(cat)):
                set_item(board, cat[item], "o")

        else:
            print("You eaten yourself.")
            return(False)

    else:
        print("You hit a wall.")
        return(False)

#entire game
def game(width, height, number):
    cat=[]
    board=create_board(width, height)
    cat.append(gen_cat(board))
    set_item(board, cat[0], "H")
    gen_items(board, number)
    num=number

    while True:
        if (len(cat)-1)==num:           #refreshing mice
            num+=number
            gen_items(board, number)
        print_board(board)
        if mouse_move(cat, board)==False:
            print("END.")
            return

game(10,7, 7)

