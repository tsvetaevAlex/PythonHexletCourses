def  sort_pair(items):
    item1, item2 = items
    print(f"item1:{item1}")
    print(f"item2:{item2}")

    if item1 > item2:
        print(f"return tuple--> {item2} | {item1}")
        return(item2, item1)
    else:
        print(f"return tuple--> {item1} | {item2}")
        return(item1,item2)



sort_pair((5, 1)) # (1, 5)
sort_pair((2, 2)) # (2, 2)
sort_pair((7, 8)) # (7, 8)
assert sort_pair((5, 1)) == (1, 5)
assert sort_pair((2, 2)) == (2, 2)
assert sort_pair((7, 8)) == (7, 8)