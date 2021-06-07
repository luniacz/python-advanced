def read_input(filename):
    with open(filename, 'r') as read_file:
        initial_layer = [[[element for element in line.strip()] for line in read_file.readlines()]]
    return initial_layer


def create_empy_cube(x_size, y_size, z_size):
    cube = [[['.' for _ in range(x_size)] for _ in range(y_size)] for _ in range(z_size)]
    return cube


cycles = 6
initial_layer = read_input('input.txt')
xy_size = cycles * 2 + len(initial_layer[0])
z_size = cycles * 2 + 1

unit_vector = [-1, 0, 1]

new_cube = create_empy_cube(xy_size, xy_size, z_size)
copy_cube = create_empy_cube(xy_size, xy_size, z_size)

for y in range(len(initial_layer)):
    for x in range(len(initial_layer)):
        new_cube[cycles][cycles + y][cycles + x] = initial_layer[y][x]


