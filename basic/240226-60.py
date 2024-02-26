# Q. 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, 
#    my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.

# S. 0 < my_string 길이 < 100

def solution(my_string):
    answer=""
    for i in my_string:
        answer+=i.lower()
    sorted_string = ''.join(sorted(answer))
    return sorted_string


# def solution(my_string):
#    return ''.join(sorted(my_string.lower()))


# 리스트나 튜플 등의 iterable한 객체의 각 요소를 문자열로 이어붙이고 싶다면 join()을 사용할 수 있습니다. 
# 하지만, 숫자, 딕셔너리, 집합 등에서는 join()을 사용할 수 없습니다.