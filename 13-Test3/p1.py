def f(n):
    sticks = ""
    if (n < 1):
        return ""
    else:
        for i in range(1,n+1):
            sticks += "/"
            try:
                if (i % 5 == 0):
                    sticks += "-"
            except:
                pass

        if (sticks[-1] == "-"):
            sticks = sticks[:-1]

        return sticks



