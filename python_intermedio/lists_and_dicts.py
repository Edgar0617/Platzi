def main():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname":"Edgar", "lastname":"Rosales"}

    super_list = [
        {"firstname":"Edgar", "lastname":"Rosales"},
        {"firstname":"Gabriela", "lastname":"Burbano"},
        {"firstname":"Wilmer", "lastname":"Rosales"},
        {"firstname":"Keyla", "lastname":"Meneses"},
        {"firstname":"Danna", "lastname":"Rosales"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1, 2.4, 6.0, 3.1]
    }


    for key,value in super_dict.items():
        print(key, ".", value)
    
    for i in super_list:
        print(i["firstname"], "-", i["lastname"])
    
    print(my_list,my_dict)

if __name__ == '__main__':
    main()