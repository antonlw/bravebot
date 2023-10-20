
def write_to_file(filename, text):
    try:
        with open(filename, 'w') as file:
            file.write(text)
            print("Text successfully written to the file!")
    except FileNotFoundError:
        print("File not found. Please check the file path.")


def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
