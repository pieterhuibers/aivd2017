import sys

def is_valid(i, sum, product) :
   current_sum = 0
   current_product = 1
   for c in str(i) :
      n = int(c)
      current_sum = current_sum + n
      current_product = current_product * n
   return current_sum == sum and current_product == product

def find_number(n, sum, product) :
    max = 10**n
    for i in range(max) :
        if is_valid(i, sum, product) :
            print i

if __name__ == "__main__" :
    n = int(sys.argv[1])
    sum = int(sys.argv[2])
    product = int(sys.argv[3])
    find_number(n,sum,product)
