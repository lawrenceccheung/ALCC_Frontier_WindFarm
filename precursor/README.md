# Precursor conditions

## Catalog of precursor conditions for offshore conditions
| Case | surface rough. | surface temp <br> rate (flux) | latitude | WD, <br> rel. err. | WS, <br> rel. err. | TI, <br> rel. err. | Shear, <br> rel. err. | Veer, <br> rel. err. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Low WS, Low TI | 0.001 | -0.06 | 50 | 270.07, <br>  0.025% | 6.52, <br>  0.37% |0.0363, <br>  4.2% |0.142, <br>  0.19% | 7.92,  <br>  53% |
| Med WS, Low TI (7km x 2km) | 0.0005| -0.12 | 39.55 | 270.06, <br> 0.021% | 9.05, <br> 0.26% | 0.0264, <br> 29% | 0.171, <br> 0.0044% | 8.99, <br> 58% |
| Med WS, Low TI (4.5km x 2km) | 0.0005| -0.12 | 39.55 | 269.86, <br> 0.051% | 9.01, <br> 0.17% | 0.0309, <br> 17% | 0.160, <br> 6.3% | 8.94, <br> 58% |
| Med WS, Med TI |  0.0013 | (0.001) | 50.0 | 269.77, <br> 0.084% | 9.03, <br> 0.0022% | 0.0700, <br> 0.0023% | 0.0655, <br> 3.7% | 1.06, <br> 82% |
| Med WS, Hig TI | 0.051 | (0.032) | 50.0 | 267.73, <br> 0.84% | 8.93, <br> 1.1% | 0.109, <br> 15% | 0.0566,  <br> 2.4% | 1.23, <br> 11% |
| High WS, Low TI | 0.0003 | -0.145 | 39.55 | 270.13, <br> 0.049% | 11.58, <br> 0.64% | 	0.0348, <br> 5.9% | 0.156, <br> 21% | 5.62, <br> 73% |

## Original catalog of precursor files for offshore conditions
| Case | Lead | Base Directory | (Small Domain) Trials | Time-Searching | Boundary Data | Selected Time Range |
| --- | --- | --- | --- | --- | --- | --- |
| Low WS, Low TI | Gopal | /gpfs/gyalla/OffshorePrecursor/case_LowWS_LowTI_coarse_7x2x1/ | Postprocessing_Stable_7x2x1.ipynb | optmize_time/PrecursorSearch_metmast.ipynb |case_stable_0.06_0.001_50_bcoutput/bndry_data/ | 19765 - 20365 s |
| Med WS, Low TI (7km x 2km) | Lawrence | Frontier: /lustre/orion/cfd162/scratch/lcheung/ALCC_Frontier_WindFarm/MedWS_LowTI/precursor6_7kmX2km_5m/ | --- | --- | --- | 27241 - 27841 s |
| Med WS, Low TI (4.5km x 2km) | Lawrence | Fronter: /lustre/orion/cfd162/scratch/lcheung/ALCC_Frontier_WindFarm/MedWS_LowTI/precursor6_4kmX2km_5m/ | --- | --- | --- | 27473 - 28073 s |
| Med WS, Med TI | Ken | /nscratch/kbrown1/Advanced_Control/AMR/Precursors/TwoTurbine/Offshore_MedTI_Precursor_Coarse/ | ../../Postprocessing_MedWS_MedTI.ipynb | post_processing/time_search_window/PrecursorSearch_horiz_metmast.ipynb | ../Offshore_MedTI_Precursor_Coarse_BoundaryPlanes/bndry_data/ | 42445 - 43745 s |
| Med WS, Hig TI | Ken | /nscratch/kbrown1/Advanced_Control/AMR/Precursors/TwoTurbine/Offshore_HighTI_Precursor_Coarse/ | ../../Postprocessing_MedWS_HighTI.ipynb | post_processing/time_search_window/PrecursorSearch_horiz_metmast.ipynb | ../Offshore_HighTI_Precursor_Coarse_BoundaryPlanes/bndry_data/ | 47473 - 48673 s |
| High WS, Low TI | Dan | /gpfs/drhouck/AdvancedControls/OffshoreStablePrecursor/newmesh/z0_0p0003_temp_-0p145/ | ../../Postprocessing_Stable.ipynb | post_processing/time_window_search/ | bndry_data/ | 25729 - 26329 s |

Note: all notebooks comparing simulations to measurement are here: /nscratch/kbrown1/Advanced_Control/AMR/NYSERDA_Data/
<br> (in five of the notebooks labeled "processor_SWbuoy_*WS_*TI.ipynb")
