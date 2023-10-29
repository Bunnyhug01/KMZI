from .base import base


def group(mod: int):
    baseVar = base(mod)
    result = set()
    
    if type(baseVar) == str:
        return baseVar 
    
    x = baseVar
    while x not in result:
        result.add(x)
        x = (x * baseVar) % mod
    return sorted(list(result))