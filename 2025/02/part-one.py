from dataclasses import dataclass
from time import time

@dataclass
class Ranges:
    first: int
    middle: int
    last: int

def main() -> None:

    user_input = """
    10327-17387,74025-113072,79725385-79874177,964628-1052240,148-297,3-16,126979-227778,1601-2998,784-1207,831289-917268,
    55603410-55624466,317-692,602197-750430,17-32,38-58,362012-455626,3622441-3647505,883848601-883920224,62-105,766880-804855,
    9184965756-9185005415,490073-570277,2929273115-2929318135,23251-48475,9696863768-9697013088,229453-357173,29283366-29304416,
    4526-8370,3095-4389,4400617-4493438
    """

    parsed_input = user_input.split(',')

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
            y_length = len(str(y))
            # Uneven will never contain a full sequence
            if y_length % 2 != 0:
                continue
            y_range.append(int(y))

        for z in range(x.first, x.middle + 1):
            z_length = len(str(z))
            # Uneven will never contain a full sequence
            if z_length % 2 != 0:
                continue
            z_range.append(int(z))

        # Only containing uneven
        if not y_range and not z_range:
            continue

        complete: list = z_range + y_range
        for entry in complete:
            if debug: print("Entry: %s" % (entry,))
            k = str(entry)
            middle = (len(k) - 1)//2 + 1
            left = k[:middle]
            right = k[middle:]
            if debug: print("left: %s, middle: %s, right: %s" % (left, middle, right))

            if left == right:
                invalid_ids.append(entry)

        if debug: print("Complete range: %s" % (complete,))

    if debug: print("Invalid IDs: %s" % (invalid_ids,))

    for entry in invalid_ids:
        total = total + entry

    print("Sum of invalid IDs: %s" % (total,))


if __name__ == "__main__":
    debug = False
    start = time()
    main()
    end = time()

    print("Total time: %10f seconds" % (end - start)) # ~0.45s
