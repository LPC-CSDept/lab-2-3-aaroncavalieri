def main():
    ##################################################
    
    val1 = 100
    val2 = 90
    val3 = 110
    
    """
    val1 = input(("Value 1: "))
    val2 = input(("Value 2: "))
    val3 = input(("Value 3: "))
    """
    
    sum = int(val1) + int(val2) + int(val3) #added int incase input field is used
    avg = sum / 3 
    

    
    print ("Values: {0:2d} {1:3d} {2:4d}" .format(val1, val2, val3))
    print ("Total:  \t {0:.0f} ".format(sum))
    print ("Average: \t {0:.2f} ".format(avg)) #\t means skip over next horizontal tab.{0:}.2f} 0 means 1st position and .2f means two decimal places.

    ##################################################

    pass


if __name__ == '__main__':
    main()
