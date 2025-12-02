from dataclasses import dataclass
from time import time

@dataclass
class Ranges:
    first: int
    middle: int
    last: int

# https://sqlpey.com/python/solved-how-to-identify-repeating-patterns-in-a-string-using-python/#method-6-string-comparison-optimization
def repeats(string):
    n = len(string)
    tried = set()
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            candidate = string[:i]
            if candidate in tried:
                continue
            tried.add(candidate)
            if candidate * (n // i) == string:
                return candidate
    return None



def main() -> None:

    user_input = "10327-17387,74025-113072,79725385-79874177,964628-1052240,148-297,3-16,126979-227778,1601-2998,784-1207,831289-917268,55603410-55624466,317-692,602197-750430,17-32,38-58,362012-455626,3622441-3647505,883848601-883920224,62-105,766880-804855,9184965756-9185005415,490073-570277,2929273115-2929318135,23251-48475,9696863768-9697013088,229453-357173,29283366-29304416,4526-8370,3095-4389,4400617-4493438"

    parsed_input = user_input.split(',')
    if debug: print("input: %s" % (parsed_input,))

    ranges: list[Ranges] = []
    for x in parsed_input:
        range_input = x.split('-')
        first = int(range_input[0])
        last = int(range_input[1])

        middle = ((first + last) / 2)
        if middle % 2 != 0:
            middle = int(middle + 0.5)
        middle = int(middle - 1)

        ranges.append(Ranges(first, middle, last))

    total: int = 0
    invalid_ids: list = []
    for x in ranges:
        y_range: list = []
        z_range: list = []

        for y in range(x.middle + 1, x.last + 1):
            y_range.append(int(y))

        for z in range(x.first, x.middle + 1):
            z_range.append(int(z))

        # Only containing uneven
        if not y_range and not z_range:
            continue

        complete_even: list = z_range + y_range
        if debug: print("Complete range: %s" % (complete_even,))
        for entry in complete_even:
            if debug: print("Entry: %s" % (entry,))

            candidate = repeats(str(entry))
            if candidate:
                if debug: print("Invalid ID: %s" % (candidate,))
                invalid_ids.append(entry)

    if debug: print("Invalid IDs: %s" % (invalid_ids,))

    for entry in invalid_ids:
        total = total + entry

    print("Sum of invalid IDs: %s" % (total,))


if __name__ == "__main__":
    debug = False
    start = time()
    main()
    end = time()

    print("Total time: %.10f seconds" % (end - start))
