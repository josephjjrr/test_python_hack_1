"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    for numero in range(7):
        if numero == 1 or numero == 3 or numero == 6:
            result.insert(numero , "@")
    return result