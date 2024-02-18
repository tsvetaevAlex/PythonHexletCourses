def normalize_url(url: str) -> str:
    non_secured_prefix: str ="http://"
    secured_prefix: str = "https://"

    if url.startswith(secured_prefix):
        return url

    if url.startswith(non_secured_prefix):
        return url.replace(non_secured_prefix, secured_prefix)

    if not url.startswith(secured_prefix) and not url.startswith(non_secured_prefix):
        return secured_prefix + url