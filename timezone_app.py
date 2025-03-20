import streamlit as st
import datetime
import pytz

# App title
st.title("🌍 Time Zone Converter 🕒")

# Get list of time zones
time_zones = pytz.all_timezones

# Select multiple time zones
tz_selection = st.multiselect("Select Time Zones", time_zones, default=["UTC", "Asia/Karachi", "America/New_York"])

# Display current time in selected time zones
st.subheader("Current Time in Selected Zones")
for tz in tz_selection:
    now = datetime.datetime.now(pytz.timezone(tz))
    st.write(f"**{tz}**: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Time conversion tool
st.subheader("Convert Time Between Time Zones")

col1, col2, col3 = st.columns(3)

with col1:
    from_tz = st.selectbox("From Time Zone", time_zones, index=time_zones.index("UTC"))

with col2:
    to_tz = st.selectbox("To Time Zone", time_zones, index=time_zones.index("Asia/Karachi"))

with col3:
    time_input = st.time_input("Select Time", datetime.datetime.now().time())

# Convert time
if st.button("Convert Time"):
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    
    # Create datetime object for conversion
    now = datetime.datetime.now().date()
    selected_time = datetime.datetime.combine(now, time_input)
    selected_time = from_zone.localize(selected_time)
    converted_time = selected_time.astimezone(to_zone)
    
    st.success(f"{time_input} in {from_tz} is {converted_time.strftime('%Y-%m-%d %H:%M:%S')} in {to_tz}")
