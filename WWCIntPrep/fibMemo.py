# http://www.geeksforgeeks.org/dynamic-programming-set-1/
# Python program for Memoized version of nth Fibonacci number
 
# Function to calculate nth Fibonacci number
def fib(n, lookup):
 
    # Base case
    if n == 0 or n == 1 :
        lookup[n] = n
        # print lookup[n]
 
    # If the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup) 
        # print lookup[n]
 
    # return the value corresponding to that value of n
    return lookup[n]
# end of function
 
# Driver program to test the above function
def main():
    n = 34
    # Declaration of lookup table
    # Handles till n = 100 
    lookup = [None]*(101)
    print "Fibonacci Number is ", fib(n, lookup)
    # print lookup
 
if __name__=="__main__":
    main()



# This code is contributed by Nikhil Kumar Singh(nickzuck_007)