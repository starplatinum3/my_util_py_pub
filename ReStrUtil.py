
import regex
# from tqdm import main
# import re


def tail_delete_brackets(string):
    """
    删除最后面的括号 ()
    """
    pattern = r"(\((?:[^()]++|(?1))*\))(?=[^()]*$)"
    return regex.sub(pattern, "", string)



# main
if __name__ == "__main__":
    strings = [
    "hell(h)o(world)",
    "hel(lo(wor)ld)",
    "hell(h)o(world)blahblahblah"
    ]
    # pattern = r"(\((?:[^()]++|(?1))*\))(?=[^()]*$)"
    for s in strings:
        # print(regex.sub(pattern, "", s))
        # print(re.sub(pattern, "", s))
        print(tail_delete_brackets(s))