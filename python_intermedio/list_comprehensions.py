def main():
    
    #squares = []
    #for i in range (1,11):
    #    if i % 3 !=0:
    #        squares.append(i**2)
    #
#
    #print(squares)

    #squares = [i**2 for i in range(1,101) if i % 3 != 0]
    #print(squares)


    # RETO multiplo de 4,6 y 9 
    squares = [ i for i in range(1, 100000) if i % 36 == 0]
    print(squares)


if __name__ == "__main__":
    main()