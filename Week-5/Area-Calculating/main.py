if __name__ == "__main__":
    import square_area
    import circle_area
    import rect_area
    import triangle_area

    

    def recall():
        area_calc = int(input('Please choice from one of the following: \n1. The area of a circle \n2. The area of a rectangle \n3. The area of a square \n4. The area of a Triangle \nEnter: '))

        if area_calc == 1:
            # Circle Area
            circle_area.calc()
            go_again()
        elif area_calc == 2:
            # Rectangle Area
            rect_area.calc()
            go_again()
        elif area_calc == 3:
            # Square Area
            square_area.calc()
            go_again()
        elif area_calc == 4:
            # Triangle Area
            triangle_area.calc()
            go_again()
        else:
            print('Invalid option.')
            recall()

    def go_again():
        again = input('Would you like to calculate again? ')
        if again == "yes":
            recall()
        elif again == "no":
            print("Exiting. . .")
            exit
        else:
            print('Please enter yes or no.')
            go_again()
    
    
    recall()

    