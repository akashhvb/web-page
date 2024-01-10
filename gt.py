month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
c_l= tuple(month)  
print(c_l)  
print(type(c_l))  
####################
def creating_gen(index):  
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
    yield months[index]  
    yield months[index+2]  
next_month = creating_gen(3)  
print(next(next_month), next(next_month))  
#####################################33
for  num in range(1,103):
    if all (num%i!=0 for i in range(2,num)):
        print(num)
###########################
global_var = 0  
def modify_global_var():  
    global global_var # Setting global_var as a global variable  
    global_var = 10  
def printing_global_var():  
    print(global_var) # There is no need to declare global variable  
modify_global_var()  
printing_global_var()
###########################################
l=[]  
for i in range(1,n+1):  
    element = int(input("Enter the element: "))  
    l.append(element)  
average = sum(l)/n  
print("Average of the elements in list",round(average,2)) 
