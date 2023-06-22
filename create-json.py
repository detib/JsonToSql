import json
import random
import string


# random json data creator to test JsonToSql
def generate_random_json():
    data = {}

    # Generate random table names
    table_names = ['users', 'products', 'orders']

    # Generate random single object
    single_object = {}
    for _ in range(random.randint(2, 5)):
        key = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
        value = random.choice([random.randint(1, 100), random.uniform(1, 100), ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))])
        single_object[key] = value
    data[random.choice(table_names)] = single_object

    # Generate random array of objects
    array_objects = []
    for _ in range(random.randint(2, 5)):
        obj = {}
        for _ in range(random.randint(2, 5)):
            key = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
            value = random.choice([random.randint(1, 100), random.uniform(1, 100), ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))])
            obj[key] = value
        array_objects.append(obj)
    data[random.choice(table_names)] = array_objects

    return data

def write_json_to_file(file_path, json_str):
    with open(file_path, 'w') as sql_file:
        sql_file.write(json_str)

def main():
    data = generate_random_json()
    json_str = json.dumps(data, indent=4)
    write_json_to_file("data.json", json_str)
    print(json_str)


if __name__ == '__main__':
    main()
