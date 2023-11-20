# Print a downward Half-Pyramid Pattern of Star (asterisk)

def print_downward_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()
rows = 5
print_downward_half_pyramid(rows)