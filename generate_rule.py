import sys

def generate_rule(api_list):
    rules = []
    for api in api_list:
        parts = api.split(',')
        uri = parts[0]
        method = parts[1] if len(parts) > 1 else None
        rule = f'(http.request.full_uri matches "{uri}"'
        if method:
            rule += f' and http.request.method eq "{method}"'
        rule += ')'
        rules.append(rule)
    return ' or '.join(rules)

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            api_list = [line.strip() for line in file.readlines()]
        rule = generate_rule(api_list)
        print(rule)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_rule.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
