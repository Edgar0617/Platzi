from functools import reduce
def run():
    """LIST COMPREHENSIONS"""
    #impar = [i for i in range (1,101) if i % 2 == 0]
    #print(impar)
    #

    #square = [i**2 for i in range(1,11) ]
    #print(square)
    #

    #my_list = [2,2,2,2,2]
    #all_multiplied = 1
    #for i in my_list:
    #    all_multiplied = all_multiplied*i
    #print(all_multiplied)

    """FUNCTION IMPORT"""
    #my_list = [1,4,5,6,9,13,19,21]
    #impar = [list(filter(lambda i:i % 2 !=0,my_list))]
    #print(impar)
    
    #my_list = [1,4,5,6,9,13,19,21]
    #par = [list(filter(lambda i:i % 2 ==0,my_list))]
    #print(par)

    """FUNCTION MAP"""
    
    #my_list = [1,2,3,4,5]
    #square = [list(map(lambda i:i**2, my_list))]
    #print(square)

    """FUNCTION REDUCE"""
    
    my_list = [2,2,2,2,2]
    all_multiplied = reduce(lambda a,b : a*b, my_list)
    print(all_multiplied)
    

if __name__ == "__main__":
    run()