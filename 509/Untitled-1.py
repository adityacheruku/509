def fixed():
    a = input("Enter data")
    fs = int(input("Enter frame size"))
    f = round(len(a) / fs)
    k = 0

    for i in range(f + 1):
        print("Frame", i + 1)
        for j in range(k, min(k + fs, len(a))):
            print(a[j])
            j+=fs
        k += fs

def variable():
    a = input("Enter data")
    req = len(a)

    for i in range(req):
        k=0
        f1 = int(input(f"Enter frame size for frame "))
        print("Frame no", i, ":")
        for j in range(k+f1):
            print(a[j])
        j+=f1
        k+=f1
        

def main():
    fixed()

if __name__ == "__main__":
    main()






