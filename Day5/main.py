import os

class Optranges:
    @staticmethod
    def read_sample_file():
        try:
            with open("ranges.txt", "r") as file:
                return file.read()
        except Exception as e:
            return f"Error reading file: {e}"

    @staticmethod
    def check_seed(d, a, b, c):
        if b <= d <= b + c:
            return d + (a - b)
        else:
            return d

    @staticmethod
    def transform_seed(lines, initial_seed):
        final_seed = initial_seed
        for line in lines:
            if line:
                a, b, c = map(int, line.split())
                new_seed = Optranges.check_seed(final_seed, a, b, c)
                if new_seed != final_seed:
                    final_seed = new_seed
                    break
        return final_seed

    @staticmethod
    def generic_seed_to_transform(seed, step):
        content = Optranges.read_sample_file()
        strings = content.split("\r\n\r")
        example_string = strings[step].strip()
        lines = Optranges.extract_data(example_string)
        return Optranges.transform_seed(lines, seed)

    @staticmethod
    def extract_data(input_string):
        _header, numbers_string = input_string.split("map:\r\n", 1)
        return numbers_string.split("\r\n")

    @staticmethod
    def lookup(number, map_dict):
        return map_dict.get(number, number)

    @classmethod
    def main(cls):
        content = cls.read_sample_file()
        strings = content.split("\r\n\r", 1)
        seeds_string = strings[0].split(": ", 1)[1]
        seeds = list(map(int, seeds_string.split()))

        transformations = [
            cls.seed_to_soil,
            cls.soil_to_fertilizer,
            cls.fertilizer_to_water,
            cls.water_to_light,
            cls.light_to_temperature,
            cls.temperature_to_humidity,
            cls.humidity_to_location,
        ]

        for transform in transformations:
            seeds = list(map(transform, seeds))

        final_output = min(seeds)
        return final_output

    @classmethod
    def seed_to_soil(cls, seed):
        return cls.generic_seed_to_transform(seed, 1)

    @classmethod
    def soil_to_fertilizer(cls, seed):
        return cls.generic_seed_to_transform(seed, 2)

    @classmethod
    def fertilizer_to_water(cls, seed):
        return cls.generic_seed_to_transform(seed, 3)

    @classmethod
    def water_to_light(cls, seed):
        return cls.generic_seed_to_transform(seed, 4)

    @classmethod
    def light_to_temperature(cls, seed):
        return cls.generic_seed_to_transform(seed, 5)

    @classmethod
    def temperature_to_humidity(cls, seed):
        return cls.generic_seed_to_transform(seed, 6)

    @classmethod
    def humidity_to_location(cls, seed):
        return cls.generic_seed_to_transform(seed, 7)

# Example of how to run the main function
if __name__ == "__main__":
    final_output = Optranges.main()
    print(final_output)
