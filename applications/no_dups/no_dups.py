def no_dups(s):
    s_arr = s.split()
    found = {}
    output = ""
    for i in range(len(s_arr)):
        if s_arr[i] not in found:
            found[s_arr[i]] = True
            output += s_arr[i] + " "
    return output[:-1]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))