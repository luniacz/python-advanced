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
                key, password_value = record.split(':')
                passport[key] = password_value
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
    min_year = 1920
    max_year = 2002
    return bool(min_year <= int(year) <= max_year and year.isnumeric())


def iyr(year):
    min_year = 2010
    max_year = 2020
    return bool(min_year <= int(year) <= max_year and year.isnumeric())


def eyr(year):
    min_year = 2020
    max_year = 2030
    return bool(min_year <= int(year) <= max_year and year.isnumeric())


def hgt(height):
    unit = height[-2:]
    try:
        int_height = int(height[:-2])
    except ValueError:
        return False

    if unit == 'in':
        min_height = 59
        max_height = 76
    elif unit == 'cm':
        min_height = 150
        max_height = 193
    else:
        min_height = 0
        max_height = 0

    return bool(min_height <= int_height <= max_height)


def hcl(color):
    return bool(re.search('[#][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', color))


def ecl(color):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return bool(color in valid_colors)


def pid(input_number):
    return bool(re.search('^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', input_number))


def check_passports(passports, input_locals):
    output_passwords = []
    number_of_valids = 0
    for passport in passports:
        status = True
        number_fields = len(passport.keys())
        for key in passport.keys():

            if key == 'cid':
                number_fields -= 1
            else:
                status &= input_locals[key](passport[key])

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
print(number_of_valid)
