s = "Strings are awesome!"
# Довжина повинна бути 20
print("Length of s = %d" % len(s))

# Перше входження "a" має бути з індексом 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Кількість a має бути 2
print("a occurs %d times" % s.count("a"))

# Нарізання рядка на біти
print("The first five characters are '%s'" % s[:5]) # Почніть з 5
print("The next five characters are '%s'" % s[5:10]) # 5 до 10
print("The thirteenth character is '%s'" % s[12]) # Просто номер 12
print("The characters with odd index are '%s'" %s[1::2]) # (Індексація на основі 0)
print("The last five characters are '%s'" % s[-5:]) # 5-й - від останнього до кінця

# Перетворити все на великі літери
print("String in uppercase: %s" % s.upper())

# Перетворити все на малі літери
print("String in lowercase: %s" % s.lower())

# Перевірте, як починається рядок
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Перевірте, як закінчується рядок
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Розбийте рядок на три окремі рядки,
# кожен з яких містить лише слово
print("Split the words of the string: %s" % s.split(" "))