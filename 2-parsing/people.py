import re


def read_input(filename: str) -> list:
    # with open(filename, 'r') as read_file:
    #     full_file = read_file.read()
    #
    # output_people = []
    # dict_person = {}
    # input_people = full_file.split('\n\n')
    # for person in input_people:
    #     person = person.replace('\n', ' ')
    #     split_person = person.strip().split(' ')
    #     for part_of_person in split_person:
    #         dict_person[part_of_person[:3]] = part_of_person[5:]
    #     output_people.append(dict_person)
    #     dict_person = {}
    # return output_people

    with open(filename, 'r') as my_file:
        lines = my_file.readlines()

    passports, passport, records = [], {}, []
    for line in lines:

        if line.strip():
            records.extend(line.split())
        else:
            for record in records:
                key, value = record.split(':')
                passport[key] = value
            passports.append(passport)
            passport, records = {}, []

    return passports


def verify_passports(input_passports):
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    counter = 0
    output_passport_status = []
    for passport in input_passports:
        valid_counter = 0
        for field in valid_fields:
            try:
                if passport[field]:
                    valid_counter += 1
            except KeyError:
                output_passport_status.append('NOT VALID')
                break

        if valid_counter == 7:
            output_passport_status.append('VALID')
            counter += 1

    return output_passport_status, counter


def byr(year):
    if 1920 <= int(year) <= 2002 and year.isnumeric():
        return True
    else:
        return False


def iyr(year):
    if 2010 <= int(year) <= 2020 and year.isnumeric():
        return True
    else:
        return False


def eyr(year):
    if 2020 <= int(year) <= 2030 and year.isnumeric():
        return True
    else:
        return False


def hgt(height):
    if height[-2:] == 'in' and 59 <= int(height[:-2]) <= 76:
        return True
    elif height[-2:] == 'cm' and 150 <= int(height[:-2]) <= 193:
        return True
    else:
        return False


def hcl(color):
    if re.search(r'[#][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', color):
        return True
    else:
        return False


def ecl(color):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if color in valid_colors:
        return True
    else:
        return False


def pid(input_number):
    if re.search(r'^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', input_number):
        return True
    else:
        return False


def check_passports(passports, locals):
    output_passwords = []
    number_of_valids = 0
    for passport in passports:
        status = True
        number_fields = len(passport.keys())
        for key in passport.keys():

            if key != 'cid':
                status &= locals[key](passport[key])
            else:
                number_fields -= 1

        if status and number_fields == 7:
            output_passwords.append('VALID')
            number_of_valids += 1
        else:
            output_passwords.append('NOT VALID')
    return output_passwords, number_of_valids


passports = read_input('input.txt')
verified_passports, number = verify_passports(passports)
print(number)

passport_statuses, number_of_valid = check_passports(passports, locals())
pass
