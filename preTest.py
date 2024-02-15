non_secured_prefix: str = "http://"
secured_prefix: str = "https://"


def normalize_url(url: str) -> str:
    if (secured_prefix in url):
        return url

    if (non_secured_prefix in url):
        result = url.replace(non_secured_prefix, secured_prefix)
        return result

    if not (secured_prefix in url) and not (non_secured_prefix in url):
        result = secured_prefix + url
        return result

    if (non_secured_prefix in url):
        result = url.replace(non_secured_prefix, secured_prefix)
        return result


normalize_url('https://ya.ru')  # https://ya.ru
normalize_url('google.com')  # https://google.com
normalize_url('http://ai.fi')  # https://ai.fi
