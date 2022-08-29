input_str = input()
input_chr = input()

input_chr = input_chr.upper()
input_str = input_str.upper()
from collections import Counter
c = Counter(input_str)
print(c[input_chr])

