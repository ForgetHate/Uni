if __name__ == '__main__':
    # import fah_to_cel
    tempratures = []
    
    def recall():
        temp = float(input('Please enter a temprature: '))
        f_or_c = int(input('Is the temprature Fahreinheit or Celcius? \n1. FahreinHeit \n2. Celcius \nEnter: '))
        
        if f_or_c == 1:
            temp = (temp - 32) * 5/9
            tempratures.append(temp)
            again()
        elif f_or_c == 2:
            tempratures.append(temp)
            again()
        else:
            print('Error, invalid option.')
            
    

    def again():
        option = input('Would you like to enter another temprature? ')
        if option == "yes":
            recall()
        elif option == "no":
            print(tempratures)
            print(f'Highest temprature:', max(tempratures), '\nLowest Temprature', min(tempratures))
        else:
            print('Please enter yes or no.')
            again()

    recall()
    