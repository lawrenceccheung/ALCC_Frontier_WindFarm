#!/bin/sh

export CONFIGSCRIPT=baseline.py
jupyter nbconvert --to notebook --execute MedWS_LowTI_Offshore_Stable_Farmrun1_10x10_template.ipynb --output MedWS_LowTI_Offshore_Stable_Farmrun1_10x10_baseline.ipynb

export CONFIGSCRIPT=WM_Helix_A2_St_0p3.py
jupyter nbconvert --to notebook --execute MedWS_LowTI_Offshore_Stable_Farmrun1_10x10_template.ipynb --output MedWS_LowTI_Offshore_Stable_Farmrun1_10x10_WM_Helix_A2_St_0p3.ipynb

export CONFIGSCRIPT=WM_Pulse_A2_St_0p3.py
jupyter nbconvert --to notebook --execute MedWS_LowTI_Offshore_Stable_Farmrun1_10x10_template.ipynb --output MedWS_LowTI_Offshore_Stable_Farmrun1_10x10_WM_Pulse_A2_St_0p3.ipynb

export CONFIGSCRIPT=WM_SideToSide_A2_St_0p3.py
jupyter nbconvert --to notebook --execute MedWS_LowTI_Offshore_Stable_Farmrun1_10x10_template.ipynb --output MedWS_LowTI_Offshore_Stable_Farmrun1_10x10_WM_SideToSide_A2_St_0p3.ipynb

