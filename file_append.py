# The file already has 3 items from earlier

# Open in 'a' mode — goes to the end, does NOT wipe
file = open("bucket-list.txt", "a")
file.write("4. Travel to Japan\n")
file.write("5. Run a 5K marathon\n")
file.close()
print("2 more items added!")

# Now read the full updated file
file = open("bucket-list.txt", "r")
print(file.read())
file.close()

# Output:
# 1. Visit the Eiffel Tower
# 2. Learn to play the guitar
# 3. Code my own game
# 4. Travel to Japan         <- appended
# 5. Run a 5K marathon       <- appended