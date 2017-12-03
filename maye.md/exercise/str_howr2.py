import sys
a = raw_input()
m = 0
b = []
for i in a:
    if 64 < ord(i) < 91 or 96 < ord(i) < 123:
        m = ord(i) + 1
        sys.stdout.write(chr(m))
    else:
        sys.stdout.write(i)
print
