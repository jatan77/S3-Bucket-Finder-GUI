file_name = "g.txt"
string_to_add1 = "fbcdn-"

file_name1 = "list.txt"
with open(file_name, 'r') as f:
    file_lines = [''.join([string_to_add1,x.strip(), '\n']) for x in f.readlines()]

with open(file_name1, 'w') as f:
    f.writelines(file_lines) 
