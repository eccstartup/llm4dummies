# this is the first comment
spam = 1  # and this is the second comment
# ... and now a third!
text = "# This is not a comment because it's inside quotes."

width = 20
width = 'abc'
"what's up"

a = 1
b = a
b = 2
print(a)
print(b)


x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# Now call the function we just defined:
fib(2000)


def plus1(n):
    print('Hello world')
    # return n + 1


# p1 = lambda x: x + 1
print((lambda x: x + 1)(3))
