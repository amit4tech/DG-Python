
count = 0
def permutation(st, allowed_chars, ix):
    global count
    if len(st) >= len(allowed_chars):
        count += 1
        print(st)
    else:
        for i in range(len(allowed_chars)):
            if i not in ix:
                ix.append(i)
                st += allowed_chars[i]
                permutation(st, allowed_chars, ix)
                st = st[:-1]
                ix.pop(-1)

permutation("", ["a", "e", "i", "o", "u", "z"], [])
print(count)