
def test(str):
    str_lst = str.split()
    for count, item in enumerate(str_lst):
        if item[0] == "{" or item [0] == "(":
            yield item + " " + str_lst[count + 1]
        elif item[-1] != "}" and item [-1] != ")":
            yield item

str = "HELP NOI DUNG {{NOI DUNG}} ((NOI DUNG))"

result = test(str)

print([*result])