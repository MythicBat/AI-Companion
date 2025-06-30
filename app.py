import streamlit as st
import datetime
from firebase.client import save_mood, get_mood_history
import plotly.express as px
from ai.chatbot import ask_companion

# PAGE CONFIG
st.set_page_config(
    page_title="SAD Companion",
    page_icon="🌼",
    layout="centered"
)

# HEADER
st.title("🌼 SAD Companion")
st.subheader("Your daily springtime mental wellness buddy ☀️")

st.markdown("---")

# USER NAME
st.sidebar.title("👤 Your Profile")
user_name = st.sidebar.text_input("Enter your name")

# DAILY MOOD TRACKER
st.header("How are you feeling today?")
today = datetime.date.today().strftime("%Y-%m-%d")

mood = st.slider(
    "Rate your moode today",
    min_value=1,
    max_value=10,
    value=5,
    format="%d",
    help="1 = Very Low, 10 = Great!"
)

if st.button("💾 Save Mood Entry"):
    if user_name:
        save_mood(user_name, mood, today)
        st.success(f"Saved mood {mood}/10 for {user_name} on {today}")
    else:
        st.error("Please enter your name to save the entry.")

st.markdown("---")
st.header("📈 Your Mood Trend")

if user_name:
    history = get_mood_history(user_name)

    if history:
        dates = [entry[0] for entry in history]
        moods = [entry[1] for entry in history]

        fig = px.line(
            x=dates,
            y=moods,
            markers=True,
            title="Mood over Time",
            labels={"x": "Date", "y": "Mood (1-10)"}
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No mood data found yet. Start tracking daily!")
else:
    st.warning("Enter your name above to see your mood history.")

# DAILY POSITIVE HABIT
st.header("🌱 Daily Positive Habit")

habit = "🌞 Get 15 minutes of sunlight before 10 AM."

st.info(habit)
st.markdown("---")

# AI CHATBOT
st.header("💬 Talk to your Companion")
user_message = st.text_input("How are you feeling today?", placeholder="I'm feeling anxious...")

if st.button(" 🧠 Get Support"):
    if user_message:
        with st.spinner("Thinking of something kind..."):
            response = ask_companion(user_message)
            st.success(response)
    else:
        st.warning("Please enter a message first.")

# FOOTER
st.markdown("---")