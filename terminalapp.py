# terminal_app.py (CLI version of Financial Time Machine)

from logic import run_projection, get_recommendations
import locale
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Set locale for Indian currency formatting
try:
    locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')

def format_inr(amount):
    try:
        return locale.currency(amount, grouping=True)
    except:
        return f"₹{amount:,.2f}"

def main():
    print("\n💸 Financial Time Machine")
    print("Simulate your financial future. Enter your current details.\n")

    income = float(input("Enter Monthly Income (₹): ") or 30000)
    expenses = float(input("Enter Monthly Expenses (₹): ") or 20000)
    savings = float(input("Enter Current Savings (₹): ") or 50000)
    years = int(input("Enter Years to Simulate (1-30): ") or 10)

    print("\n🧪 What-If Scenarios")
    income_change = float(input("Income Growth Rate (%) [-50 to 200]: ") or 10)
    expense_change = float(input("Expense Growth Rate (%) [-50 to 200]: ") or 5)
    investment_return = float(input("Annual Investment Return (%) [0 to 20]: ") or 5)

    has_goal = input("\n🎯 Do you have a savings goal? (y/n): ").lower() == 'y'
    goal_amount = 0
    target_year = 0
    if has_goal:
        goal_amount = float(input("Enter your goal amount (₹): ") or 1000000)
        target_year = int(input(f"In how many years do you need it? (1 to {years}): ") or 5)

    projection = run_projection(
        income, expenses, savings, years,
        income_change, expense_change, investment_return
    )

    print("\n📈 Savings Projection:")
    for year, amt in enumerate(projection, 1):
        print(f"Year {year}: {format_inr(amt)}")

    if has_goal:
        print("\n🎯 Goal Analysis:")
        if target_year > years:
            print("⚠️ Your goal year is beyond the simulation range.")
        else:
            future = projection[target_year - 1]
            print(f"Goal: {format_inr(goal_amount)} | Projected: {format_inr(future)}")
            if future >= goal_amount:
                print("✅ On track! 🚀")
            else:
                gap = goal_amount - future
                print(f"❌ Short by {format_inr(gap)}. Increase savings or adjust goal.")

    try:
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, years + 1), projection, marker='o', color='green')
        plt.title("Projected Savings Over Time")
        plt.xlabel("Years from Now")
        plt.ylabel("Savings (₹)")
        plt.grid(True)
        ax = plt.gca()
        ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('₹{x:,.0f}'))
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Graph display failed:", e)

    print("\n💡 Recommendations:")
    tips = get_recommendations(income, expenses, savings)
    for t in tips:
        print(f"- {t}")

    print("\n⏳ Back in Time Simulation")
    past_monthly = float(input("Enter Past Monthly Investment (₹): ") or 5000)
    past_years = int(input("Years ago you could have started (1-30): ") or 5)
    past_return = float(input("Average Annual Return (%) [0-20]: ") or 8)

    months = past_years * 12
    rate = past_return / 100 / 12
    try:
        past_total = past_monthly * (((1 + rate) ** months - 1) / rate)
        print(f"💡 If you had invested {format_inr(past_monthly)}/mo for {past_years} years at {past_return}%, you'd have {format_inr(past_total)} today.")
    except:
        print("⚠️ Could not compute backward projection.")

if __name__ == "__main__":
    main()

