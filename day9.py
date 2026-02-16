# dic 裡面可以放各種資料型態，甚至是 list 或 tuple

dct = {
    "name": "Yi-Hsien",
    "age": 30,
    "country": "Taiwan",
    "skills": ["Python", "JavaScript", "HTML", "CSS"],
    "is_married": False
}

print(dct["skills"]) # ['Python', 'JavaScript', 'HTML', 'CSS']
print(dct["skills"][0]) # Python

#要確定該key存在才不會error， 不然就用'get'

print(dct.get("is_married")) # False
print(dct.get("address")) # 該key不存在，所以回傳None

#可以直接新增不同的key-value
dct["address"] = "Taipei"
print(dct)

#刪除資料
# pop() : 刪除指定key的資料，並回傳該key的value
# popitem() : 刪除最後一筆資料，並回傳該key的value
# del : 刪除指定key的資料，但不回傳該key的value

dct.pop("age")
print(dct)

dct.popitem()
print(dct)

del dct["is_married"]
print(dct)