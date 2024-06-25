# Define some properties
CASETAG='WM_SideToSide_A2_St0p3'
rotorD = 240           # Rotor diameter
WS     = 9.05          # Wind speed, m/s
OFoptions=("ADparam_TwrAero:True ADparam_TwrShadow:0 FSTparam_CompHydro:0 FSTparam_CompSub:0 "
               "ADparam_OutList0:RtAeroFxh "
               "EDparam_YawDOF:False "
               "EDparam_PtfmSgDOF:False "
               "EDparam_PtfmSwDOF:False "
               "EDparam_PtfmHvDOF:False "
               "EDparam_PtfmRDOF:False "
               "EDparam_PtfmPDOF:False "
               "EDparam_PtfmYDOF:False "
               "AMRparam_Actuator_epsilon:[2;2;2] "
               "AMRparam_Actuator_epsilon_tower:[2;2;2] "
              )
DISCON2p8_options = ("SDparam_DLL_FileName:/lustre/orion/cfd162/proj-shared/lcheung/ROSCO_2.8/ROSCO/build/libdiscon.so "
                     "SDparam_DLL_InFile:IEA-15-240-RWT-Monopile_DISCON.IN "
                     )

St           = 0.3
AWC_NumModes = 2
AWC_n        = [1,-1]; AWC_n = '"{}"'.format(" ".join(map(str, AWC_n)));
AWC_freq     = [St*WS/rotorD, St*WS/rotorD]; AWC_freq = '"{}"'.format(" ".join(map(str, AWC_freq)));
AWC_amp      = [1.0, 1.0]; AWC_amp = '"{}"'.format(" ".join(map(str, AWC_amp)));
AWC_clock    = [90, 90]; AWC_clock = '"{}"'.format(" ".join(map(str, AWC_clock)));
AWCoptions = ("SD_param_Ptch_Cntrl:1 "
              "DISCONparam_AWC_Mode:1 "
              "DISCONparam_AWC_NumModes:%i DISCONparam_AWC_n:%s DISCONparam_AWC_freq:%s DISCONparam_AWC_amp:%s DISCONparam_AWC_clockangle:%s "%(AWC_NumModes,AWC_n,AWC_freq, AWC_amp, AWC_clock)
             )
NAWCTURBS = 3
