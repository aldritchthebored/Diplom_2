from faker import Faker


class Helpers:
    @staticmethod
    def create_data():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.name()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

    @staticmethod
    def generate_random_email():
        fake = Faker()
        email = fake.email()
        return email

    @staticmethod
    def generate_random_password():
        fake = Faker()
        password = fake.password()
        return password

    @staticmethod
    def generate_random_name():
        fake = Faker()
        name = fake.name()
        return name
