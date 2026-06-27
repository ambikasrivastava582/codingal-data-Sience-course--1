# read all lines into a list
file = open('class-notes.txt', 'r')
lines = file.readlines()
file.close()

# open a new file for writing
out = open('odd-lines.txt', 'w')

# range(0, len, 2) gives index 0, 2, 4, 6 -- every other line
for i in range(0, len(lines), 2):
    out.write(lines[i])

out.close()
print('Odd lines saved to odd-lines.txt')

# odd-lines.txt will contain:
# Maths: Learn equations today
# Science: Photosynthesis
# English: Essay writing
# History: World War II