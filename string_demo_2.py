import sys

def main():
    line = "-"*65
    print(line)

    print("Find")
    s = "aaBBaaBBBaaBBB"
    print("s.find('aa'):", s.find('aa'))

    n = s.find("BCD")
    print("n:",n)
    print(line)

    #strip,rstrip, lstrip
    s = "\n\n\tHello\n\n"
    s1 = s.strip()
    print("s1:", s1)

    s2 = s.rstrip()
    print("s2:", s2)

    s3 = s.lstrip()
    print("s3:", s3)
    print(line)
    #split, rsplit, splitlines, join
    s = "yogeshwar:x:1001:1001:Yogeshwar Shukla,,,:/home/yogeshwar:/bin/bash"
    L = s.split(":")
    print("split:L:", L)

    L1 = s.split(":", maxsplit = 3)
    print("split with maxsplit:L1:", L1)

    L = s.rsplit(":", maxsplit = 3)
    print("rsplit:L:", L)

    print(line)
    s = "Hello\nPython\nWorld"
    L = s.splitlines()
    print("s.splitlines():",L)
    print(s)
    print(line)

    delim = "##"
    s_joined = delim.join(L)
    print("s_joined:", s_joined)
    print(line)

    #partition, rpartition
    s = "Processor - Corei7 695x - this"
    T = s.partition("-")
    print("First:", T[0])
    print("Sep:", T[1])
    print("second:", T[2])
    print(line)
    T = s.rpartition("-")
    print("second:", T[0])
    print("sep:", T[1])
    print("First:", T[2])
    print(line)

    #format, format_map
    
main()
