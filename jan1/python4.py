
# Find the missing number in the list 

# 1 method 

# l = [1,2,3,4,6,7,8]
# minel = min(l)
# maxel = max(l)
# for i in range(minel,maxel+1):
#     if i not in l:
#         print(i)

# 2 method 

list = [11,12,13,14,15,16,17,19]
minel = min(list)
maxel = max(list)
sum_of_list = sum(list)
sum = 0
for i in range(minel,maxel+1):
    sum = sum + i
print(sum - sum_of_list)
