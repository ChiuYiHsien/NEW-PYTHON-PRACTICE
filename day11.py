

count = 0
while count <= 10:
    print(count)
    count += 1
    
count = 10
while count >= 0:
    print(count)
    count -= 1
    
    
#str = "Python"
#for i in str:
#    print(i)
    
#for i in range(len(str)):
#   print(str[i])

for i in range(10,0):
    print(i)
    
str_t = '#'

for i in range(0,7):
    print(str_t)
    str_t += '#'
    
index = 1
for i in range(7):
    print('#' * index)
    index += 1
    

for i in range(0,8):
    for j in range(0,8):
        print("#", end = ' ')
    print() #自動換列
    
print("__________")
for i in range(8):
    print("# " * 8)
        
print("__________")

for i in range(1,9):
    print( f"{i} * {i} = {i}")
    
odd_sum = 0
even_sum = 0

for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"The sum of all odd numbers is {odd_sum}. And the sum of all even numbers is {even_sum}.")

import countries
import countries_data

list_land = []
for country in countries.countries:
    if 'land' in country:
        list_land.append(country)

print(list_land)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse() #reverse()不會回傳東西，如果寫成 fruits = fruits.reverse()會回傳none
print(fruits)
#另一種寫法是宣告一個新列表new = fruits[::-1]

all_lan = set()

for country in countries_data.datas:
    all_lan.update(country["languages"])# update()可以把列表中所有不重複的全部加進set

print(f"There are totally {len(all_lan)} languages")
    

counts = {} #使用字典來存語言和次數對應，如{"English":23, "Chinese":12}等等......
for country in countries_data.datas:
    lans = country.get("languages", [])
    for lan in lans:
        if lan in counts:
            counts[lan] += 1
        else:
            counts[lan] = 1
         
#max_count = 0
#most_lan = None
#for lan, count in counts.items(): #items()會把字典裡面的key-value對應拆成許多tuple {(k-v),(k-v),(k-v)......}
    #if count > max_count:
        #max_count = count
        #most_lan = lan
#print(f"最多國家使用的語言是{most_lan}，共{max_count}國使用")

temp_counts = counts.copy()

for i in range(10):
    top_ten = []
    max_count = -1
    most_lan = None
    if count > max_count:
        max_count = count
        most_lan = lan
        
    if most_lan:
        top_ten.append((most_lan, max_count))
        del counts[most_lan]
        
    
for i in range(10):
    print(f"第{i}多國家使用的語言是{most_lan}，共{max_count}國使用")




