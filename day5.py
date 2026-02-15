list1 = []
list2 = ["apple", "banana", "cherry", "orange", "kiwi"]
print(len(list2))
mixed_data_types = ["Yi-Hsien", 23, 172, "single", "Taipei"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("Twitter")
it_companies[3] = it_companies[3].upper()
print(it_companies)

company1 = it_companies[0:3:]
print(company1)

it_companies.remove("IBM")
print(it_companies)

it_companies.pop(0)
print(it_companies)

it_companies += ["#"]
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies