import sys

# Read all the input into a string, spaces, newlines and all, but
# I remove the newlines since these are annoying to print...
x = sys.stdin.read().replace("\n", "")

count = {}
# Count the characters in `x`` and put the counts in `counts`.
# Your code goes here.

# dictionary has "keys" and values (can be values or lists)
# le estoy diciendo que dentro de count, le ponga el valor de uno al i (por ejemplo la h de hello)
# si la letra ya está, le digo que le sume 1
for i in x:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1


# Get the keys, i.e., the characters, in sorted order
# and print the count
for a in sorted(count):
    print(f"{a}: {count[a]}")
