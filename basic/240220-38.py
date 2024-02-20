# Q. 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 
#    처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.


# S. 1 ≤ n ≤ 10
#    1 ≤ t ≤ 15

def solution(n, t):
    answer=n
    for i in range(1,t+1):
        answer = answer *2
    return answer


# def solution(n, t):
#     return n*(2**t)