# Q1. write a python program that sums up all the items in a lst of 9 items;
# remove duplicates and print the result.

# user list 9  numbers
# user removes duplicate
# user sum up number and then
# print the result


age =[32, 45, 22 ,89 ,10 ,32 ,45 ,44]
remove_dup = set(age)
age_sum = sum(remove_dup)
print(age_sum)
