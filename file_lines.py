# open the file
file = open('class-notes.txt', 'r')
lines = file.readlines()
file.close()

# how many lines are there?
print('Total lines:', len(lines))

# print each line with its number
for i in range(len(lines)):
    print(i + 1, '->', lines[i].strip())

# output:
# Total lines: 7
# 1 -> Maths: Learn equations today
# 2 -> Coding: Variables and loops
# ...