import streamlit as st
from qsdsan import WasteStream, System, processes as pc, sanunits as su

# Setup temperature and constants
Temp = 293.15  # 20°C
Q_waste = 385
Q_external = 18446

# Title
st.title("Wastewater Treatment Simulator (QSDsan + ASM2d)")

# User inputs
Q_inflow = st.slider("Influent Flowrate (m³/day)", 5000, 30000, 18446)
COD_in = st.slider("Influent COD (mg/L)", 200, 1000, 565)

# Component setup
cmps = pc.create_asm2d_cmps()
WasteStream.default_composition = cmps

# Set influent
influent = WasteStream('influent', T=Temp)
influent.set_flow_by_concentration(Q_inflow, {
    'concentrations': {
        'S_I': 14,
        'X_I': 26.5,
        'S_F': 20.1,
        'S_A': 94.3,
        'X_S': 409.5,
        'S_NH4': 31,
        'S_NO3': 0.266,
        'S_PO4': 2.8,
        'X_PP': 0.05,
        'X_PHA': 0.5,
        'X_H': 0.15,
        'S_ALK': 7 * 12,
    },
    'units': ('m3/d', 'mg/L')
})

# Build a minimal system (simplified)
effluent = WasteStream('effluent', T=Temp)
clarifier = su.Clarifier('C1', ins=influent, outs=effluent)
system = System('WWTP', path=(clarifier,))

# Simulate
if st.button("Run Simulation"):
    system.simulate()
    st.success("Simulation complete!")
    st.write(f"Effluent COD: **{effluent.COD:.2f} mg/L**")
