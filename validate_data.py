def validate_data(data):
    invalid_entries = []

    for entry in data:
        if not isinstance(entry.get("age"), int):
            invalid_entries.append(entry)

    return invalid_entries

if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": "25"},
        {"name": "Charlie", "age": None},
        {"name": "David"}
    ]

    print(validate_data(data))
