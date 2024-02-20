# Q. 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
#    정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

# S. 1 ≤ n ≤ 1,000,000



def solution(n):
    for i in range(1,n):
        if i*i==n:
            return 1
    return 2

#! is_integer()를 통해 주어진 수의 제곱근이 정수인지 확인해주는 함수
# def solution(n):
#     return 1 if (n ** 0.5).is_integer() else 2
