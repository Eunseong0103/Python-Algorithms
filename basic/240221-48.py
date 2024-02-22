# Q. 정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# S. 1 ≤ array의 길이 ≤ 100
#    0 ≤ array 원소 ≤ 1,000
#    array에 중복된 숫자는 없습니다.

def solution(array):
    
    max_value=max(array)
    max_index=array.index(max_value)
    return [max_value,max_index]

def solution(array):
    return [max(array), array.index(max(array))]


# max() 함수는 주어진 인자 중에서 가장 큰 값을 반환하는 내장 함수

# index() 메서드는 리스트에서 주어진 값의 첫 번째 출현 위치(인덱스)를 반환합니다.
# 예를 들어, numbers = [3, 7, 1, 5, 2]일 때, numbers.index(7)은 1을 반환합니다

#!enumerate() 함수는 순회 가능한(iterable) 객체(예: 리스트, 튜플, 문자열)를 입력으로 받아, 
#!각 요소에 대해 인덱스와 값을 쌍으로 묶어 튜플로 반환하는 파이썬의 내장 함수입니다.

# my_list = ['apple', 'banana', 'orange']

# for index, value in enumerate(my_list):
#     print(index, value)
