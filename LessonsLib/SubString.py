def my_substr(text: str, len: int):
    print(f"inbound params: text=={text} and Len=={len}")
    i: int = 1
    result:str = ''
    while (i <= len):
        print(f'index: {i-1} symbol: {text[i-1]}')
        result += text[i-1]
        i += 1
    return_value = result
    print(f"result=={result}")
    del result
    print(f"return_value=={return_value}")
    return  return_value


my_substr('got', 3)
my_substr('got', 2)
my_substr('got', 1)