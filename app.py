import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.title("User Input")

age = st.sidebar.number_input("Age", 15, 60)
weight = st.sidebar.number_input("Weight (kg)", 40, 150)
height = st.sidebar.number_input("Height (cm)", 140, 210)

goal = st.sidebar.selectbox("Fitness Goal", ["Fat Loss", "Muscle Gain", "Maintain"])
experience = st.sidebar.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])

# -----------------------------
# Title
# -----------------------------
st.title("🏋️ FitFusion: Gym Analysis System")

# -----------------------------
# BMI Calculator
# -----------------------------
bmi = weight / ((height/100) ** 2)

st.subheader("📊 BMI Analysis")
st.write(f"Your BMI: **{round(bmi,2)}**")

if bmi < 18.5:
    st.warning("Underweight")
elif 18.5 <= bmi < 24.9:
    st.success("Normal Weight")
elif 25 <= bmi < 29.9:
    st.warning("Overweight")
else:
    st.error("Obese")

# -----------------------------
# Workout Planner
# -----------------------------
st.subheader("🏋️ Weekly Workout Plan")

def workout_plan(goal, exp):
    if goal == "Muscle Gain":
        return ["Chest", "Back", "Legs", "Shoulders", "Arms", "Rest"]
    elif goal == "Fat Loss":
        return ["HIIT", "Full Body", "Cardio", "Strength", "Core", "Rest"]
    else:
        return ["Light Cardio", "Yoga", "Full Body", "Rest"]

plan = workout_plan(goal, experience)

for day, workout in enumerate(plan):
    st.write(f"Day {day+1}: {workout}")

# -----------------------------
# Diet & Calorie Tracker
# -----------------------------
st.subheader("🍽️ Diet Tracker (Indian Foods)")

food_data = {
    "Food": ["Roti", "Rice", "Dal", "Paneer", "Poha"],
    "Calories": [100, 200, 150, 300, 180],
    "Protein": [3, 4, 9, 18, 5]
}

df_food = pd.DataFrame(food_data)

food_selected = st.multiselect("Select Food Items", df_food["Food"])

if food_selected:
    selected_df = df_food[df_food["Food"].isin(food_selected)]
    st.write(selected_df)

    st.write("Total Calories:", selected_df["Calories"].sum())
    st.write("Total Protein:", selected_df["Protein"].sum())

# -----------------------------
# Progress Tracker
# -----------------------------
st.subheader("📈 Progress Tracker")

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Weight": [weight, weight-0.2, weight-0.4, weight-0.5, weight-0.7]
}

df_progress = pd.DataFrame(data)

fig = px.line(df_progress, x="Day", y="Weight", title="Weight Progress")
st.plotly_chart(fig)

# -----------------------------
# Goal Recommendation
# -----------------------------
st.subheader("🎯 Goal Recommendation")

if goal == "Fat Loss":
    st.info("Focus on calorie deficit + cardio + HIIT")
elif goal == "Muscle Gain":
    st.info("High protein diet + strength training")
else:
    st.info("Maintain balanced diet and regular exercise")

# -----------------------------
# AI Chatbot (Basic)
# -----------------------------
st.subheader("🤖 Fitness Chatbot")

query = st.text_input("Ask fitness question:")

if query:
    if "protein" in query.lower():
        st.write("Eat paneer, eggs, chicken, dal")
    elif "fat loss" in query.lower():
        st.write("Maintain calorie deficit + cardio")
    else:
        st.write("Stay consistent with workouts!")

# -----------------------------
# Footer
# -----------------------------
st.write("💡 Developed using Streamlit + Plotly")
