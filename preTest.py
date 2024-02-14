def normalize_url(adr: str) -> str:
    not_secured_prefix: str = "'http://"
    secured_prefix: str = "https://"
    result = None
    if not_secured_prefix in adr:
        result = adr.replace(not_secured_prefix, secured_prefix)
        return result
    else:
        result = secured_prefix + adr
    print (result)
    return result


normalize_url('https://ya.ru')  # https://ya.ru
normalize_url('google.com')  # https://google.com
normalize_url('http://ai.fi')  # https://ai.fi
