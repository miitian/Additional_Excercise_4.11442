def fib2(n):
    list1 = [0, 1]
    if n <= 0:
        print("Please enter a positive integer")

    elif n == 1:
        print(f"Fibonacci sequence upto", {n}, ":")
        return (list1[0])

    else:
        print(f"Fibonacci sequence upto", {n}, ":")
        x = 0
        while x < n:
            x = list1[-1] + list1[-2]
            if x < n:
                list1.append(x)
        return list1

print(fib2(10))