my_dict = [5, 'some_text', 42.5, None, False, True]
print(list(my_dict))
for val in my_dict:
    data_type = type(val)
    print(f"{val} - тип данных: {data_type}")
