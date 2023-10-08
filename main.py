import time

print("Welcome back to Python")
#test function that multiplies the first param by the second and returns the product
def mult(num,num2):
    var = num
    var2 = num2
    return num*num2
result = mult(1,2)
print(result)

#Test out a while loop
i = 0
while i<10:
  
    result+=1
    #test out the time.sleep function
    time.sleep(0.5)
    print(result+1)
    i+=1
