a=eval(input("enter the numbers=: "))
print(a)
for i in a:
      if i%2==0:
        list = [i]
if list != []:
    print(max(list))
else:
    print("there is no even numbers")

