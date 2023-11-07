if __name__ == '__main__':
    import fah_to_cel as ftoc
    tempratures = []
    
    def recall():
        temp = float(input('Please enter a temprature: '))
        f_or_c = int(input('Is the temprature Fahreinheit or Celcius? \n1. FahreinHeit \n2. Celcius \nEnter: '))
        
        if f_or_c == 1:
            tempratures.append(ftoc.conv(temp))
            again()
        elif f_or_c == 2:
            tempratures.append(temp)
            again()
        else:
            print('Error, invalid option.')
            
    

    def again():
        option = input('Would you like to enter another temprature? ')
        if option == "y":
            recall()
        elif option == "n":
            print(tempratures)
            print(f'Highest temprature:', max(tempratures), '\nLowest Temprature', min(tempratures), '\nAverage Temprature: ', (sum(tempratures)/len(tempratures)))
        else:
            print('Please enter y or n.')
            again()

    recall()
    