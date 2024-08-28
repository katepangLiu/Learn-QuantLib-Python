import QuantLib as ql

settlementDays = 2

# Holiday calendar of united states
calendar = ql.UnitedStates(ql.UnitedStates.Settlement)

forwardRate = 0.05

"""Day Counter provides methods for determining the length of a time period according to given market convention,
both as a number of days and as a year fraction."""
dayCounter = ql.Actual360()

# Construct flat forward rate term structure
flatForwardTermStructure = ql.FlatForward(settlementDays, calendar, forwardRate, dayCounter)

flatForwardTermStructure.referenceDate()

print("Max Date: ", flatForwardTermStructure.maxDate())