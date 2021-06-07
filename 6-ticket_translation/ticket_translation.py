with open('input.txt', 'r') as read_file:
    lines = read_file.readlines()
lines = [line.strip() for line in lines]

limits = []
for line in lines:
    if ' or ' in line:
        limit = {}
        info, rest = line.split(': ')
        limit1, limit2 = rest.split(' or ')
        limit1_min, limit1_max = limit1.split('-')
        limit2_min, limit2_max = limit2.split('-')
        limit[info] = [int(limit1_min), int(limit1_max), int(limit2_min), int(limit2_max)]
        limits.append(limit)
del limit, info, rest, limit1_max, limit1_min, limit2_min, limit2_max, limit1, limit2, line, lines

with open('input.txt', 'r') as read_file:
    data = read_file.read()
temp, your_ticket_data, nearby_ticket_data = data.split('\n\n')
del temp, data

your_ticket_data = your_ticket_data.split('\n')[1]
your_ticket_temp, your_ticket = [], []
your_ticket_temp = your_ticket_data.split(',')
for data in your_ticket_temp:
    your_ticket.append(int(data))
del your_ticket_temp, your_ticket_data, data

nearby_tickets = []

temp = []
temp = nearby_ticket_data.split('\n')
del temp[0]
for line in temp:
    line = line.split(',')
    ticket = []
    for data in line:
        ticket.append(int(data))
    nearby_tickets.append(ticket)
del data, line, nearby_ticket_data, temp, ticket

sum = 0
for ticket in nearby_tickets:
    for ticket_value in ticket:
        break_bool = False
        for limit in limits:
            value = [value for value in limit.values()][0]
            if ticket_value in range(value[0], value[1]) or ticket_value in range(value[2], value[3]):
                break_bool = True
                break
        if not break_bool:
            sum += ticket_value

pass




