"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    return result.replace(result[-1] , result[-1].capitalize())