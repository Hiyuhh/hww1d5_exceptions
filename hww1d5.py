# 1. Exceptional Weather Forecast
# Task 1: Start
# Task 2: Temperature Conversion
# Task 3: User Experience
def temp():
    try:
        fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
    except ZeroDivisionError:
        print("Bruhh...")
    except OverflowError:
        print("Too.. many.. numbers.. about.. to.. break (T_T)")
    except ValueError:
        print("Umm..that is not a number. ")
    else:
        print(f"The converted temperature is: {celsius} ")
    finally:
        print(f"Thank you for using our amazing weather forecast application! (●'◡'●)")
temp()