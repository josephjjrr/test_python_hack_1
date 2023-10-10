"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    result = result.replace(result[1:2] , "0")
    result = result.replace(result[4] , "1")
    result = result.replace(result[6] , "@")
    return result
