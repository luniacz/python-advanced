def execute_command(command, acc, index):
    if command[0] == 'nop':
        return acc, index + 1
    elif command[0] == 'jmp':
        return acc, index + command[1]
    elif command[0] == 'acc':
        return acc + command[1], index + 1


with open('input.txt', 'r') as read_file:
    lines = read_file.readlines()
lines = [line.strip() for line in lines]
commands = [[line[:3], int(line[4:])] for line in lines]

acc = 0
command_index = 0
command = commands[command_index]
executed_commands = []

while command_index not in executed_commands:
    executed_commands.append(command_index)
    acc, command_index = execute_command(command, acc, command_index)
    command = commands[command_index]

print(acc)
