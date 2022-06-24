a = input("Type something: ").strip()
char_list = list(a)
x = 0
y = -1

while x < len(a)//2 and y < len(a)//2:
    char_list[x], char_list[y] = char_list[y], char_list[x]
    x += 1
    y -= 1
        

output = "".join(char_list)
print(output)
