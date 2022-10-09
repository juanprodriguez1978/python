# def repeat(s):
#     s2 = ''
#     for i in s:
#         s2+=i*2
#     return s2
# print(repeat('hola'))
# print(repeat('pepe1234'))

def repeat(s):
    return "".join([i*2 for i in s])

print(repeat('hola'))
print(repeat('pepe1234'))
