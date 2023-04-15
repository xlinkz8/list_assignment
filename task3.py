
# Q3. write a python function thst removes  duplicates from an amount in a listand also
# sum up all the items and remove 7% vat from that amount and print the amount.


numbers = [2000 , 4000 ,8000 ,9000 ,4500 ,7400 ,1200 ,9000 ,4000, 7400 ,1200]
rm_dup = set(numbers)
sum_num = sum(rm_dup)
vat = 7
final_amount = sum_num * (1 - vat/100)
print(f"your balance is N{final_amount}.")