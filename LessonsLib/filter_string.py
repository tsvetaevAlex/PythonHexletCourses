def filter_string(message: str, expel_symbol: str) -> str:
    print (f"message : {message}")
    print (f"expel_symbol : {expel_symbol}")
    return_value: str = ''
    for char in message:
        if not char.lower() == expel_symbol.lower():
            #print(f"append symbol; {char}")
            return_value +=char

    print (f"return value : {return_value}")
    return return_value.strip()


text = 'I look back if you are lost'
assert filter_string(text, 'w') == 'I look back if you are lost'
assert filter_string(text, 'I') == 'look back f you are lost'
assert filter_string(text, 'o') == 'I lk back if yu are lst'
assert filter_string('zz zorro', 'z') == 'orro'