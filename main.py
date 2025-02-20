"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""
# Created running total function
def running_total():
    total = 0
    for i in range(5):
        number = int(input("Enter a number: "))
        total += number

    print("The running total is: " + str(total))

def main():
    running_total()
#Run main function for script
if __name__ == "__main__":
    main()