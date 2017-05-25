ptf #
[TITLE]
Data from Seattle EOC Green Roof Study
Data entered on September 24, 2013 by E. Hirschmann
BMP 17, STRM 137

[OPTIONS]
FLOW_UNITS           GPM
INFILTRATION         GREEN_AMPT
FLOW_ROUTING         DYNWAVE
START_DATE           04/12/2009
START_TIME           03:10:00
REPORT_START_DATE    04/12/2009
REPORT_START_TIME    03:10:00
END_DATE             04/13/2009
END_TIME             15:25:00
SWEEP_START          01/01
SWEEP_END            12/31
DRY_DAYS             0
REPORT_STEP          00:05:00
WET_STEP             00:01:00
DRY_STEP             00:01:00
ROUTING_STEP         0:00:05 
ALLOW_PONDING        YES
INERTIAL_DAMPING     PARTIAL
VARIABLE_STEP        0.00
LENGTHENING_STEP     0
MIN_SURFAREA         0
NORMAL_FLOW_LIMITED  BOTH
SKIP_STEADY_STATE    NO
FORCE_MAIN_EQUATION  H-W
LINK_OFFSETS         DEPTH
MIN_SLOPE            0

[EVAPORATION]
;;Type       Parameters
;;---------- ----------
CONSTANT     0.0
DRY_ONLY     NO

[RAINGAGES]
;;               Rain      Time   Snow   Data      
;;Name           Type      Intrvl Catch  Source    
;;-------------- --------- ------ ------ ----------
04/12/09_Storm   INTENSITY 0:05   1.0    TIMESERIES Storm137        

[SUBCATCHMENTS]
;;                                                 Total    Pcnt.             Pcnt.    Curb     Snow    
;;Name           Raingage         Outlet           Area     Imperv   Width    Slope    Length   Pack    
;;-------------- ---------------- ---------------- -------- -------- -------- -------- -------- --------
;Subcatchment for Seattle Green Roof (BMP ID 17)
EOCSeattle       04/12/09_Storm   1                0.17171717 100      86       4.1      0                        

[SUBAREAS]
;;Subcatchment   N-Imperv   N-Perv     S-Imperv   S-Perv     PctZero    RouteTo    PctRouted 
;;-------------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
EOCSeattle       0.01       0.1        0          0          25         OUTLET    

[INFILTRATION]
;;Subcatchment   Suction    HydCon     IMDmax    
;;-------------- ---------- ---------- ----------
EOCSeattle       3.0        0.5        4         

[LID_CONTROLS]
;;               Type/Layer Parameters
;;-------------- ---------- ----------
GreenRoof        GR
;;GreenRoof      SURFACE   srf_strg   srf_vgvlm   srf_rghns    srf_slp   0.0
GreenRoof        SURFACE  #srf_strg# #srf_vgvlm# #srf_rghns# # srf_slp#  0.0
;;GreenRoof      SOIL       sl_thck    sl_prsty    sl_fldcp   sl_wltpt      sl_kst     sl_kcff     sl_sctn  
GreenRoof        SOIL     # sl_thck# # sl_prsty# # sl_fldcp# #sl_wltpt#  #  sl_kst#  # sl_kcff#  # sl_sctn#  
;;GreenRoof      DRAINMAT   drnm_thck   drnm_vdfr   drnm_rghns
GreenRoof        DRAINMAT  #drnm_thck# #drnm_vdfr# #drnm_rghns#
[LID_USAGE]
;;Subcatchment   LID Process      Number  Area       Width      InitSatur  FromImprv  ToPerv     Report File
;;-------------- ---------------- ------- ---------- ---------- ---------- ---------- ---------- -----------
EOCSeattle       GreenRoof        1       7480.00    #ldu_wdth# #ldu_ntstr# 100        0          "gr17.txt"

[OUTFALLS]
;;               Invert     Outfall    Stage/Table      Tide
;;Name           Elev.      Type       Time Series      Gate
;;-------------- ---------- ---------- ---------------- ----
1                0          FREE                        NO

[TIMESERIES]
;;Name           Date       Time       Value     
;;-------------- ---------- ---------- ----------
;04/12/2009 Seattle Green Roof (in/hr)
Storm137         4/12/2009  3:30       0.12      
Storm137         4/12/2009  3:35       0.12      
Storm137         4/12/2009  3:40       0         
Storm137         4/12/2009  3:45       0         
Storm137         4/12/2009  3:50       0         
Storm137         4/12/2009  3:55       0.12      
Storm137         4/12/2009  4:0        0         
Storm137         4/12/2009  4:5        0.12      
Storm137         4/12/2009  4:10       0         
Storm137         4/12/2009  4:15       0         
Storm137         4/12/2009  4:20       0         
Storm137         4/12/2009  4:25       0         
Storm137         4/12/2009  4:30       0         
Storm137         4/12/2009  4:35       0         
Storm137         4/12/2009  4:40       0.12      
Storm137         4/12/2009  4:45       0.12      
Storm137         4/12/2009  4:50       0         
Storm137         4/12/2009  4:55       0         
Storm137         4/12/2009  5:0        0.12      
Storm137         4/12/2009  5:5        0         
Storm137         4/12/2009  5:10       0.12      
Storm137         4/12/2009  5:15       0         
Storm137         4/12/2009  5:20       0.12      
Storm137         4/12/2009  5:25       0         
Storm137         4/12/2009  5:30       0.12      
Storm137         4/12/2009  5:35       0         
Storm137         4/12/2009  5:40       0.12      
Storm137         4/12/2009  5:45       0.12      
Storm137         4/12/2009  5:50       0.12      
Storm137         4/12/2009  5:55       0.12      
Storm137         4/12/2009  6:0        0.12      
Storm137         4/12/2009  6:5        0         
Storm137         4/12/2009  6:10       0.12      
Storm137         4/12/2009  6:15       0.24      
Storm137         4/12/2009  6:20       0.12      
Storm137         4/12/2009  6:25       0.12      
Storm137         4/12/2009  6:30       0.12      
Storm137         4/12/2009  6:35       0         
Storm137         4/12/2009  6:40       0         
Storm137         4/12/2009  6:45       0.12      
Storm137         4/12/2009  6:50       0         
Storm137         4/12/2009  6:55       0         
Storm137         4/12/2009  7:0        0         
Storm137         4/12/2009  7:5        0         
Storm137         4/12/2009  7:10       0         
Storm137         4/12/2009  7:15       0.12      
Storm137         4/12/2009  7:20       0         
Storm137         4/12/2009  7:25       0         
Storm137         4/12/2009  7:30       0         
Storm137         4/12/2009  7:35       0.12      
Storm137         4/12/2009  7:40       0         
Storm137         4/12/2009  7:45       0         
Storm137         4/12/2009  7:50       0         
Storm137         4/12/2009  7:55       0         
Storm137         4/12/2009  8:0        0         
Storm137         4/12/2009  8:5        0.12      
Storm137         4/12/2009  8:10       0         
Storm137         4/12/2009  8:15       0         
Storm137         4/12/2009  8:20       0         
Storm137         4/12/2009  8:25       0         
Storm137         4/12/2009  8:30       0         
Storm137         4/12/2009  8:35       0.12      
Storm137         4/12/2009  8:40       0         
Storm137         4/12/2009  8:45       0         
Storm137         4/12/2009  8:50       0         
Storm137         4/12/2009  8:55       0         
Storm137         4/12/2009  9:0        0.12      
Storm137         4/12/2009  9:5        0         
Storm137         4/12/2009  9:10       0.12      
Storm137         4/12/2009  9:15       0         
Storm137         4/12/2009  9:20       0.12      
Storm137         4/12/2009  9:25       0         
Storm137         4/12/2009  9:30       0.12      
Storm137         4/12/2009  9:35       0         
Storm137         4/12/2009  9:40       0.12      
Storm137         4/12/2009  9:45       0.12      
Storm137         4/12/2009  9:50       0         
Storm137         4/12/2009  9:55       0         
Storm137         4/12/2009  10:0       0.12      
Storm137         4/12/2009  10:5       0         
Storm137         4/12/2009  10:10      0         
Storm137         4/12/2009  10:15      0.12      
Storm137         4/12/2009  10:20      0         
Storm137         4/12/2009  10:25      0         
Storm137         4/12/2009  10:30      0         
Storm137         4/12/2009  10:35      0.12      
Storm137         4/12/2009  10:40      0         
Storm137         4/12/2009  10:45      0.12      
Storm137         4/12/2009  10:50      0         
Storm137         4/12/2009  10:55      0         
Storm137         4/12/2009  11:0       0         
Storm137         4/12/2009  11:5       0.12      
Storm137         4/12/2009  11:10      0         
Storm137         4/12/2009  11:15      0         
Storm137         4/12/2009  11:20      0         
Storm137         4/12/2009  11:25      0         
Storm137         4/12/2009  11:30      0         
Storm137         4/12/2009  11:35      0         
Storm137         4/12/2009  11:40      0.12      
Storm137         4/12/2009  11:45      0         
Storm137         4/12/2009  11:50      0         
Storm137         4/12/2009  11:55      0         
Storm137         4/12/2009  12:0       0         
Storm137         4/12/2009  12:5       0         
Storm137         4/12/2009  12:10      0         
Storm137         4/12/2009  12:15      0         
Storm137         4/12/2009  12:20      0         
Storm137         4/12/2009  12:25      0         
Storm137         4/12/2009  12:30      0         
Storm137         4/12/2009  12:35      0         
Storm137         4/12/2009  12:40      0         
Storm137         4/12/2009  12:45      0.12      
Storm137         4/12/2009  12:50      0         
Storm137         4/12/2009  12:55      0         
Storm137         4/12/2009  13:0       0.12      
Storm137         4/12/2009  13:5       0         
Storm137         4/12/2009  13:10      0.12      
Storm137         4/12/2009  13:15      0         
Storm137         4/12/2009  13:20      0         
Storm137         4/12/2009  13:25      0         
Storm137         4/12/2009  13:30      0.12      
Storm137         4/12/2009  13:35      0         
Storm137         4/12/2009  13:40      0.12      
Storm137         4/12/2009  13:45      0         
Storm137         4/12/2009  13:50      0         
Storm137         4/12/2009  13:55      0.12      
Storm137         4/12/2009  14:0       0         
Storm137         4/12/2009  14:5       0.12      
Storm137         4/12/2009  14:10      0.12      
Storm137         4/12/2009  14:15      0         
Storm137         4/12/2009  14:20      0.12      
Storm137         4/12/2009  14:25      0         
Storm137         4/12/2009  14:30      0.12      
Storm137         4/12/2009  14:35      0         
Storm137         4/12/2009  14:40      0.12      
Storm137         4/12/2009  14:45      0         
Storm137         4/12/2009  14:50      0         
Storm137         4/12/2009  14:55      0.12      
Storm137         4/12/2009  15:0       0.12      
Storm137         4/12/2009  15:5       0.12      
Storm137         4/12/2009  15:10      0.12      
Storm137         4/12/2009  15:15      0.12      
Storm137         4/12/2009  15:20      0.12      
Storm137         4/12/2009  15:25      0         
Storm137         4/12/2009  15:30      0.12      
Storm137         4/12/2009  15:35      0.12      
Storm137         4/12/2009  15:40      0         
Storm137         4/12/2009  15:45      0.24      
Storm137         4/12/2009  15:50      0         
Storm137         4/12/2009  15:55      0.12      
Storm137         4/12/2009  16:0       0         
Storm137         4/12/2009  16:5       0.12      
Storm137         4/12/2009  16:10      0         
Storm137         4/12/2009  16:15      0.12      
Storm137         4/12/2009  16:20      0         
Storm137         4/12/2009  16:25      0         
Storm137         4/12/2009  16:30      0.12      
Storm137         4/12/2009  16:35      0         
Storm137         4/12/2009  16:40      0         
Storm137         4/12/2009  16:45      0.12      
Storm137         4/12/2009  16:50      0         
Storm137         4/12/2009  16:55      0         
Storm137         4/12/2009  17:0       0         
Storm137         4/12/2009  17:5       0         
Storm137         4/12/2009  17:10      0.12      
Storm137         4/12/2009  17:15      0         
Storm137         4/12/2009  17:20      0         
Storm137         4/12/2009  17:25      0.12      
Storm137         4/12/2009  17:30      0.24      
Storm137         4/12/2009  17:35      0.12      
Storm137         4/12/2009  17:40      0.12      
Storm137         4/12/2009  17:45      0.12      
Storm137         4/12/2009  17:50      0.12      
Storm137         4/12/2009  17:55      0         
Storm137         4/12/2009  18:0       0.12      
Storm137         4/12/2009  18:5       0         
Storm137         4/12/2009  18:10      0.12      
Storm137         4/12/2009  18:15      0         
Storm137         4/12/2009  18:20      0         
Storm137         4/12/2009  18:25      0         
Storm137         4/12/2009  18:30      0         
Storm137         4/12/2009  18:35      0         
Storm137         4/12/2009  18:40      0         
Storm137         4/12/2009  18:45      0.12      

[REPORT]
INPUT      YES
CONTROLS   YES
SUBCATCHMENTS ALL
NODES ALL
LINKS ALL

[TAGS]

[MAP]
DIMENSIONS 0.000 0.000 10000.000 10000.000
Units      None

[COORDINATES]
;;Node           X-Coord            Y-Coord           
;;-------------- ------------------ ------------------
1                6674.234           6265.607          

[VERTICES]
;;Link           X-Coord            Y-Coord           
;;-------------- ------------------ ------------------

[Polygons]
;;Subcatchment   X-Coord            Y-Coord           
;;-------------- ------------------ ------------------
EOCSeattle       1783.781           7951.079          
EOCSeattle       2564.846           8223.268          
EOCSeattle       3570.764           8033.919          
EOCSeattle       4103.308           7465.871          
EOCSeattle       4624.018           6637.469          
EOCSeattle       3570.764           6270.605          
EOCSeattle       2647.687           6175.931          
EOCSeattle       1570.764           6696.641          
EOCSeattle       1464.255           7501.374          
EOCSeattle       1795.616           7915.576          

[SYMBOLS]
;;Gage           X-Coord            Y-Coord           
;;-------------- ------------------ ------------------
04/12/09_Storm   1328.036           8127.128          
