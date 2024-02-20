# Q. 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.


# S. 0 ≤ numbers의 원소 ≤ 10,000
#    2 ≤ numbers의 길이 ≤ 100


def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]


#! sort() 메서드:
# list.sort()는 리스트 자체를 정렬하며, 원본 리스트를 변경합니다.
# 반환 값은 None입니다.

#! sorted() 함수:
# sorted(list)는 정렬된 새로운 리스트를 반환하며, 원본 리스트는 변경되지 않습니다.
# 반환 값은 새로운 정렬된 리스트입니다.