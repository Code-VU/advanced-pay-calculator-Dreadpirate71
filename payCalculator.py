def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    try:
        float(hrs)
    except:
        print("Error Please enter a number")
        quit()
    rate = input("Enter Rate: ")
    try:
        float(rate)
    except:
        print ("Error Please enter a number")
        quit()
    if float(hrs) > 40 :
        pay = 40 * float(rate) + (float(hrs)- 40) * (float(rate)*1.5)
    else:
        pay = float(hrs) * float(rate)
    print ("Pay:", pay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()