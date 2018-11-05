# -*- coding: utf-8 -*-


def QuickSort(arr,firstIndex,lastIndex):
    if firstIndex<lastIndex:
        divIndex = Partition(arr,firstIndex,lastIndex)

        print divIndex
        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr,divIndex+1,lastIndex)
    else:
        return

def Partition(arr,firstIndex,lastIndex):
    print arr
    i=firstIndex-1
    for j in range(firstIndex,lastIndex):
        if arr[j]<=arr[lastIndex]:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[lastIndex]=arr[lastIndex],arr[i+1]
    return i

arr=[1,4,7,1,5,5,3,85,34,75,23,75,2,0]

print("initial array:\n",arr)
QuickSort(arr,0,len(arr)-1)
print("result array:\n",arr)



def QuickSort(myList, start, end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中第i,j个元素相等
            myList[i] = myList[j]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]

        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base
        print myList

        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList


myList = [49,38,65,97,76,13,27,49]
print 'init array', myList
print("Quick Sort: ")
QuickSort(myList,0,len(myList)-1)
print(myList)

def hh():
    '''
    快速排序基本思想是：
    通过一趟排序将要排序的数据分割成独立的两部分，
    其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，
    整个排序过程可以递归进行，以此达到整个数据变成有序序列。

    如序列[6，8，1，4，3，9]，
    选择6作为基准数。
    从右向左扫描，寻找比基准数小的数字为3，交换6和3的位置，[3，8，1，4，6，9]，
    接着从左向右扫描，寻找比基准数大的数字为8，交换6和8的位置，[3，6，1，4，8，9]。
    重复上述过程，直到基准数左边的数字都比其小，右边的数字都比其大。
    然后分别对基准数左边和右边的序列递归进行上述方法
    '''
    return 'success'
