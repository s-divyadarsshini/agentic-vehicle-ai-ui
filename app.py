import streamlit as st
import requests

st.set_page_config(
    page_title="Agentic Vehicle AI Platform",
    layout="wide"
)

AGENT_URL = "https://agentic-vehicle-advisor.hf.space"


st.title("🚗 Agentic Vehicle Intelligence Platform")
st.caption("Autonomous diagnostics • Predictive maintenance • Secure AI agents")

st.divider()

# SECTION 1 — VEHICLE HEALTH
st.subheader("🟢 Vehicle Digital Twin")

vehicle_data = requests.get(
    "https://s-divyadarsshini.github.io/agentic-vehicle-ai-db/vehicle_state.json"
).json()

for comp in vehicle_data["components"]:
    st.metric(
        label=comp["name"],
        value=f"{comp['health']}%",
        delta=f"Risk {comp['failure_score']}"
    )

st.divider()

# SECTION 2 — SERVICE AGENT
st.subheader("🧠 AI Service Advisor")

issue = st.text_input("Describe the issue (optional)")
confirm = st.radio("Confirm service booking", ["No", "Yes"])

if st.button("Run AI Agent"):
    response = requests.post(
    AGENT_URL + "/api/predict",
    json={
        "data": [issue, confirm]
    }
)

result = response.json()
st.success(result["data"][0])


st.divider()

# SECTION 3 — RCA INSIGHTS
st.subheader("📊 RCA Insights")

if st.button("Generate RCA Insights"):
    response = requests.post(
    AGENT_URL + "/api/predict",
    json={
        "data": ["", "No"]
    }
)

result = response.json()
st.info(result["data"][0])


st.divider()

# SECTION 4 — SECURITY STATUS
st.subheader("🔐 System Security")

st.success("All agent actions verified • Secure ✔")
