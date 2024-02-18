
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

print(f"{value[2]}{value[3]}{value[1]}")


text123 = 'When \t\n you play a \t\n game of thrones you win or you die.'

# BEGIN (write your solution here)
sub_string = text123[5:16].strip()
print(sub_string)
print(f"Sub string Len: {len(sub_string)}")
# END