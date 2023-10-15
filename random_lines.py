import random

num_lines = 2500000
output_file = "random_numbers.txt"
unique_numbers = set()

with open(output_file, "w") as file:
    while len(unique_numbers) < num_lines:
        random_number = random.randint(1, 2500000) 
        if random_number not in unique_numbers:
            unique_numbers.add(random_number)
            file.write(str(random_number) + "\n")

print(f"Generated {len(unique_numbers)} unique random numbers in {output_file}")

