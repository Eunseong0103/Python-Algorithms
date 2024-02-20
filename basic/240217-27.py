# Q. 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다.
#    머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 
#    머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# S. 0 < money ≤ 1,000,000


def solution(n, k):
    total = n*12000+k*2000
    if n//10:
        service = n//10
        total=total-service*2000
        return total
    return total

# def solution(n, k):
#     return 12000 * n + 2000 * (k - n // 10)

