def x(n,target):
    def sortnum(n):
        n = [n]
        n = n.sort()
        return n
    left = 0
    right = len(n) - 1
    while left < right:
        sum_number = sortnum(left) + sortnum(right)
        if sum_number == target:
            break
        elif sum_number > target:
            right -= 1
        elif sum_number < target:
            left += 1
    if left == right:
        return -1, -1
    else:
        pos1 = n.index(sortnum[left]) + 1
        pos2 = n.index(sortnum[right]) + 1
        if pos1 == pos2:
            pos2 = n[pos1:].index(sortnum[right]) + pos1 + 1
        return min(pos1, pos2), max(pos1, pos2)

a = raw_input()
b = int(input('target:'))
print x(a,b)
