# set

test = {"Django", "Flask", "Bottle", "Pyramid", "Falcon"}

test.discard("Django")

# discard()比remove()更安全，因為如果元素不存在於set中，discard()不會引發錯誤，而remove()會引發KeyError。
print(test)

test.add("Cool")

# add()方法會將元素添加到set中，如果元素已經存在於set中，則不會添加重複的元素。

test.pop()

# pop()方法會隨機刪除set中的一個元素，並返回該元素的值。由於set是無序的，因此無法確定哪個元素會被刪除。
print(test)


#合併兩個set 使用union() , update()方法
set1 = {"Django", "Flask", "Bottle"}
set2 = {"Pyramid", "Falcon", "Cool"}
set1.union(set2) # set2 插到前面
print(set1)
set1.update(set2) # set2 插到後面
print(set1)

#交集intersection(), 差集difference(), 子集 issubset()


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
#print(it_companies.add("Twitter")) #這樣寫會回傳None，因為add()方法不會返回任何值。
it_companies.add("Twitter")
print(it_companies)

more_IT = {"LinkedIn", "Snapchat"}
it_companies.update(more_IT)
print(it_companies)

a = A.intersection(B)
print(a)

b = A.issubset(B)
print(b)
