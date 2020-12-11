from typing import Dict
import re

REQUIRED_FIELDS = {'byr': lambda x: 1920 <= int(x) <= 2002,
                    'iyr': lambda x: 2010 <= int(x) <= 2020,
                    'eyr': lambda x: 2020 <= int(x) <= 2030,
                    'hgt': lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
                    'hcl': lambda x: re.fullmatch(r"#[0-9a-f]{6}", x),
                    'ecl': lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
                    'pid': lambda x: re.fullmatch(r"[0-9]{9}", x)}
OPTIONAL_FIELDS = ['cid']


def verify_passport(passport: Dict[str, str]) -> bool:
    for field, validator in REQUIRED_FIELDS.items():
        if field not in passport:
            return False
        else:
            try:
                if not validator(passport[field]):
                    return False
            except:
                return False
    return True

if __name__ == "__main__":
    passports = []
    failed_passports = 0
    valid_passports = 0
    with open("four_input.txt") as f:
        passports = f.read().split('\n\n')

    for passport in passports:
        pairs = passport.split()
        passport_dict = {x.split(':')[0]: x.split(':')[1] for x in pairs}
        if verify_passport(passport_dict):
            valid_passports += 1
        else:
            failed_passports += 1

    print(valid_passports)
    print(failed_passports)
