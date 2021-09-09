"""

Hello!, This is Naveen
https://www.github.com/naveen-m-it

"""
# function for find TotalWeeklyPay
def TotalWeeklyPay(HourlyWage,TotalRegularHours,TotalOverTimeHours):
    hw = HourlyWage
    trh = TotalRegularHours
    toth = TotalOverTimeHours
    #over time pay as otp
    otp = toth*(1.5*hw)
    #total weekly pay as twp
    twp = hw*trh+otp
    #display total weekly pay
    print("Total Weekly Pay: $%.2f"%twp)
   
# main method
if __name__=="__main__":
    hw = int(input("Hourly Wage: "))
    trh = int(input("Total Regular Hours: "))
    toth = int(input("Total Over Time Hours: "))
    TotalWeeklyPay(hw,trh,toth)