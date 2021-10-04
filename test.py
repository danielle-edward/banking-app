import sys

def test():
    input1 = input("1?")
    input2 = input("2?")
    print("1:", input1, "2:", input2)

def run():
    f1 = sys.stdin
    f = open('input.txt','r')
    sys.stdin = f
    test()
    f.close()
    sys.stdin = f1
