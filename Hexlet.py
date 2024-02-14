
#строки подстроки срезы

text = 'Hexlet'
#xeH
print(f"0-{text[0]}")
print(f"1-{text[1]}")
print(f"2-{text[2]}")
print(f"3-{text[3]}")
print(f"4-{text[4]}")
print(f"5-{text[5]}")

print("-----------------")
print(text[2::-1])

#В переменной value лежит значение Hexlet.
# Извлеките из него и выведите на экран срез,
# который получит подстроку xle. Это задание можно сделать разными способами.


print("-----------------")

value = "Hexlet"

print(value[2:4])

#---------------------------------------
#type conversion
number = 2

t = "times"

print(f"{str(number)} {t}")#=> 2 times
#---------------------------------------

print("-----------------")

value = "-42"

# BEGIN (write your solution here)
value = "-42"
int_value = int(value)
abs_value = abs(int_value)
print(abs_value)
# END
# END
