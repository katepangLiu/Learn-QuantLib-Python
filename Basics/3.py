import QuantLib as ql

today = ql.Date(15,6,2020)
ql.Settings.instance().evaluationDate = today

effectiveDate = ql.Date(15, 6, 2020)
terminationDate = ql.Date(15, 6, 2022)

schedule = ql.MakeSchedule(effectiveDate, terminationDate, ql.Period('6M'))
dayCounter = ql.Actual360()
notional = [100.0]
rate = [0.05]

leg = ql.FixedRateLeg(schedule, dayCounter, notional, rate)
interestRate = ql.InterestRate(0.05, dayCounter, ql.Compounded, ql.Annual)
ql.Settings.instance().evaluationDate = ql.Date(15,12,2020)
print( ql.CashFlows.npv(leg, interestRate, False) )
