import os
import logging


def read_input(filename):
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
    with open(input_path, 'r') as read_file:
        matrix = [[element for element in line.strip()] for line in read_file.readlines()]
    return matrix


def count_trees(input_matrix):
    column_index = 0
    line_index = 0
    move_line_index = 1
    move_column_index = 3
    counter = 0

    for _ in range(len(input_matrix)):
        if input_matrix[line_index][column_index] == '#':
            counter += 1
        if column_index + move_column_index >= len(input_matrix[0]):
            column_index = 3 - (len(input_matrix[0]) - column_index)
        else:
            column_index += move_column_index
        line_index += move_line_index

    return counter


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG, datefmt='%H:%M:%S')
matrix_input = read_input('input.txt')
number_of_tries = count_trees(matrix_input)
logging.info(f'Total number of trees : {number_of_tries}')
