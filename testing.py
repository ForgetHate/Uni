if __name__ == "__main__":
    def recall():
        area_calc = input(int('Please choice from one of the following: \n1. The area of a circle \n2. The area of a rectangle \n3. The area of a square \n4. The area of a Triangle \nEnter: '))

        if area_calc == "1":
            # Circle Area
            print('1')
        elif area_calc == "2":
            # Rectangle Area
            print('2')
        elif area_calc == "3":
            # Square Area
            print('3')
        elif area_calc == "4":
            # Triangle Area
            print('4')
        else:
            recall()
    
    
    recall()

    
