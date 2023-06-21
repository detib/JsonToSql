import json


def create_insert_statements(data):
    insert_statements = []

    for table_name, records in data.items():
        if isinstance(records, dict):  # Single object
            keys = []
            values = []

            for key, value in records.items():
                keys.append(key)
                if isinstance(value, str):
                    values.append(f"'{value}'")
                else:
                    values.append(str(value))

            insert_statement = f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({', '.join(values)});"
            insert_statements.append(insert_statement)
        elif isinstance(records, list):  # Array of objects
            for record in records:

                keys = []
                values = []

                for key, value in record.items():
                    if isinstance(value, dict):
                        continue  # Skip nested objects
                    keys.append(key)
                    if isinstance(value, str):
                        values.append(f"'{value}'")
                    else:
                        values.append(str(value))

                insert_statement = f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({', '.join(values)});"
                insert_statements.append(insert_statement)

    return insert_statements


def write_insert_statements_to_file(file_path, insert_statements):
    with open(file_path, 'w') as sql_file:
        for statement in insert_statements:
            sql_file.write(statement + '\n')


def main():
    file_path = 'data.json'  # Replace with the path to your JSON file
    output_file_path = 'output.sql'  # Replace with the desired output file path

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    insert_statements = create_insert_statements(data)

    write_insert_statements_to_file(output_file_path, insert_statements)

    print(f"Insert statements written to {output_file_path}")


if __name__ == '__main__':
    main()
