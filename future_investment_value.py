def future_investment_value(investment_amount, monthly_interestRate,years):
	numberOfMonths = years / 12
	future_investment_value = investment_amount*(1+monthly_interestRate)**numberOfMonths
	return future_investment_value
print(future_investment_value
(100, 0.6, 1))