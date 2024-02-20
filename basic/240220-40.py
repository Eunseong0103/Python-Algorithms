# Q. 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

# S. 0 ≤ n ≤ 1,000,000


def solution(n):
    nums = [int(num) for num in str(n)]
    return sum(nums)




                