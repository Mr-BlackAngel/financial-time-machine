# logic.py

def run_projection(income, expenses, savings, years, income_growth, expense_growth, investment_return):
    projection = []
    for year in range(years):
        income *= 1 + (income_growth / 100)
        expenses *= 1 + (expense_growth / 100)
        savings += income - expenses
        savings *= 1 + (investment_return / 100)
        projection.append(round(savings, 2))
    return projection

def get_recommendations(income, expenses, savings):
    tips = []
    if expenses > 0.8 * income:
        tips.append("⚠️ You're spending over 80% of your income. Try to reduce unnecessary expenses.")
    if savings < 3 * expenses:
        tips.append("💡 Build an emergency fund with at least 3 months of expenses.")
    if income - expenses <= 0:
        tips.append("🚨 Your expenses exceed income. Consider cutting costs or boosting income.")
    else:
        tips.append("👍 You're saving well! Consider investing more for long-term growth.")
    return tips

