# Q. 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
#    문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.


# S. my_string은 소문자와 공백으로 이루어져 있습니다.
#    1 ≤ my_string의 길이 ≤ 1,000


def solution(my_string):
    i = "aeiou"
    result = "".join(str for str in my_string if str not in i)
    return result


# def solution(my_string):
#     vowels = ['a','e','i','o','u']
#     for vowel in vowels:
#         my_string = my_string.replace(vowel, '')
#     return my_string