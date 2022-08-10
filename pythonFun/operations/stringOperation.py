__all__=["concatString","stringMul"]

def concatString(str1: str, str2: str) -> str:
    return _stringAddition(str1,str2)


def stringMul(str1: str, num: int)  -> str:
    return str1 * num

# * private functions start with '_'

def _stringAddition(str1: str,str2: str):
    return str1 +str2