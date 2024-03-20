import re

def parse_input(input_string):
        rows = input_string.strip().split("\n")
        processed_rows = [process_row(row) for row in rows]
        flattened_rows = [item for sublist in processed_rows for item in sublist]
        return sum(flattened_rows)


def process_row(row):
        left, right = row.split(" ")
        counts = parse_damaged_counts(right)
        if '?' in left:
            return (process_row(left.replace('?', '#', 1) + " " + right) +
                    process_row(left.replace('?', '.', 1) + " " + right))
        else:
            return [validate(f"{left} {','.join(map(str, counts))}")]
def validate(row):
        status_desc, damaged_counts = row.split(" ")
        counts = parse_damaged_counts(damaged_counts)
        count_string = [len(part) for part in status_desc.split('.')]
        count_string_without_0 = [c for c in count_string if c != 0]
        return 1 if count_string_without_0 == counts else 0


def parse_damaged_counts(counts):
        return [int(x) for x in re.sub(r"\r", "", counts).split(",")]

def test():
    try:
        with open("Day12/springs.txt", "r") as file:
            input_string = file.read()
        result = parse_input(input_string)
        print(result)
    except FileNotFoundError:
        print("File not found.")

# Example usage
test()
