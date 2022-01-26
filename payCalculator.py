def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours: ")

    try:
        float(hrs)
        try:
            rate = input("Enter Rate: ")
            float(rate)
            if float(hrs) > 40 :
                ot_pay = (float(hrs)- 40) * (float(rate)*1.5)
                reg_pay = 40 * float(rate)
                pay = ot_pay + reg_pay
            else:
                pay = float(hrs) * float(rate)
            print ("Pay:", pay)
        except:
            print ("Error, Please enter numeric input")
    except:
        print("Error, Please enter numeric input")
        
        
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()