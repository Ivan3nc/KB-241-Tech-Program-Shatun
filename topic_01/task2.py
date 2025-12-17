def print_str_methods(text):
    print("strip():", text.strip())
    print("capitalize():", text.capitalize())
    print("title():", text.title())
    print("upper():", text.upper())
    print("lower():", text.lower())

s = input("Введіть рядок: ")
print_str_methods(s)
