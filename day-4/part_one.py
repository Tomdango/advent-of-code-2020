class Passport:
    VALID_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    def __init__(self, fields):
        self.fields = self._build_fields(fields)

    def _build_fields(self, fields):
        sanitised_fields = {}

        for entry in fields:
            field, value = entry.split(":")

            if field in self.VALID_FIELDS:
                sanitised_fields[field] = value

        return sanitised_fields

    def is_valid(self):
        present_keys = self.fields.keys()
        field_count = len(present_keys)

        if field_count == 8:
            return True
        elif field_count == 7 and "cid" not in present_keys:
            return True
        else:
            return False

def get_passports():
    fields = []
    for line in open("input.txt", "r"):
        # If the line is empty, we've hit the end of one passport
        if line == "\n":
            yield Passport(fields)
            fields = []
            continue

        fields.extend(line.strip().split(" "))

    yield Passport(fields)


if __name__ == "__main__":
    valid_passports = [passport for passport in get_passports() if passport.is_valid()]

    print(f"Valid Passports: {len(valid_passports)}")
