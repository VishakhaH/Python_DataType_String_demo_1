import sys

def main():

    #ways of creation:
    #singly quoted string
    s1 = 'singly quoted string can contain " as a data'
    print("s1:", s1, "type(s1):", type(s1))

    #Double quoted string
    s2 = "This is doubly quoted string can contain ' as a data"
    print("s2:", s2, "type(s2):", type(s2))

    line = "-" *65
    print(line)

    s3 = "Hello\tWorld"
    s4 = "Hello\nWorld"
    print(s3)
    print(s4)

    print(line)
    #Raw string
    s5 = r"Hello\nWorld"
    print("s5- raw string:", s5)
    path = r"C:\New Folder\abc.txt"
    print("Path:", path)
    print(line)
    #creating string from bool, integer, float
    b = True
    n = 56
    f = 3.14
    print("b:", b, "type(b):", type(b))
    print("n:", n, "type(n):", type(n))
    print("f:", f, "type(f):", type(f))
    s1 = str(b)
    s2 = str(n)
    s3 = str(f)
    print("s1:", s1, "type(s1):", type(s1))
    print("s2:", s2, "type(s2):", type(s2))
    print("s3:", s3, "type(s3):", type(s3))
    print(line)
    #Built-in functions
    s = "Hello World!"
    print("type(s):", type(s))
    print("len(s):", len(s))
    print("id(s):", id(s))
    print(line)
    #Built-in operations on string
    #concatination (s1+ s2)
    s1 = "Hello"
    s2 = "Bangtan"
    s3 = s1 + s2
    print("s3:", s3)
    s4 = s1 + "," + s2 + "!"
    print(s4)
    print(line)
    #Multiplication by scalar (s * n)
    s1 = "Hey!"
    s2 = s1 * 3
    print("s2:", s2)
    print(line)
    #Index (s[i])
    s1 = "Hello!"
    print("s[0]:", s[0])
    print("s[3]:", s[3])
    print(line)
    #Traversing through string indexing
    for i in range(len(s1)):
        print("s[", i,"]", s[i])

    print(line)
    #Negative indexing
    print("s1[-1]:", s1[-1])
    print("s1[-3]:", s1[-6])
    print(line)
    #Range operation s([i:j])
    s = "This is s long string created for the purpose of illistration"
    print("len(s):", len(s))
    print("s[3:7]:", s[3:7])
    print("s[1:10]:", s[1:10])
    print("s[3:40]:", s[3:40])
    print(line)
    #Range operations with negative indice
    print("s[-40: -20]:", s[-40:-20])
    print("s[-17:-1]:", s[-17:-1])
    #Range operation with anchor character
    print("s[ : 10]=", s[:10])
    print("s[40 : ]=", s[40 :])
    print(line)
    #slice operation s[i:j:k]
    #with positive k
    print("s[1:10:3]:", s[1:10:3])
    print("s[3:24:4]:", s[3:24:4])

    #with anchor syntax
    print("s[ : 10 : 2]:", s[ : 10 : 2])
    print("s[30 : : 3]:", s[30 : : 3])
    print("s[: : 2]:", s[::2])
    print(line)
    #with negative k
    print("s[7:1:-2]:", s[7:1:-2])
    print("s[8:2:-1]:", s[8:2:-1])
    print("s[::-1]:", s[::-1])
    s1 = s.upper()
    print(s1)
    print(line)
    #string: class method #Index
    s = "aaBBaaBBBaaCCCCaaDDDD"
    n1 = s.index("aa")
    print("n1:", n1)
    n2 = s.index("aa", n1+1)
    print("n2:", n2)
    n3 = s.index("aa", n2+1)
    print("n3:",n3)
    print(line)
    #count method
    print("count method")
    n = s.count("CCCC")
    print("n:", n)
    n5 = s.count("aa")
    print("n5:", n5)
    n = s.count("XYZ")
    print("n:", n)


main()
