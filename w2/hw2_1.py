n = int(input("請輸入三角形的高度:"))
if n <= 1:
    print("輸入錯誤")
else:
    L = n
    R = n
    for i in range(1, n):
        if i != 1:
            L -= 1
            R += 1  
        if i == 1:
            #top
            print(" " * (n-1) + "*" + " " * (n-1))
        else:
            #mid
            line = ""
            for j in range(1, n*2):
                if j == L or j == R:
                    line += "*"
                else:
                    line+= " "
            print(line)
    #bottom
    print("*" * (2*n - 1), end="")