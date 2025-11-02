from decimal import Decimal, getcontext

# Set the precision to 30 decimal places (plus one for the '3.')
getcontext().prec = 31 

pi_decimal = Decimal('3.141592653589793238462643383279') # A known value of Pi for demonstration
print(pi_decimal)