
def absent_digits(n):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  n = set([int(i) for i in n])
  n = n.symmetric_difference(all_nums)
  n = sorted(n)
  return n
number = input("Enter 10 digit mobile number:")

digit_string = str(number)
digit_map = map(int, digit_string)
digit_list = list(digit_map)


print(absent_digits(digit_list))