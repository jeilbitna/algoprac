answer = ''

name = 'Hyundai-Motor-Company'

arr = name.split('-')

arr = [x[0] for x in arr]

for x in arr:
    answer += x

print(answer)