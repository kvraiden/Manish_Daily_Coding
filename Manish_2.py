# K_Flynn
#Time_Complexity O[n^2]
#As of i am learning I have used naive approach and not used inbuilt function ofcourse there are oneliners too!!
def make_arr():
    arr_lnth = int(input("Enter the array length : "))
    tmp = []
    for x in range(arr_lnth):#will run for n cases
        tmp.append(input())
    min_ele, max_ele = tmp[0], tmp[0]
    for b in range(1, len(tmp)):#will run for upto n cases(list length)
        if tmp[b] < min_ele:
            min_ele = tmp[b]
        if tmp[b] > max_ele:
            max_ele = tmp[b]
    print('Minimum Element in the list', tmp, 'is', min_ele)
    print('Maximum Element in the list', tmp, 'is', max_ele)
    return tmp


tst = int(input("Enter the number of arrays : "))
for a in range(tst):
    print(make_arr())
