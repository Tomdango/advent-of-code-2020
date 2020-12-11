# Advent of Code 2020
# Day Four - Part Two
# Thomas Judd-Cooper

from part_one import Passport
from string import hexdigits
import re

class PassportWithValidation(Passport):
    VALID_EYE_COLOURS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def is_valid(self):
        if super().is_valid() == False:
            return False

        if not self._validate_year("byr", 1920, 2002):
            return False

        if not self._validate_year("iyr", 2010, 2020):
            return False

        if not self._validate_year("eyr", 2020, 2030):
            return False

        if not self._validate_height():
            return False

        if not self._validate_hair_colour():
            return False

        if not self._validate_eye_colour():
            return False

        if not self._validate_pid():
            return False

        return True

    def _validate_year(self, key, lower_bound, upper_bound):
        year = self.fields.get(key, None)
        if key is None:
            return False

        if len(year) != 4:
            return False

        year = int(year)

        if year < lower_bound or year > upper_bound:
            return False

        return True

    def _validate_height(self):
        height = self.fields.get("hgt")
        units = height[-2:]
        value = height[:-2]

        if units not in ["cm", "in"]:
            return False

        try:
            value = int(value)
        except ValueError:
            return False

        if units == "cm" and value >= 150 and value <= 193:
            return True
        elif units == "in" and value >= 59 and value <= 76:
            return True
        return False

    def _validate_hair_colour(self):
        colour = self.fields.get("hcl")
        if colour[0] != "#":
            return False

        if len(colour) != 7:
            return False

        last_six_chars = colour[-6:]
        return not re.match(r"/[0-9a-f]+/", last_six_chars)

    def _validate_eye_colour(self):
        eye_colour = self.fields.get("ecl")
        return eye_colour in self.VALID_EYE_COLOURS


    def _validate_pid(self):
        pid = self.fields.get("pid")

        if len(pid) != 9:
            return False

        return re.match(r"^([\s\d]+)$", pid) is not None


def get_passports():
    fields = []
    for line in open("input.txt", "r"):
        # If the line is empty, we've hit the end of one passport
        if line == "\n":
            yield PassportWithValidation(fields)
            fields = []
            continue

        fields.extend(line.strip().split(" "))

    yield Passport(fields)

if __name__ == "__main__":
    valid_passports = [passport for passport in get_passports() if passport.is_valid()]
    print(f"Valid Passport Count: {len(valid_passports)}")
