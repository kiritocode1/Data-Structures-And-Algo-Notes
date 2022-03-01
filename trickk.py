# from typing import Counter

# with("./constits.txt.txt") as file:
#     cum = {}
#     for i in filr.readlines():
#         for j in i:
#             cum[i].add(j)

from cgi import print_directory


for i in range(ace:=int(input("enter the side length--->"))):
    print("1"*ace)

for item in range(ace:=int(input("enter the no of columns--->"))):
    print("2"*(item+1))

i=0
for _ in range(ace:=(2*int(input("enter the no of columns -->"))+1)):
    if _ <=ace//2:
        print(f'{" "*(ace//2)}{"3"*_}{"3"*(_+1)}')
    else:
        print("3"*(ace//2-i))
        i+=1
