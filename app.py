import streamlit as st
import requests
import json

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
AGENT_URL = "https://divi220903-agentic-vehicle-advisor.hf.space/predict"

st.set_page_config(
    page_title="Agentic Vehicle AI",
    page_icon="🚗",
    layout="centered"
)

# --------------------------------------------------
# UI HEADER
# --------------------------------------------------
st.title("🚗 Agentic Vehicle Advisor")
st.caption("AI-powered vehicle health, RCA insights & autonomous service booking")

st.divider()

# --------------------------------------------------
# INPUT DATA (Demo Vehicle)
# --------------------------------------------------
vehicle_data = {
    "vehicle": "Demo Car",
    "components": [
        {"name": "Brakes", "health": 78, "failure_score": 0.22},
        {"name": "Engine", "health": 92, "failure_score": 0.08},
        {"name": "Battery", "health": 65, "failure_score": 0.35}
    ]
}

st.subheader("🔍 Vehicle Health Snapshot")
st.json(vehicle_data)

# --------------------------------------------------
# ACTION BUTTON
# --------------------------------------------------
if st.button("🧠 Run Vehicle Agent"):
    with st.spinner("Agent analyzing vehicle data..."):
        try:
            response = requests.post(
                AGENT_URL,
                headers={"Content-Type": "application/json"},
                data=json.dumps(vehicle_data),
                timeout=30
            )

            # Show raw response for debugging (SAFE)
            st.subheader("📡 Raw Agent Response")
            st.code(response.text)

            # Try parsing JSON safely
            try:
                result = response.json()
            except Exception:
                st.error("❌ Agent did not return valid JSON")
                st.stop()

            # --------------------------------------------------
            # DISPLAY RESULTS
            # --------------------------------------------------
            st.success("✅ Agent executed successfully")

            if "rca" in result:
                st.subheader("📊 RCA Insights")
                st.write(result["rca"])

            if "security_logs" in result:
                st.subheader("🔐 Security Logs")
                st.write(result["security_logs"])

            if "service_booking" in result:
                st.subheader("📅 Service Booking")
                st.success(
                    f"""
                    **Date & Time:** {result['service_booking']['date_time']}  
                    **Service Center:** {result['service_booking']['center']}  
                    **Booking ID:** {result['service_booking']['booking_id']}
                    """
                )

        except requests.exceptions.RequestException as e:
            st.error("🚨 Failed to connect to Agent Space")
            st.code(str(e))
