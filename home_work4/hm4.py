import random

def movement(move:str, line:int, column:int, maze:int):
    if move == "up" and line > 0:
        line -= 1
    elif move == "down" and line < maze:
        line += 1
    elif move == "right" and column < maze:
        column += 1
    elif move == "left" and column > 0:
        column -= 1
    else:
        pass
    return line, column

def fix_maze(maze_rooms, maze_size:int):
    key_positions = []
    maze_rooms[0][0] = "empty"
    for lines in range(maze_size):
        for columns in range(maze_size):
            if maze_rooms[lines][columns] == "key":
                key_positions.append((lines, columns))

    if len(key_positions) > 1:
        for i in range(1, len(key_positions)):
            line, col = key_positions[i]
            maze_rooms[line][col] = 'empty'

    if len(key_positions) == 0:
        maze_rooms[6][6] = "key"

    return maze_rooms


def room():
    var_room = ['box', 'enemy', 'empty', 'trap', 'portal', 'key']
    return random.choice(var_room)

def box():
    var_room = ['potion', 'sword', 'empty', 'tool']
    return random.choice(var_room)

def enemy(hp:int, inventory):
    if "sword" in inventory:
        return hp
    else:
        return hp - 10


def trap(hp:int, inventory):
    if "tool" in inventory:
        inventory = throwOutInv('tool', inventory)
        return hp, inventory
    else:
        return hp - 5, inventory

def portal(position, portal_positions):
    if len(portal_positions) > 1:
        portal_positions = portal_positions.copy()
        portal_positions.remove(position)
        new_pos = random.choice(portal_positions)
        return new_pos[0], new_pos[1]
    return position[0], position[1]


def pickUpInv(item:str, inventory):
    if len(inventory) < 5 and item != "empty":
        inventory.append(item)
    return inventory

def throwOutInv(item:str, inventory):
    inventory.remove(item)
    return inventory

def sortInv(inventory):
    inventory.sort()
    return inventory

def portals(maze_rooms, maze_size:int):
    portal_positions = []
    for lines in range(maze_size):
        for columns in range(maze_size):
            if maze_rooms[lines][columns] == "portal":
                portal_positions.append((lines, columns))
    return portal_positions

inventory = []
hp = int(100)
maze_size = int(7)
key = False
maze_rooms = [[room() for columns in range(maze_size)] for lines in range(maze_size)]
maze = [['#' for columns in range(maze_size)] for columns in range(maze_size)]

fix_maze(maze_rooms, maze_size)

line_now = int(0)
column_now = int(0)
exit = int(6)
while not(column_now == exit and line_now == exit and key) and hp > 0 :
    print( "right, left, up, down, use potion, remove 'item'")
    maze[line_now][column_now] = "*"
    print(hp)
    if key:
        print("key")
    print('inventory:', end = ' ')
    print( *inventory, sep ="")
    for lines in range(maze_size):
        for columns in range(maze_size):
            print(maze[lines][columns], end='')
        print()
    maze[line_now][column_now] = "_"
    type_room = maze_rooms[line_now][column_now]
    print( type_room)
    if type_room == "box":
        item = box()
        inventory = pickUpInv(item, inventory)
    elif type_room == "enemy":
        hp = enemy(hp, inventory)
    elif type_room == "empty":
        pass
    elif type_room == "trap":
        hp, inventory = trap(hp, inventory)
    elif type_room == "portal":
        portal_list = portals(maze_rooms, maze_size)
        maze_rooms[line_now][column_now] = "empty"
        line_now, column_now = portal((line_now, column_now), portal_list)
        maze_rooms[line_now][column_now] = "empty"
        continue
    elif type_room == "key":
        key = True
    move = str(input())
    maze_rooms[line_now][column_now] = "empty"
    if move == "use potion":
        inventory = throwOutInv("potion", inventory)
        hp+= 5
    elif move == "sort":
        inventory = sortInv(inventory)
    elif "remove" in move:
        func = move.split(" ")
        inventory = throwOutInv(func[-1], inventory)
    line_now, column_now = movement(move, line_now, column_now, exit)
if key:
    print('you win')
else:
    print("game over")

