def mystery(q):
  return '%'.join(map(repr, map(lambda x: x if len(x) == 0 else x[0] if len(x) == 1 else "%s%s%s" % (x[0], "%s", x[-1]), [q[len(q)/2-i:len(q)/2+i+(1 if len(q) % 2 == 1 else 0)] for i in xrange(len(q)/2+1)])[::-1]))

print mystery("hello world")
print eval(mystery("hello world"))

# Output:
# 'h%sd'%'e%sl'%'l%sr'%'l%so'%'o%sw'%' '
