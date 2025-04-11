# # app.py

# from logic import run_projection, get_recommendations
# import locale
# import matplotlib.pyplot as plt
# import matplotlib.ticker as mtick


# # Set locale for Indian currency formatting
# try:
#     locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
# except:
#     locale.setlocale(locale.LC_ALL, '')  # fallback if above fails

# def format_inr(amount):
#     try:
#         return locale.currency(amount, grouping=True)
#     except:
#         # fallback formatting
#         return f"₹{amount:,.2f}"

# def main():
#     print("\n💸 Financial Time Machine")
#     print("See your financial future in real-time. Enter your current info and simulate outcomes.\n")

#     # User Inputs
#     income = float(input("Enter Monthly Income (₹): ") or 30000)
#     expenses = float(input("Enter Monthly Expenses (₹): ") or 20000)
#     savings = float(input("Enter Current Savings (₹): ") or 50000)
#     years = int(input("Enter Years to Simulate (1-30): ") or 10)

#     print("\n🧪 What-If Scenarios")
#     income_change = float(input("Income Growth Rate (%) [-50 to 200]: ") or 10)
#     expense_change = float(input("Expense Growth Rate (%) [-50 to 200]: ") or 5)
#     investment_return = float(input("Annual Investment Return (%) [0 to 20]: ") or 5)
#     print("\n🎯 Goal Tracker")
#     has_goal = input("Do you have a savings goal? (y/n): ").lower() == 'y'
#     goal_amount = 0
#     target_year = 0

#     if has_goal:
#         goal_amount = float(input("Enter your goal amount (₹): ") or 1000000)
#         target_year = int(input(f"In how many years do you need it? (1 to {years}): ") or 10)

#     # Run projection
#     projection = run_projection(
#         income, expenses, savings, years, income_change, expense_change, investment_return
#     )

#     # Display projection
#     print("\n📈 Savings Projection Over Time:")
#     for year, amount in enumerate(projection, start=1):
#         print(f"Year {year}: {format_inr(amount)}")
#     # Check if user can meet their goal
#     if has_goal:
#         if target_year > years:
#             print(f"\n⚠️ Goal year ({target_year}) exceeds simulation length ({years}). Extend the simulation.")
#         else:
#             final_amount = projection[target_year - 1]
#             print(f"\n🎯 Goal Check (Year {target_year}):")
#             print(f"Goal: {format_inr(goal_amount)}")
#             print(f"Projected Savings: {format_inr(final_amount)}")
#             if final_amount >= goal_amount:
#                 print("✅ You're on track to meet your goal! 🚀")
#             else:
#                 gap = goal_amount - final_amount
#                 print(f"❌ You may fall short by {format_inr(gap)}. Consider adjusting savings or timeline.")
#     # After savings projection print loop:
#     print("\n🧠 Smart Financial Suggestions:")
#     for tip in get_recommendations(income, expenses, savings):
#         print(f"- {tip}")

#     try:
#         years_list = list(range(1, years + 1))
#         plt.figure(figsize=(10, 5))
#         plt.plot(years_list, projection, marker='o', color='green')
#         plt.title("Savings Projection Over Time (INR)")
#         plt.xlabel("Years from Now")
#         plt.ylabel("Projected Savings (₹)")
#         ax = plt.gca()
#         ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('₹{x:,.0f}'))
#         plt.grid(True)
#         plt.tight_layout()
#         plt.show()
#         plt.close()
#     except Exception as e:
#         print(f"Visualization failed: {e}")

#     # 🔙 Backward Simulation
#     print("\n⏳ Back in Time: What if you had started earlier?")
#     past_monthly = float(input("Enter past monthly investment amount (₹): ") or 5000)
#     past_years = int(input("How many years ago could you have started? (1-30): ") or 5)
#     past_return = float(input("What average annual return (%)? [0-20]: ") or 8)

#     months = past_years * 12
#     rate = past_return / 100 / 12
#     try:
#         future_value = past_monthly * (((1 + rate) ** months - 1) / rate)
#         print(f"💡 If you had invested {format_inr(past_monthly)}/mo for {past_years} years at {past_return}%, you'd have {format_inr(future_value)} today.")
#     except:
#         print("⚠️ Could not compute backward projection.")


# if __name__ == "__main__":
#     main()

# import streamlit as st
# import matplotlib.pyplot as plt
# import matplotlib.ticker as mtick
# from logic import run_projection, get_recommendations

# # INR formatter
# def format_inr(amount):
#     try:
#         return f"₹{amount:,.2f}"
#     except:
#         return f"₹{amount}"

# st.set_page_config(page_title="Financial Time Machine", layout="centered")
# st.title("💸 Financial Time Machine")
# st.markdown("Visualize alternate financial futures and make smarter money decisions.")

# # Sidebar Inputs
# st.sidebar.header("Your Financial Info")
# income = st.sidebar.number_input("Monthly Income (₹)", min_value=0, value=30000)
# expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0, value=20000)
# savings = st.sidebar.number_input("Current Savings (₹)", min_value=0, value=50000)
# years = st.sidebar.slider("Years to Simulate", 1, 30, 10)

# st.sidebar.header("Growth Rates")
# income_change = st.sidebar.slider("Income Growth Rate (%)", -50.0, 200.0, 10.0)
# expense_change = st.sidebar.slider("Expense Growth Rate (%)", -50.0, 200.0, 5.0)
# investment_return = st.sidebar.slider("Annual Investment Return (%)", 0.0, 20.0, 5.0)

# st.sidebar.header("Goal Tracking")
# has_goal = st.sidebar.checkbox("Track a Savings Goal")

# if has_goal:
#     goal_amount = st.sidebar.number_input("Goal Amount (₹)", min_value=0, value=1000000)
#     target_year = st.sidebar.slider("Years until Goal", 1, years, 5)
# else:
#     goal_amount = 0
#     target_year = 0

# # Projection
# projection = run_projection(
#     income, expenses, savings, years, income_change, expense_change, investment_return
# )

# # Output Section
# st.subheader("📈 Savings Projection Over Time")
# st.write("Projected savings after each year based on your inputs.")
# for year, amount in enumerate(projection, start=1):
#     st.write(f"Year {year}: {format_inr(amount)}")

# # Goal Analysis
# if has_goal:
#     st.subheader("🎯 Goal Analysis")
#     if target_year <= years:
#         final_amount = projection[target_year - 1]
#         st.write(f"**Goal Amount:** {format_inr(goal_amount)}")
#         st.write(f"**Projected Savings in Year {target_year}:** {format_inr(final_amount)}")
#         if final_amount >= goal_amount:
#             st.success("✅ You're on track to meet your goal!")
#         else:
#             st.error(f"❌ Shortfall: {format_inr(goal_amount - final_amount)}. Consider increasing savings or timeline.")
#     else:
#         st.warning("⚠️ Goal year exceeds simulation period.")

# # Graph
# st.subheader("📊 Savings Growth Visualization")
# fig, ax = plt.subplots(figsize=(10, 4))
# years_list = list(range(1, years + 1))
# ax.plot(years_list, projection, marker='o', color='green')
# ax.set_title("Savings Projection (INR)")
# ax.set_xlabel("Years")
# ax.set_ylabel("Projected Savings")
# ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('₹{x:,.0f}'))
# ax.grid(True)
# st.pyplot(fig)

# # Backward Simulation
# st.subheader("⏳ Back in Time")
# st.markdown("What if you had started investing earlier?")
# past_monthly = st.number_input("Past Monthly Investment (₹)", min_value=0, value=5000)
# past_years = st.slider("Years Ago You Could Have Started", 1, 30, 5)
# past_return = st.slider("Average Annual Return (%)", 0.0, 20.0, 8.0)

# months = past_years * 12
# rate = past_return / 100 / 12
# try:
#     future_value = past_monthly * (((1 + rate) ** months - 1) / rate)
#     st.info(f"💡 You'd have {format_inr(future_value)} today if you invested {format_inr(past_monthly)}/mo for {past_years} years at {past_return}%.")
# except:
#     st.error("Could not compute backward projection.")

# # Recommendations
# st.subheader("💡 Personalized Financial Tips")
# for tip in get_recommendations(income, expenses, savings):
#     st.write(tip)


# app.py (Final Streamlit Version with Full UX Improvements)

# app.py (Final Streamlit Version with Sidebar Navigation Layout)

# import streamlit as st
# import matplotlib.pyplot as plt
# import matplotlib.ticker as mtick
# from logic import run_projection, get_recommendations

# # Currency formatter
# def format_inr(amount):
#     try:
#         return f"₹{amount:,.2f}"
#     except:
#         return f"₹{amount:.2f}"

# st.set_page_config(page_title="💸 Financial Time Machine", layout="wide")
# st.title(":money_with_wings: Financial Time Machine")
# st.caption("Visualize your financial future. Compare savings, goals, and past what-ifs.")

# menu = st.sidebar.radio("Navigation", ["Financial Inputs", "Projections & Chart", "Goal Tracker", "Recommendations", "Backward Simulation"])

# if "submitted" not in st.session_state:
#     st.session_state.submitted = False

# if menu == "Financial Inputs":
#     st.header("🔢 Financial Inputs")
#     with st.form("inputs_form"):
#         income = st.number_input("Monthly Income (₹)", min_value=0, value=30000)
#         expenses = st.number_input("Monthly Expenses (₹)", min_value=0, value=20000)
#         savings = st.number_input("Current Savings (₹)", min_value=0, value=50000)
#         years = st.slider("Years to Simulate", min_value=1, max_value=30, value=10)

#         st.header("🧪 What-If Scenarios")
#         income_change = st.slider("Income Growth Rate (%)", min_value=-50, max_value=200, value=10)
#         expense_change = st.slider("Expense Growth Rate (%)", min_value=-50, max_value=200, value=5)
#         investment_return = st.slider("Annual Investment Return (%)", min_value=0, max_value=20, value=5)

#         st.session_state.has_goal = st.checkbox("I have a savings goal")
#         if st.session_state.has_goal:
#             st.session_state.goal_amount = st.number_input("Goal Amount (₹)", min_value=0, value=1000000)
#             st.session_state.target_year = st.slider("Target Year to Reach Goal", min_value=1, max_value=30, value=5)

#         if st.form_submit_button("Run Simulation"):
#             st.session_state.projection = run_projection(
#                 income, expenses, savings, years, income_change, expense_change, investment_return
#             )
#             st.session_state.inputs = (income, expenses, savings, years)
#             st.session_state.years = years
#             st.session_state.submitted = True

# if menu == "Projections & Chart":
#     if st.session_state.submitted:
#         st.subheader("📈 Projected Savings Over Time")
#         st.dataframe({"Year": list(range(1, st.session_state.years + 1)), "Savings (₹)": st.session_state.projection})

#         fig, ax = plt.subplots(figsize=(10, 5))
#         ax.plot(range(1, st.session_state.years + 1), st.session_state.projection, marker='o', color='green')
#         ax.set_title("Savings Projection Over Time (INR)")
#         ax.set_xlabel("Years from Now")
#         ax.set_ylabel("Projected Savings (₹)")
#         ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('₹{x:,.0f}'))
#         ax.grid(True)
#         st.pyplot(fig)
#     else:
#         st.warning("Please enter your inputs in the 'Financial Inputs' section first.")

# if menu == "Goal Tracker":
#     if st.session_state.submitted and st.session_state.has_goal:
#         st.subheader("🌟 Goal Check")
#         if st.session_state.target_year > st.session_state.years:
#             st.warning("Goal year exceeds simulation length. Extend the simulation.")
#         else:
#             final_amount = st.session_state.projection[st.session_state.target_year - 1]
#             st.markdown(f"**Goal:** {format_inr(st.session_state.goal_amount)}")
#             st.markdown(f"**Projected Savings in Year {st.session_state.target_year}:** {format_inr(final_amount)}")
#             if final_amount >= st.session_state.goal_amount:
#                 st.success("✅ You're on track to meet your goal! 🚀")
#             else:
#                 gap = st.session_state.goal_amount - final_amount
#                 st.error(f"❌ You may fall short by {format_inr(gap)}. Consider adjusting savings or timeline.")
#     else:
#         st.info("Enable and configure your savings goal in the 'Financial Inputs' section.")

# if menu == "Recommendations":
#     if st.session_state.submitted:
#         income, expenses, savings, _ = st.session_state.inputs
#         st.subheader("💡 Recommendations")
#         for tip in get_recommendations(income, expenses, savings):
#             st.markdown(f"- {tip}")
#     else:
#         st.warning("Please run the simulation first from 'Financial Inputs'.")

# if menu == "Backward Simulation":
#     st.subheader("⏳ Back in Time: What if you had started earlier?")
#     with st.expander("Try Backward Simulation"):
#         past_monthly = st.number_input("Past Monthly Investment (₹)", value=5000)
#         past_years = st.slider("Years Ago You Could've Started", min_value=1, max_value=30, value=5)
#         past_return = st.slider("Average Annual Return (%)", min_value=0, max_value=20, value=8)

#         months = past_years * 12
#         rate = past_return / 100 / 12
#         try:
#             future_value = past_monthly * (((1 + rate) ** months - 1) / rate)
#             st.success(f"💡 If you had invested {format_inr(past_monthly)}/mo for {past_years} years at {past_return}%, you'd have {format_inr(future_value)} today.")
#         except:
#             st.error("⚠️ Could not compute backward projection.")

# app.py (Final Streamlit Version with Sidebar Navigation Layout + Improved Icons)

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from logic import run_projection, get_recommendations

# Currency formatter
def format_inr(amount):
    try:
        return f"₹{amount:,.2f}"
    except:
        return f"₹{amount:.2f}"

st.set_page_config(page_title="💸 Financial Time Machine", layout="wide")
st.markdown("""
    <style>
        .element-container:has(label[for="Navigation"]) label {
            font-size: 1.25rem !important;
        }
        .st-emotion-cache-6qob1r:hover {
            background-color: #f0f2f6;
        }
        section[tabindex="-1"] > div:first-child {
            padding-top: 0rem;
        }
        .st-emotion-cache-1v0mbdj svg {
            height: 24px;
            width: 24px;
        }
    </style>
""", unsafe_allow_html=True)

st.title(":money_with_wings: Financial Time Machine")
st.caption("Visualize your financial future. Compare savings, goals, and past what-ifs.")

menu = st.sidebar.radio("📁 Navigation", ["🏠 Financial Inputs", "📊 Projections & Chart", "🌟 Goal Tracker", "💡 Recommendations", "⏳ Backward Simulation"])

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if menu == "🏠 Financial Inputs":
    st.header("🔢 Financial Inputs")
    with st.form("inputs_form"):
        income = st.number_input("Monthly Income (₹)", min_value=0, value=30000)
        expenses = st.number_input("Monthly Expenses (₹)", min_value=0, value=20000)
        savings = st.number_input("Current Savings (₹)", min_value=0, value=50000)
        years = st.slider("Years to Simulate", min_value=1, max_value=30, value=10)

        st.header("🧪 What-If Scenarios")
        income_change = st.slider("Income Growth Rate (%)", min_value=-50, max_value=200, value=10)
        expense_change = st.slider("Expense Growth Rate (%)", min_value=-50, max_value=200, value=5)
        investment_return = st.slider("Annual Investment Return (%)", min_value=0, max_value=20, value=5)

        st.session_state.has_goal = st.checkbox("I have a savings goal")
        if st.session_state.has_goal:
            st.session_state.goal_amount = st.number_input("Goal Amount (₹)", min_value=0, value=1000000)
            st.session_state.target_year = st.slider("Target Year to Reach Goal", min_value=1, max_value=30, value=5)

        if st.form_submit_button("Run Simulation"):
            st.session_state.projection = run_projection(
                income, expenses, savings, years, income_change, expense_change, investment_return
            )
            st.session_state.inputs = (income, expenses, savings, years)
            st.session_state.years = years
            st.session_state.submitted = True

if menu == "📊 Projections & Chart":
    if st.session_state.submitted:
        st.subheader("📈 Projected Savings Over Time")
        st.dataframe({"Year": list(range(1, st.session_state.years + 1)), "Savings (₹)": st.session_state.projection})

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(range(1, st.session_state.years + 1), st.session_state.projection, marker='o', color='green')
        ax.set_title("Savings Projection Over Time (INR)")
        ax.set_xlabel("Years from Now")
        ax.set_ylabel("Projected Savings (₹)")
        ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('₹{x:,.0f}'))
        ax.grid(True)
        st.pyplot(fig)
    else:
        st.warning("You need to enter your financial details first.")
        if st.button("➡️ Enter values and run simulation"):
            st.experimental_set_query_params(menu="🏠 Financial Inputs")
            st.rerun()

if menu == "🌟 Goal Tracker":
    if st.session_state.submitted and st.session_state.has_goal:
        st.subheader("🌟 Goal Check")
        if st.session_state.target_year > st.session_state.years:
            st.warning("Goal year exceeds simulation length. Extend the simulation.")
        else:
            final_amount = st.session_state.projection[st.session_state.target_year - 1]
            st.markdown(f"**Goal:** {format_inr(st.session_state.goal_amount)}")
            st.markdown(f"**Projected Savings in Year {st.session_state.target_year}:** {format_inr(final_amount)}")
            if final_amount >= st.session_state.goal_amount:
                st.success("✅ You're on track to meet your goal! 🚀")
            else:
                gap = st.session_state.goal_amount - final_amount
                st.error(f"❌ You may fall short by {format_inr(gap)}. Consider adjusting savings or timeline.")
    else:
        st.info("Enable and configure your savings goal in the 'Financial Inputs' section.")

if menu == "💡 Recommendations":
    if st.session_state.submitted:
        income, expenses, savings, _ = st.session_state.inputs
        st.subheader("💡 Recommendations")
        for tip in get_recommendations(income, expenses, savings):
            st.markdown(f"- {tip}")
    else:
        st.warning("Please run the simulation first from 'Financial Inputs'.")

if menu == "⏳ Backward Simulation":
    st.subheader("⏳ Back in Time: What if you had started earlier?")
    with st.expander("Try Backward Simulation"):
        past_monthly = st.number_input("Past Monthly Investment (₹)", value=5000)
        past_years = st.slider("Years Ago You Could've Started", min_value=1, max_value=30, value=5)
        past_return = st.slider("Average Annual Return (%)", min_value=0, max_value=20, value=8)

        months = past_years * 12
        rate = past_return / 100 / 12
        try:
            future_value = past_monthly * (((1 + rate) ** months - 1) / rate)
            st.success(f"💡 If you had invested {format_inr(past_monthly)}/mo for {past_years} years at {past_return}%, you'd have {format_inr(future_value)} today.")
        except:
            st.error("⚠️ Could not compute backward projection.")
