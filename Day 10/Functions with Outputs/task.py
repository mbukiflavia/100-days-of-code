def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}" #this output replaces the part where the function was called

formatted_string = format_name("flAviA", "ANGELA")
print(formatted_string)