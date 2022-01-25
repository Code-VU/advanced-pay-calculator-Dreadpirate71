def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    #try:
       # float(hrs)
    #except:
       # print("Error, Please enter numeric input")
       # quit()
    rate = input("Enter Rate: ")
   # try:
      #  float(rate)
   # except:
       # print ("Error, Please enter numeric input")
        #quit()
    if float(hrs) > 40 :
        ot_pay = (float(hrs)- 40) * (float(rate)*1.5)
        reg_pay = float(40*float(rate))
        pay = ot_pay + reg_pay
    else:
        pay = float(hrs) * float(rate)
    print ("Pay:", pay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()