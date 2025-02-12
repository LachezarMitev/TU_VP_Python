n = int(input())
children = []
adults = []
age_sum = 0
for i in range(n):
    age = int(input())
    if age < 18: children.append(age)
    else: 
        adults.append(age)
        age_sum += age

print(children, "\n", adults, 
      f"\nNumber of children: {len(children)}", 
      f"\nNumber of adults: {len(adults)}", 
      f"\nAverage age of adults: {age_sum / n}")