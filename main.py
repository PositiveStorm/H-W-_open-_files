import os

file_path = os.getcwd()
name_list = os.listdir(file_path)

new_dict = {}
for file in name_list:
    if file.endswith('.txt'):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.readlines()
            length = len(data)
            length = int(length)
            data.insert(0, length)
            new_dict[file] = data
sorted_values = sorted(new_dict.values(), key=len)
new_dict_sorted = {}
for i in sorted_values:
    for key in new_dict.keys():
        if new_dict[key] == i:
            new_dict_sorted[key] = new_dict[key]
            break


new_list = []

for keys, values in new_dict_sorted.items():
    new_list.append(str(keys) + "\n")
    print(keys)
    for el in values:
        print(el)
        new_list.append(str(el) + "\n")
with open('sortedtext.txt', 'w', encoding='utf-8') as new_file:
    for data in new_list:
        data = str(data)
        new_file.write(data)
