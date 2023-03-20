#Oleksii Kaba

#Контрольні запитання
letters = ['a', 'b', 'c', 'd']
print(letters[int('3' * 2) // 11])
# Answer is 'd'

print(letters[-1])
# Answer is 'd'

print(letters[:2])
# Answer is 'a' and 'b'

letters = [2, 4, 6, 8, 10]
letters.insert(3 , 'zero')
print(letters)

metering = [3.14, 'inch', 2.54, 'inch', True]
print(metering.index('inch'))

metering = [3.14, 'inch', 2.54, 'inch', True]
metering.append(99)
print(metering)

metering = [3.14, 'inch', 2.54, 'inch', True]
metering.remove('inch')
print(metering)

# 'append' = додає до кінця списку 
brands = ['Adidas', 'Nike', 'Puma']
brands.append('Kappa')
print(brands)

# 'insert' = Ви самі можете вказати куди саме додати 
brands = ['Adidas', 'Nike', 'Puma']
brands.insert(1, 'Kappa')
print(brands)


# 1 варіант = видалення елементу за номерацією самого елементу:
brands = ['Adidas', 'Nike', 'Puma']
del brands [-1]
print(brands)

# 2 варіант = видалення елементу за назвою самого елементу:
brands = ['Adidas', 'Nike', 'Puma']
brands.remove('Adidas')
print(brands)

# 3 варіант = видалення елементу за номерацією самого елементу але бачиш що видаляєш:
brands = ['Adidas', 'Nike', 'Puma']
brands.pop(1)
print(brands)




# Задачі
languages = ('Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian')
world_languages = sorted(languages)
print(world_languages)

languages = ('Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian')
print(languages)

nums = [2, -1, 9, 6]
print(sum(nums))


cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
cities.insert(5, 'and')
print(cities)
numbers = [1, 2, 3, 4, 5]
numbers_reverse = [5, 4, 3, 2, 1]
numbers.extend(numbers_reverse)
print(numbers)

kinds_sports = ['Hockey', 'Football', 'Basketball', 'Baseball', 'Golf']
print('Baseball' in kinds_sports)
print('Volleyball' in kinds_sports)
