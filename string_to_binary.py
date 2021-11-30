def space_by_eigth(a):
    return ' '.join([a[i:i + 8] for i in range(0, len(a), 8)])

q = "?"
c = ","
d = "."


question_mark = '02b', 111111, '04b', 1010
comma = '02b', 101100, '04b',1010
dot = '02b', 101110, '04b',1010

quso = "Jee jee"
   
print("The original string is : " + str(quso))

if (q or c or d in quso):
    q = question_mark
    c = comma
    d = dot

res = ''.join(format(ord(i), '08b') for i in quso)
  
print("The string after binary conversion : " + str(space_by_eigth(res)))