# 함수란??(function)
# 특정 작업을 수행하는 코드의 묶음
#  모듈화를 통해 재상용성을 높이는 코드입니다.



# def greeting(name):
#     print("안녕하세요 " + name + " 님!")

# greeting("영수")
# greeting("영철")
# greeting("광수")
# greeting("영희")


# def add_numbers(num1, num2):
#     sum = num1 + num2
#     return sum
#
# result = add_numbers(5,7)
# print(result)


def add_numbers(num1, num2):
    result = num1 + num2
    print(f"두 수의 합은 {result}입니다.")

def multiply_numbers(num1, num2):
    result = num1 * num2
    print(f"두 수의 곱은 {result}입니다.")

def divide_numbers(num1, num2):
    result = num1 / num2
    print(f"두 수의 나눗셈 결과는 {result}입니다.")

num1 = 10
num2 = 20
num3 = 5
num4 = 15
num5 = 8
num6 = 2

add_numbers(num1,num2)
add_numbers(num1,num3)
multiply_numbers(num3,num4)
multiply_numbers(num3,num6)
add_numbers(num4,num3)
divide_numbers(num5,num6)




