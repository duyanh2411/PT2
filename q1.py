s = input("Enter a string (no spaces): ")
char_to_replace = input("Enter the character to replace: ")
replacement_char = input("Enter the replacement character: ")

if len(char_to_replace) != 1 or len(replacement_char) != 1:
        print("Please enter single characters.")

result = s.replace((char_to_replace), (replacement_char))
print("Result:", result)
