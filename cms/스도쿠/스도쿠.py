import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def row_test(data) :
    for i in range(0,9):
        if len(set(data[i])-num_group) > 0:
            return False
    return True

def column_group(data):
    new_list=[]
    for i in range(0,9):
        new_list.append([])
        for j in range(0,9):
            new_list[i].append(data[j][i])
    return new_list

def _3x3(data) :
    for i in range(0,2)
case_num = 0
for test_case in range(1, T + 1):
    num_group = {1,2,3,4,5,6,7,8,9}
    test_case =[]
    case_num += 1
    for i in range(0,9):
        test_case.append(list(map(int,input().split())))
    if row_test(test_case) and row_test(column_group(test_case)) == True:
        print(f"#{case_num} 1")
    else :
        print(f"#{case_num} 0")
                    
                





        





