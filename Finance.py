def recommend_investment(risk_tolerance, investment_horizon):

    if risk_tolerance == "low" and investment_horizon == "short-term":
       recommendation = "Savings Account or Bonds"
    elif risk_tolerance == "low" and investment_horizon == "medium-term":
        recommendation = "Savings Account or Bonds"
    elif risk_tolerance == "low" and investment_horizon == "long-term":
        recommendation = "Savings Account or Bonds"
    elif risk_tolerance == "medium" and investment_horizon == "short-term":
        recommendation = "Balanced Mutual Funds or ETFs"
    elif risk_tolerance == "medium" and investment_horizon == "medium-term":
        recommendation = "Balanced Mutual Funds or ETFs"
    elif risk_tolerance == "medium" and investment_horizon == "long-term":
        recommendation = "Balanced Mutual Funds or ETFs"
    elif risk_tolerance == "high" and investment_horizon == "short-term":
        recommendation = "Stocks or Equity Funds"
    elif risk_tolerance == "high" and investment_horizon == "medium-term":
        recommendation = "Stocks or Equity Funds"
    elif risk_tolerance == "high" and investment_horizon == "long-term":
        recommendation = "Stocks or Equity Funds"
    else:
        recommendation = "Please provide valid risk tolerance and investment horizon options."

    return recommendation

# implementation
risk_tolerance = input("Enter your risk tolerance (low, medium, or high): ")
investment_horizon = input("Enter your investment horizon (short-term, medium-term, or long-term): ")
recommendation = recommend_investment(risk_tolerance, investment_horizon)
print("Recommended investment:", recommendation)
