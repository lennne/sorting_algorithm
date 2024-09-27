"""
1. input array
2. input startcount as first index of array
3. input endcount as last index of array
4. calculate the middle position using (p+r)/2
5. input middlePosition as middle position of array
6. if the size of array isn't 1 go back to 
"""

def mergeSort(myArray):
    if(int(myArray.__len__())  == 1):
        print("the length of this array is myArray", myArray)
        return myArray
    lastindex = myArray.__len__()
    # if(myArray.__len__() == 3):
    #     print("last index", lastindex)
    endcount = int(lastindex)
    middlePosition = int(endcount/2 )
    print("middle Position: ", middlePosition)
    print("splitting array....")
    leftArray = myArray[0:middlePosition]
    rightArray = myArray[middlePosition:endcount]
    print("first array before mergeSort: ", leftArray)
    print("second array before mergeSort: ", rightArray)
    leftArray = mergeSort(leftArray)
    rightArray = mergeSort(rightArray)
    print("first array after mergeSort: ", leftArray)
    print("second array after mergeSort: ", rightArray)
    sortedArray =  sortArrays(leftArray, rightArray)
    print("do you work", sortedArray)
    return sortedArray
    
    
def sortArrays(firstArray, secondArray):
    firstpointer = 0
    secondpointer = 0
    sortedArray = []
    lengthOfArray = int(firstArray.__len__())
    lengthOfSecondArray = int(secondArray.__len__())
    print(firstpointer < lengthOfArray)
    while (firstpointer < lengthOfArray and secondpointer < lengthOfSecondArray):
        print("first pointer ",firstpointer, "|| second pointer ", secondpointer)
        if firstArray[firstpointer] > secondArray[secondpointer]:
            print("what is this", secondArray[secondpointer])
            sortedArray.append(secondArray[secondpointer])
            
            if(secondpointer + 1 == lengthOfSecondArray):
               print("i entered madeam")
               sortedArray.extend(firstArray[firstpointer:lengthOfArray])
     
            secondpointer += 1
        else:
            #shows that first number is < than second number so insert first number into the sorted array and move one step
            #in the first array
            print("i came here", firstArray[firstpointer])

            sortedArray.append(firstArray[firstpointer])
            if(firstpointer + 1 == lengthOfArray):
                print("did you enter")
                myarray = secondArray[secondpointer:lengthOfSecondArray]
        
                sortedArray.extend(myarray)
                
           
            firstpointer += 1
        print("the first array: ",firstArray," ", "the second array: ", secondArray)
        print("the sorted array: ",sortedArray)

    return sortedArray


mergeSort([20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])
#mergeSort([2,5,6,1,3,7])
#sortArrays((20, 19, 18, 17, 16, 15),(14, 13, 12, 11, 10, 9))