import streamlit as st
import datetime
import time
import winsound  # Windows ke liye sound play karne ke liye

def play_sound():
    """Plays a beep sound when the alarm goes off."""
    for _ in range(3):  # Beep 3 times
        winsound.Beep(1000, 500)  # Frequency: 1000 Hz, Duration: 500ms
        time.sleep(0.5)

st.title("⏰ Streamlit Alarm Clock 🔔")

# List to store alarms
if "alarms" not in st.session_state:
    st.session_state.alarms = []

# Input field for adding new alarms
new_alarm = st.text_input("Set Alarm (HH:MM:SS):", "")

if st.button("Add Alarm"):
    try:
        datetime.datetime.strptime(new_alarm, "%H:%M:%S")  # Validate format
        st.session_state.alarms.append(new_alarm)
        st.success(f"✅ Alarm set for {new_alarm}")
    except ValueError:
        st.error("❌ Invalid format! Use HH:MM:SS")

# Display set alarms
st.subheader("🕰️ Active Alarms:")
for alarm in st.session_state.alarms:
    st.write(f"⏳ {alarm}")

# Alarm checking function
def check_alarms():
    """Checks if the current time matches any alarm and triggers it."""
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now in st.session_state.alarms:
            st.warning("⏰ Time's up! Wake up! 🔔")
            play_sound()
            st.session_state.alarms.remove(now)
        time.sleep(1)

# Run the alarm checker
if st.button("Start Alarm"):
    st.write("🔄 Alarm system running...")
    check_alarms()
