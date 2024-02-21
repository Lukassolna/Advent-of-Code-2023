import re
from range import Range

class NewRange:
    @staticmethod
    def read_sample_file():
        try:
            with open("ranges.txt", "r") as file:
                content = file.read()
            return content
        except Exception as e:
            return f"Error reading file: {str(e)}"

    @staticmethod
    def transform_ranges(input_range, example_string_index):
        content = NewRange.read_sample_file()
        if "Error reading file" in content:
            return input_range  

        strings = re.split(r'\r\n\r', content, flags=re.MULTILINE)
        try:
            example_string = strings[example_string_index]
        except IndexError:
            return input_range 

        lines = NewRange.extract_data(example_string)
        flattened_input_range = [item for sublist in input_range for item in sublist]

        test = []
        for line in lines:
            a, b, c = map(int, line.split())
            single_range = Range.range(b, b + c - 1)  

            intersections = Range.intersection(flattened_input_range, single_range)
            adjusted_intersections = [(from_val + a - b, to_val + a - b - 1) for from_val, to_val in intersections]

            test.extend(adjusted_intersections)

        if not test:
            return input_range
        else:
            test.sort(key=lambda x: x[0])  
            result = []
            for range_val in test:
                result = Range.union(result, [range_val])
            return result

    @staticmethod
    def extract_data(input_string):
        header, numbers_string = input_string.split("map:\r\n", 1)
        return numbers_string.split("\r\n")

    @staticmethod
    def initial(num):
        content = NewRange.read_sample_file()
        if "Error reading file" in content:
            return []  

        strings = re.split(r'\r\n\r', content, flags=re.MULTILINE)
        example_string = strings[0]
        seeds = map(int, example_string.split(": ")[1].split())

        ranges = [Range.range(start, start + steps - 1) for start, steps in zip(seeds[::2], seeds[1::2])]
        return ranges[num] if num < len(ranges) else []

    @staticmethod
    def main(num):
        initial_range = NewRange.initial(num)
  
        transformed_range = initial_range
        for transformation in [NewRange.seed_to_soil, NewRange.soil_to_fertilizer, NewRange.fertilizer_to_water,
                               NewRange.water_to_light, NewRange.light_to_temperature,
                               NewRange.temperature_to_humidity, NewRange.humidity_to_location]:
            transformed_range = transformation(transformed_range)
        return transformed_range

  
    def seed_to_soil(input_range):
        return NewRange.transform_ranges(input_range, 1)

    @staticmethod
    def soil_to_fertilizer(input_range):
        return NewRange.transform_ranges(input_range, 2)

    @staticmethod
    def fertilizer_to_water(input_range):
        return NewRange.transform_ranges(input_range, 3)

    @staticmethod
    def water_to_light(input_range):
        return NewRange.transform_ranges(input_range, 4)

    @staticmethod
    def light_to_temperature(input_range):
        return NewRange.transform_ranges(input_range, 5)

    @staticmethod
    def temperature_to_humidity(input_range):
        return NewRange.transform_ranges(input_range, 6)

    @staticmethod
    def humidity_to_location(input_range):
        return NewRange.transform_ranges(input_range, 7)

   
result = NewRange.main(0)
print(result)