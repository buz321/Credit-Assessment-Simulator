import streamlit as st
import matplotlib.pyplot as plt

# Streamlit app title
st.title("💰 Loan Approval Simulator")
st.markdown("Experience a virtual loan approval process!")

# User inputs
income = st.number_input("Annual Income (10,000 KRW)", min_value=0)
job = st.selectbox("Job Type", ["Large Corporation", "Small Business", "Freelancer", "Unemployed"])
loan_amount = st.number_input("Loan Amount (10,000 KRW)", min_value=0)
loan_term = st.selectbox("Loan Term (Years)", [1, 3, 5, 10])
credit_grade = st.selectbox("Credit Grade", ["Excellent", "Good", "Average", "Below Average", "Poor"])

# Scoring logic
def calculate_score(income, job, loan_amount, loan_term, credit_grade):
    score_breakdown = {}

    # Income score
    if income >= 5000:
        score_breakdown['Income'] = 30
    elif income >= 3000:
        score_breakdown['Income'] = 20
    else:
        score_breakdown['Income'] = 10

    # Job score
    job_scores = {"Large Corporation": 30, "Small Business": 20, "Freelancer": 10, "Unemployed": 0}
    score_breakdown['Job'] = job_scores[job]

    # Loan amount score (penalty)
    if loan_amount <= 1000:
        score_breakdown['Loan Amount'] = 20
    elif loan_amount <= 3000:
        score_breakdown['Loan Amount'] = 10
    else:
        score_breakdown['Loan Amount'] = 0

    # Loan term score
    term_scores = {1: 20, 3: 15, 5: 10, 10: 5}
    score_breakdown['Loan Term'] = term_scores[loan_term]

    # Credit grade score
    credit_scores = {"Excellent": 30, "Good": 20, "Average": 10, "Below Average": 5, "Poor": 0}
    score_breakdown['Credit Grade'] = credit_scores[credit_grade]

    total_score = sum(score_breakdown.values())
    return total_score, score_breakdown

# Calculate result when button is clicked
if st.button("Start Evaluation"):
    score, breakdown = calculate_score(income, job, loan_amount, loan_term, credit_grade)

    # Display result
    st.subheader(f"🎯 Final Score: {score}")

    if score >= 70:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Denied")

    # Visualize score breakdown
    st.subheader("Score Breakdown")
    fig, ax = plt.subplots()
    factors = ["Income", "Job", "Loan Amount", "Loan Term", "Credit Grade"]
    scores = [breakdown[factor] for factor in factors]

    ax.bar(factors, scores)
    ax.set_ylabel("Score")
    ax.set_ylim(0, 40)
    st.pyplot(fig)

    # Display score breakdown text
    for factor, pts in breakdown.items():
        st.write(f"**{factor}**: {pts} points")
