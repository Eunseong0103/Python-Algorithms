# Q. 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
#    자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

# S. 1 ≤ n ≤ 100


#!
def solution(n):
    composite_count = 0  # 합성수의 개수를 세기 위한 변수

    for i in range(4, n + 1):  # 4부터 시작하여 n 이하의 수에 대해 합성수 검사
        divisor_count = 0  # 현재 수 i의 약수 개수를 저장하는 변수

        for j in range(1, i + 1):
            if i % j == 0:
                divisor_count += 1

        if divisor_count >= 3:  # 약수 개수가 3 이상인 경우, 합성수로 판단
            composite_count += 1

    return composite_count