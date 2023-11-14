import streamlit as st
import psutil
import os

# Get the PID of the current process
pid = os.getpid()
process = psutil.Process(pid)

# Function to get resource usage of the current process
def get_process_info(process):
    cpu_usage = process.cpu_percent(interval=1)
    memory_info = process.memory_info()
    return cpu_usage, memory_info.rss, memory_info.vms

# Streamlit application layout
st.title('Streamlit App Resource Usage')

cpu_usage, rss_memory, vms_memory = get_process_info(process)

st.metric(label="CPU Usage by App", value=f"{cpu_usage}%")
st.metric(label="RSS Memory by App", value=f"{rss_memory / (1024**3):.2f} GB")
st.metric(label="VMS Memory by App", value=f"{vms_memory / (1024**3):.2f} GB")

# Button to refresh the metrics
if st.button('Refresh'):
    cpu_usage, rss_memory, vms_memory = get_process_info(process)

    st.metric(label="CPU Usage by App", value=f"{cpu_usage}%")
    st.metric(label="RSS Memory by App", value=f"{rss_memory / (1024**3):.2f} GB")
    st.metric(label="VMS Memory by App", value=f"{vms_memory / (1024**3):.2f} GB")
