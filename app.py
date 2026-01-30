import streamlit as st
import requests
import json

st.set_page_config(page_title="Agentic Vehicle Advisor", layout="wide")

AGENT_URL = "https://divi220903-agentic-vehicle-advisor.hf.space/predict"

st.title("🚗 Agentic Vehicle Advisor")
st.caption("AI-powered vehicle health, RCA insights & autonomous service booking")

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

if st.button("Run Agentic Analysis"):
    with st.spinner("Agent reasoning in progress..."):
        response = requests.post(
            AGENT_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(vehicle_data)
        )

        if response.status_code == 200:
            result = response.json()

            st.subheader("🧠 RCA Insights")
            for r in result["rca"]:
                st.warning(r)

            st.subheader("📅 Autonomous Service Booking")
            st.success(
                f"""
Date & Time: {result['service_booking']['date_time']}
Service Center: {result['service_booking']['center']}
Booking ID: {result['service_booking']['booking_id']}
"""
            )

            st.subheader("🔐 Security Logs")
            st.info(result["security_logs"])

        else:
            st.error("Agent backend not reachable")
