import sys
sys.stdin = open("sample_input.txt","r")

# 병합정렬 할건데
# .sort() 쓴건지 병합정렬 쓴건지 어떻게 아냐?
# 병합 할 때 확인
# 병합 : 정렬된 2개 합치기
# [1,4,5]   [3,6,7]     >>  [1,3,4,5,6,7]

def merge_sort(arr):
    global cnt
    # 전체를 정렬하기 위해서
    # 각 절반을 각각 정렬
    # 병합
    L=len(arr)
    if L == 1:
        return arr
    left=arr[:L//2]
    right=arr[L//2:L]
    left = merge_sort(left)
    right = merge_sort(right)
    if left[-1]>right[-1]:
        cnt+=1

    # 병합
    merged_arr = []
    while left and right :  # 왼쪽 오른쪽 배열에 값이 둘다 남아 있을 때,
        # 각각 정렬되어 있으니까.. 제일 왼쪽(0번)끼리 비교
        if left[0]<right[0]:
            merged_arr.append(left.pop(0))
        else:
            merged_arr.append(right.pop(0))
    # 왼쪽, 오른쪽 두 배열중 한 배열은 남아있는 상태!
    while left:
        merged_arr.append(left.pop(0))
    while right:
        merged_arr.append(right.pop(0))
    return merged_arr


def merge_sort2(start, end):
    global cnt
    if start==end:
        return
    mid = (start+end-1)//2
    merge_sort2(start,mid)
    merge_sort2(mid+1,end)
    if arr[mid] > arr[end]:
        cnt+=1

    i=start
    j=mid+1
    tmp_arr=[]
    while i <=mid and j<= end:
        if arr[i]<arr[j]:
            tmp_arr.append(arr[i])
            i+=1
        else:
            tmp_arr.append(arr[j])
            j+=1

    # 남아있는 요소 붙이기
    while i <= mid:
        tmp_arr.append(arr[i])
        i+=1
    while j <=end:
        tmp_arr.append(arr[j])
        j+=1

    for i in range(len(tmp_arr)):
        arr[start+i]=tmp_arr[i]





T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    cnt=0   #병합시에 왼쪽 배열의 마지막 값이 더 큰 경우
    # arr = merge_sort(arr)
    merge_sort2(0,N-1)
    print(f"#{tc} {arr[N//2]} {cnt}")