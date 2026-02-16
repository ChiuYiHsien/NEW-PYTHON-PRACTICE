age = input("Enter your age: ")

print(type(age)) #str

if int(age) >= 18:
    print("You are old enough to drive.")
else:
    print("You still need to wait " + str(18-int(age)) + " years to drive.")
    
print(type(age)) #str


my_age = 23

if my_age > int(age):
    print("I'm " + str(my_age - int(age)) + " years older than you.")
elif my_age < int(age):
    print("You're " + str(int(age) - my_age) + " years older than me.")
else:
    print("We are same age.")
    
    
fruits = ['banana', 'orange', 'mango', 'lemon']
buy = input("What do you want to buy? : ")
if buy in fruits:
    print('该水果已在列表中')
else:
    fruits += [buy]
    print(fruits)
    
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': '芬兰',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '太空街',
        'zipcode': '02210'
    }
}

front = {'JavaScript', 'React'}
back = {'Node', 'MongoDB', 'Python'}
full = {'React', 'Node', 'MongoDB'}

person_skills = set(person.get("skills",[])) 
# 用person.get("skills",[])比直接使用person["skills"]好，前者若找不到會回傳none，後者會噴error
# []表示如果找不到就回傳一個空list

if "skills" in person:
    print(person['skills'])
    
    if full.issubset(person_skills): #條件嚴苛的放前面
        print("他是全端開發者")
    if front == person_skills: #用set來比較就不會有順序問題
        print("他是前端開發者")
    elif back == person_skills:
        print("他是後端開發者")
    elif 'Python' in person_skills:
        print("他有python能力")
    else:
        print("未知")
    
