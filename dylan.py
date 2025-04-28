import os

def dim_square(length, space_away):
    if length <= 1 or space_away < 1:
        raise Exception("length is too small")
    angle = length // 2 + 1 #amount of \ per side in for loop
    total_empty = space_away + 2 * length + length // 2 + 1 + space_away
    for space in range(space_away):
        print(total_empty * " ")
    print(space_away * " " + 2 * length * "_" + (length // 2 + 1) * " " + space_away * " ")
    for sides in range(0, length // 2):
        print((space_away -1) * " " + "|" + sides * " " + "\\" + 2* length * " " + "\\" + sides * " " + space_away * " ")
    print((space_away - 1) * " " + "|" + (sides + 1) * " " + "\\" + 2 * length * "_" + "\\" + space_away * " " )
    for height in range(0, length // 2):
        print((space_away -1) * " " + "|" + (sides + 1) * " " + "|" + 2 * length * " " + "|" + space_away * " ")
    extra = 0 
    for underside in reversed(range(0, length // 2)):
        print((space_away + extra -1) * " " + "\\" + (underside + 1) * " " + "|" + 2 * length * " " + "|" + space_away * " ")
        extra += 1
    extra -= 1
    print((space_away + extra) * " " + "\\" + "|" + length * 2 * "_" + "|" + space_away * " ")
    for out in range(-1, space_away):
        print(total_empty * " ")
        
        
if __name__ == '__main__':  
    dim_square(30,2)
    print(os.get_terminal_size())