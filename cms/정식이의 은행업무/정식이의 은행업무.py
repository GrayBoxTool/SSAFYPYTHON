import sys
sys.stdin = open("sample_input.txt", "r")
from copy import deepcopy

# 테스트 케이스 갯수 할당
T= int(input())
for test_case in range(1,T+1):
    # 2진수 송금액 할당
    bin_num = str(input())
    # 3진수 송금액 할당
    ter_num = str(input())
    bin_lst = []
    ter_lst = []
    # 각 자리의 숫자를 수정하기 쉽도록 문자열을 정수 리스트로 변환
    for i in bin_num :
        bin_lst.append(int(i))
    for i in ter_num :
        ter_lst.append(int(i))

    # 수정한 2진수를 10진수로 변환한 값
    bin_value = 0
    # 수정한 3진수를 10진수로 변환한 값
    ter_value = 0
    # 2진수와 3진수에서 동일한 값이 발견되면 저장할 변수
    result = 0

    # 2진수의 모든 자리를 하나씩 확인
    for j in range(1,len(bin_lst)+1):
        # 원본 2진수 리스트가 변경되지 않도록 복사
        bin_copy = deepcopy(bin_lst)
        # 2진수 값을 반전
        bin_copy[-j] = (bin_copy[-j]+1) % 2
        if bin_copy[0] == 0:
            continue
        for m in range(len(bin_lst)) :
            # 한 자리를 수정한 2진수를 문자열로 합친 후 10진수로 변환
            bin_value = int(''.join(map(str, bin_copy)), 2)

        # 3진수의 모든 자리를 하나씩 확인
        for k in range(1,len(ter_lst)+1):
            # 현재 값이 아닌 나머지 두 가지 경우를 모두 확인
            for l in range(1,3):
                ter_copy = deepcopy(ter_lst)
                ter_copy[-k] = (ter_copy[-k]+l) % 3
                if ter_copy[0] == 0:
                    continue
                for n in range(len(ter_lst)) :
                    # 한 자리를 수정한 3진수를 문자열로 합친 후 10진수로 변환
                    ter_value = int(''.join(map(str, ter_copy)), 3)
            # 수정된 2진수와 3진수의 값이 같으면 result에 저장하고 반복문 종료
            if bin_value == ter_value :
                result = bin_value
                break
        # result값에 따라 불필요한 반복을 멈춤
        if result !=0:
            break
    print(f"#{test_case} {result}")