# 함수 구현
# add() 함수 정의
def add(a, b):
    c = a + b
    print('add called!!')
    return c

# substract() 함수 정의
def sub(a, b):
    sub_result = a - b
    return sub_result

# multiply() 함수 정의
def mul(a , b):
    mul_result = a * b
    return mul_result

# divide() 함수 정의
def div(a , b):
    div_result = a/b
    return div_result



if __name__ == '__main__':
    result = add(10, 20)  # 함수호출
    print(result)
    print('Exit')

    sub_result = sub(10, 20)
    mul_result = mul(10, 20)
    div_result = div(10, 20)