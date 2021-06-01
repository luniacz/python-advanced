
def set_value_by_mask(mask, input_value):
    input_value = int(input_value)
    input_value = f'{input_value:036b}'
    output_value = ''

    for iterator in range(len(mask)):
        if mask[iterator] == '1':
            output_value += '1'
        elif mask[iterator] == '0':
            output_value += '0'
        else:
            output_value += input_value[iterator]
    return int(output_value, 2)


with open('input.txt', 'r') as read_file:
    lines = read_file.readlines()
lines = [line.strip() for line in lines]

init_reg = []
reg = {}
# create list of dictionaries
for line in lines:
    if line.find('mask = ') > -1:
        init_reg.append(reg)
        reg = {}
        reg['mask'] = line.split('mask = ')[1]
    elif line.find('mem') > -1:
        temp = line.split(' = ')
        reg[temp[0]] = temp[1]
init_reg.append(reg)

sum = 0
counted = {}

for reg in init_reg:
    for key in reg.keys():
        if key != 'mask':
            value_to_add = set_value_by_mask(reg['mask'], reg[key])
            counted[key] = value_to_add

for value in counted.values():
    sum += value

print(sum)



