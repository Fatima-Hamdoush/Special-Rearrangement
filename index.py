length1 = int(input("enter the length  of  your list  :"))
nums=[]
for i in range(length1):
       values= int(input("enter the number "))
       nums.append(values)
oddValues=[]
evenValues=[]

def  special_rearrangement(nums):

    for i in range(length1 ):
       
        if(nums[i]%2 != 0 ):
           oddValues.append(nums[i]) 
        else:
            evenValues.append(nums[i])
    
        for i in range(len(oddValues)-1):
          if(oddValues[i] > oddValues[i+1]):
            temp = oddValues[i]
            oddValues[i] = oddValues[i+1]
            oddValues[i+1] = temp
           
        for i in range(len(evenValues)-1):
          if(evenValues[i]>=evenValues[i+1]):
            temp2 = evenValues[i]
            evenValues[i] = evenValues[i+1]
            evenValues[i+1] = temp2

  
      
    print(" ".join(map(str,evenValues))," ".join(map(str, oddValues)))
     


special_rearrangement(nums)