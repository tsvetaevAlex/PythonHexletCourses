def get_one():
    return 1


motto = 'Family, Duty, Honor'

# BEGIN (write your solution here)
print(type(motto))
# END


number = 10.1234

# BEGIN (write your solution here)
round_number = round(number)
print(f"round: {round_number}")
print(hex(round_number))



print("---------------------")

result = sum(sum(1, 3), sum(sum(4, 2), 3))
print(result)