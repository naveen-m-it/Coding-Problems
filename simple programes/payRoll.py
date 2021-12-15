
"""  Hello! This is Naveen                 """
"""  https://www.github.com/naveen-m-it    """

def main(input):
    file_name = input
    #throw try method
    try:
        """here is read text method"""
        #open a file using file name and location
        file = open(file_name,"rt")
        # reading a file line by line
        read = file.readlines()
        file.close()
        en="Employee Name"
        hw = "Hourly Wage"
        wp = "Wage Paid"
        print("="*44)
        print("|  %-13s"%en,"| %-11s"%hw,"| %-10s|"%wp)
        print("="*44)
        count=0
        for line in read:
            lines=line.split()
            print("|  %-13s"%lines[0],"|%11s$"%lines[1],"|%9s$ |"%lines[2])
            print("-"*44)
            count+=1
        print("Total Employees:",count)
        print("-"*44)
    except IOError or SyntaxError as e:
        print("Error:",e)
if __name__=="__main__":
    """here input a file location and name of the file"""
    input = (input(r"Enter text file name with location: "))
    main(str(input))