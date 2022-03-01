from typing import  Counter, DefaultDict, OrderedDict
import time as tit

def basic(sequence):
    a = "|".join(sequence)
    dir = DefaultDict()
    for i in  range(1,len(a)-1):
        # tit.sleep(3)
        # print(f"{i=}")
        # Count = 0
        mint = 0 
        taste=""
        while (i-mint)>-1 and (i+mint)<len(a) and a[i+mint]==a[i-mint]:
            # print(f'true for {i=} {a[i]=}')
            taste = a[i+mint]+taste+a[i-mint]
            # Count+=1
            mint+=1
        dir[i]=taste
    # print(a)
    # print(dir)
    ak = ""
    for i in dir.values():
        if len(i)>len(ak):ak = i
        # print(i)
    ak  = [i for i in ak if i!="|"]
    # ak.pop(len(ak)//2)
    print("".join(ak))

basic("owowo")