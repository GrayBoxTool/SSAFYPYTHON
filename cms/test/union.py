# arr=[i for i in range(6)]
# print(arr)
arr=[0,1,2,3,4,5]
rank=[0]*6
def findboss(member):   #자기 자신이 보스라면 (그 그룹의 보스 찾음)
    if arr[member]==member:
        return member
    ret=findboss(arr[member])   #보스가 아니라면 arr배열의 값을 가지고 보스 찾기
    arr[member]=ret
    return ret


def union(a,b):
    fa=findboss(a)
    fb=findboss(b)
    if fa==fb:  # 두 보스가 같으면 이미 같은 그룹
        return

    # arr[fb]=fa  #보스가 다르면 a의 보스가 통합 장
    if rank[a]==rank[b]:
        rank[a]+=1
        arr[fb]=fa
    elif rank[a]>rank[b]:
        arr[fb]=fa
    else:
        arr[fa]=fb

union(0,1)
union(3,4)
union(1,4)
union(1,3)
union(5,4)

y,x=map(int,input().split())    #숫자 2개 입력 후 같은 그룹인지 출력
if findboss(y)==findboss(x):
    print("이미 같은 그룹")
else :
    print("다른 그룹")