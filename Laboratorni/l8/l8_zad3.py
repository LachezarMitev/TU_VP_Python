import math

exc = ValueError("Invalid num!")
try:
    num = int(input())
    if num < 0:
        raise exc
    else:
        print(math.sqrt(num))
except:
    raise exc
finally:
    print("Good bye!")