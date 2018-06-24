#1
1500
#2
1485
#3
def T(d):
	return(500 * d)

#4
def P(d):
	return (495 * d)
#5
def T(P(d)):
	return (T(d) - 5*d)



def jose_miles_traveled(days):
	return (500*days)

def cop_miles_traveled_from_jose(days):
	return (495*days)

def cop_miles_traveled_from_days(days):
	return(jose_miles_traveled(days)-5*days)


print(cop_miles_traveled_from_days(4))
