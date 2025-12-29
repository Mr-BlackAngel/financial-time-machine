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
