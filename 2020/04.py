import pathlib
import re

# define data-file
ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / '2020' / 'input'


def parse(file):
    input_data = [line.strip() for line in open(file, 'r').readlines()]

    passports = []
    passport = dict()
    for line in input_data:
        line = line.rstrip()
        if not line:
            if passport:
                passports.append(passport)
            passport = dict() # create new passport on blank row
        else:
            fields = [d for d in line.split()]
            for info in fields:
                k, v = info.split(':')
                passport[k] = v

    passports.append(passport)

    return passports

def validate_int(value, min, max):
    if not value.isdigit():
        return False
    return min <= int(value) <= max

def validate_passport(passport):
    """
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    """
    keys = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        #'cid',
    ]
    # return all(elem in keys for elem in passport.keys())
    return all(elem in passport.keys() for elem in keys)

def validate_passport_strict(passport):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """

    # first check if all keys exists - if not just skip
    if not validate_passport(passport):
        return False
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not validate_int(passport['byr'], min=1920, max = 2002):
        return False
    if not validate_int(passport['iyr'], min=2010, max = 2020):
        return False
    if not validate_int(passport['eyr'], min=2020, max = 2030):
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not passport['pid'].isdigit() or not len(passport['pid']) == 9:
        return False
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    hgt = passport['hgt']
    h = hgt[:len(hgt) - 2]
    m = hgt[len(hgt) - 2:]

    if m not in ['cm', 'in']:
        return False
    if m == 'cm' and not validate_int(h, min=150, max=193):
        return False
    if m == 'in' and not validate_int(h, min=59, max=76):
        return False


    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport['hcl']):
        return False
    # ecl (Eye Color) - exactly one of:
    if not any(elem in [passport['ecl']] for elem in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False

    return True

def solve_a(passports):
    print('no_of_passports', len(passports))
    return sum([validate_passport(passport) for passport in passports])


def solve_b(passports):
    return sum([validate_passport_strict(passport) for passport in passports])


def main():

    # data = parse(INPUT_DIR / 'test.txt')
    data = parse(INPUT_DIR / '04.txt')

    print(f'Answer A: {solve_a(data)}')

    print(f'Answer B: {solve_b(data)}')


if __name__ == '__main__':
    main()
