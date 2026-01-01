
# Number Expansion Calculator 

a = int(input("Enter here:"))

num1 = int("%s" % a)
num2 = int("%s%s" % (a,a))
num3 = int("%s%s%s" % (a,a,a))

sum_of_num = (num1 + num2 + num3)
print(sum_of_num)

