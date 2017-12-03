import sys
a = raw_input()
m = 0
b = []
for i in a:
    if 64 < ord(i) < 90 or 96 < ord(i) < 122:
        m = ord(i) + 1
        sys.stdout.write(chr(m))
    elif ord(i) == 90:
        sys.stdout.write('A')
    elif ord(i) == 122:
        sys.stdout.write('a')
    else:
        sys.stdout.write(i)
print
