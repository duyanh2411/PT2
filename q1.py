def replace_chars(input_string, char_to_replace, replacement_char):
    modified_string = ''
    for char in input_string:
        if char == char_to_replace:
            modified_string += replacement_char
        else:
            modified_string += char
    return modified_string

def main():
    input_string = input("Enter a string (no spaces): ")
    char_to_replace = input("Enter the character to replace: ")
    replacement_char = input("Enter the replacement character: ")
    if len(char_to_replace) != 1 or len(replacement_char) != 1:
        print("Please enter single characters.")
        return
    result = replace_chars(input_string, char_to_replace, replacement_char)
    print("Result:", result)

if __name__ == "__main__":
    main()
