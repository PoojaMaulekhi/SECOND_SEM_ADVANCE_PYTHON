# num=input("enter a no")

# def count_digit(num):
#  print(len(str(num)))

# count_digit(num)

def count_digit(n):
 count=0
 while n>0:
  n=n//10
  count=count+1
  return count

print("number of digit",count_digit(90))
  

