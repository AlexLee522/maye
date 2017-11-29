x = raw_input('please input a number:')
if x == x[::-1]:
    print '%s is a palindrome number' % x
else:
    print '%s is not a palindrome number ' % x
