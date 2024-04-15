number = 10
print(type(number)) # type(): 자료형 확인

print(id(10)) # id(): 주소 값 확인
print(id(number))

number += 1
print(id(number))

number -= 1
print(id(number))

print(type("test"))
print(type([]))
print(type(()))
print(type({}))

print([1, 2, 3, 4])
print((1, 2, 3, 4))
print({"id": 1, "name": 2})

list1 = [1,2,3,4]
tuple = (5,6,7,8)
dic1 = {"id": 1, "name": "G"}

print(list1[0])
print(tuple[0])
print(dic1["id"])

list1.append(5)
print(list1)

list2 = list(tuple)
print(list2)

print(dic1.keys())
print(dic1.values())
print(list(dic1.items())[0])

print(True) # bool 자료형: 값을 대문자로 작성