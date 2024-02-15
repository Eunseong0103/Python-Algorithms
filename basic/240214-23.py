# Q. 문자열 my_string과 문자 letter이 매개변수로 주어집니다. 
#    my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.



# S. 1 ≤ my_string의 길이 ≤ 100
#   letter은 길이가 1인 영문자입니다.
#   my_string과 letter은 알파벳 대소문자로 이루어져 있습니다.
#   대문자와 소문자를 구분합니다.


def solution(my_string, letter):
    return my_string.replace(letter,"")



#  replace(old, new, [count])' 형식으로 사용한다.

# - old : 현재 문자열에서 변경하고 싶은 문자

# - new: 새로 바꿀 문자

# - count: 변경할 횟수. 횟수는 입력하지 않으면 old의 문자열 전체를 변경한다. 기본값은 전체를 의미하는 count=-1로 지정되어있다. 

