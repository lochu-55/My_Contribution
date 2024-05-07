import json
import random
import string


class RandomPersonGenerator:
    def __init__(self, num_persons):
        self.num_persons = num_persons

    def generate_random_name(self):
        # Generate a random name consisting of a random first name and last name
        first_name = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10)))
        last_name = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10)))
        return f"{first_name.capitalize()} {last_name.capitalize()}"

    def generate_random_email(self, name):
        # Generate a random email address based on the name
        email_provider = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
        username = name.replace(" ", "").lower()
        provider = random.choice(email_provider)
        return f"{username}@{provider}"

    def generate_random_gender(self):
        # Generate a random gender
        genders = ['Male', 'Female']
        return random.choice(genders)

    def generate_random_status(self):
        # Generate a random status
        statuses = ['Active', 'Inactive']
        return random.choice(statuses)

    def generate_random_person(self):
        # Generate a random person object
        name = self.generate_random_name()
        email = self.generate_random_email(name)
        gender = self.generate_random_gender()
        status = self.generate_random_status()
        return {
            "name": name,
            "email": email,
            "gender": gender,
            "status": status,
            "id": None
        }

    def generate_and_save_persons(self, filename):
        # Generate random persons array
        random_persons = [self.generate_random_person() for _ in range(self.num_persons)]

        # Save generated persons to a JSON file
        with open(filename, 'w') as f:
            json.dump({"person": random_persons}, f, indent=4)


# Usage:
# Instantiate the RandomPersonGenerator class with the desired number of persons
num_persons = 5
person_generator = RandomPersonGenerator(num_persons)


filenames = ["data.json", "new_data.json"]
for filename in filenames:
    person_generator.generate_and_save_persons(filename)
    print(f"{num_persons} random persons generated and saved to '{filename}'.")