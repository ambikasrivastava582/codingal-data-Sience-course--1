# Open the file in read mode
file = open("bucket-list.txt", "r")

# read() returns ALL content as one string
content = file.read()

print("=== My Bucket List ===")
print(content)

file.close()   # always close after reading

# Output:
# === My Bucket List ===
# 1. Visit the Eiffel Tower
# 2. Learn to play the guitar
# 3. Code my own game