def draw_hexagon():
    print("  __  ", end='')

def draw_hexagon_top():
    print(" /  \\ ", end='')

def draw_hexagon_bottom():
    print("\\    /", end='')

def draw_hexagon_end():
    print(" \\__/ ", end='')

def draw_hexagon_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            draw_hexagon()
        print()
        for j in range(columns):
            draw_hexagon_top()
        print()
        for j in range(columns):
            draw_hexagon_bottom()
        print()
        for j in range(columns):
            draw_hexagon_end()
        print()
    print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
draw_hexagon_pattern(rows, columns)