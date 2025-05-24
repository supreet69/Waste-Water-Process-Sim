# simulation.py

from qsdsan import System, Component, WasteStream
from qsdsan.utils import load_asm2d_components

# Load predefined ASM2d components
def get_components():
    return load_asm2d_components()

# Define a basic example simulation
def run_simulation():
    # Load components
    cmps = get_components()

    # Create a sample influent WasteStream
    influent = WasteStream(
        ID='influent',
        flow=18446,  # m3/day
        T=293.15,  # K
        P=101325,  # Pa
        component_flow={
            'S_NH4': 31,
            'S_NO3': 0.266,
            'S_PO4': 2.8,
            'S_F': 20.1,
            'S_A': 94.3,
            'S_I': 14,
            'S_ALK': 84,  # mg/L
        },
        units=('m3/d', 'mg/L'),
        components=cmps
    )

    # Return influent info for now
    return influent.show()

