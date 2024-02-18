def truncate(text, length):
    result: object = text[:length] + "..."
    return result





print(truncate("missing 1 required positional argument", 15))
