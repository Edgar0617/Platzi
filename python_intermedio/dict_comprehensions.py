import math
def run():
    
    #my_dict = {}
    #for i in range(1,101):
    #    if i % 3 != 0:
    #        my_dict[i]=i**3

    #my_dict={i : i for i in range(1,1001)if i % 3 != 0}
    #print(my_dict)

    # RETO

    my_dict={i:round(i**(1/2),2)for i in range (1,1001)}
    print(my_dict)




if __name__ == "__main__":
    run()