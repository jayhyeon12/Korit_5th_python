# 함수

def add(num1, num2):
    return num1 + num2

print(add(10, 20))

result1 = add(10, 20)
print(result1)

def add(num1, num2, num3, num4):
    return num1 + num2, num3 + num4

result2 = add(10, 20, 35, 55)
print(result2)

nums = [5, 2, 7, 3, 1]
nums.sort()
print(nums)

nums.reverse()
print(nums)

name = "김종현"
print(name.find("기"))
# print(name.index("기"))

# print(nums.index(3))

user = {
    "username": "testuser",
    "password": "93864",
    "name": "orka",
    "mail": "orka@gmail.com"
}

user.update({"phone": "34-41245-6742-73"})
# user["phone"] = "34-41245-6742-73"
print(user)