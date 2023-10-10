"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    indice = 0
    while indice < 6:
        result.append(5 - indice)
        indice += 1
    return result