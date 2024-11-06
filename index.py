while True:
    try:
        length1 = int(input(" Please enter the length of your list: "))
        if length1 > 0:
            break
        else:
            print("Enter a positive integer.")
    except ValueError:
        print("That's not an integer!")

nums = []

for i in range(length1):
    while True:
        try:
            value = int(input(f"Enter a positive integer for element {i + 1}: "))
            if value > 0:
                nums.append(value)
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("That's not an integer!")

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

  
    print("Your list ranged :", end=" ")
    print(" ".join(map(str,evenValues))," ".join(map(str, oddValues)))
     


special_rearrangement(nums)