ptf #
[TITLE]
Data from Permeable Pavement Cell "A" in Boone, NC
Data entered on September 4, 2013 by E. Hirschmann
BMP ID 16, STRM 127

[OPTIONS]
;;Option             Value
FLOW_UNITS           GPM
INFILTRATION         GREEN_AMPT
FLOW_ROUTING         DYNWAVE
LINK_OFFSETS         DEPTH
MIN_SLOPE            0
ALLOW_PONDING        YES
SKIP_STEADY_STATE    NO

START_DATE           04/27/2011
START_TIME           20:40:00
REPORT_START_DATE    04/27/2011
REPORT_START_TIME    20:40:00
END_DATE             04/28/2011
END_TIME             16:00:00
SWEEP_START          01/01
SWEEP_END            12/31
DRY_DAYS             0
REPORT_STEP          00:02:00
WET_STEP             00:00:15
DRY_STEP             00:02:00
ROUTING_STEP         0:00:05 

INERTIAL_DAMPING     PARTIAL
NORMAL_FLOW_LIMITED  BOTH
FORCE_MAIN_EQUATION  H-W
VARIABLE_STEP        0.00
LENGTHENING_STEP     0
MIN_SURFAREA         0
MAX_TRIALS           0
HEAD_TOLERANCE       0
SYS_FLOW_TOL         5
LAT_FLOW_TOL         5

[EVAPORATION]
;;Type       Parameters
;;---------- ----------
CONSTANT     0.0
DRY_ONLY     NO

[RAINGAGES]
;;               Rain      Time   Snow   Data      
;;Name           Type      Intrvl Catch  Source    
;;-------------- --------- ------ ------ ----------
04/27/11_Storm     INTENSITY 0:01     1.0      FILE       "storm127.dat"   strm127    IN   

[SUBCATCHMENTS]
;;                                                 Total    Pcnt.             Pcnt.    Curb     Snow    
;;Name           Raingage         Outlet           Area     Imperv   Width    Slope    Length   Pack    
;;-------------- ---------------- ---------------- -------- -------- -------- -------- -------- --------
;Subcatchment for NC Porous Pavement(BMP ID 16)
parkinglot       04/27/11_Storm     1                0.0158   100      20       0.5      0                        

[SUBAREAS]
;;Subcatchment   N-Imperv   N-Perv     S-Imperv   S-Perv     PctZero    RouteTo    PctRouted 
;;-------------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
parkinglot       0.01       0.1        0.00       0.05       100        OUTLET    

[INFILTRATION]
;;Subcatchment   Suction    HydCon     IMDmax    
;;-------------- ---------- ---------- ----------
parkinglot       3.0        0.5        .5        

[LID_CONTROLS]
;;               Type/Layer Parameters
;;-------------- ---------- ----------
prPvmnt          PP
;;                        berm ht    veg vol     surf rgh    surf slope
prPvmnt          SURFACE  #srf_strg# #srf_vgvlm# #srf_rghns# # srf_slp#  5
;;                        thcknss    void ratio  imprv frac  permeab     clog factor
prPvmnt          PAVEMENT #pvm_thck# # pvm_vdrt# #pvm_mpvfc# #pvm_prmb#  200
;;                        thcknss    void ratio  seepage    clog factor
prPvmnt          STORAGE  #str_thck# # str_vdrt# # str_cndt#  200
;;                        flow cff   flow exp    offset        
prPvmnt          DRAIN    # drn_cff# #  drn_xpn# # drn_ffst#    6         

[LID_USAGE]
;;Subcatchment   LID Process      Number  Area       Width      InitSatur  FromImprv  ToPerv     Report File
;;-------------- ---------------- ------- ---------- ---------- ---------- ---------- ---------- -----------
parkinglot       prPvmnt          1       687        20         #ldu_ntstr# 100       0          "ppvmnt16val2.txt"

[OUTFALLS]
;;               Invert     Outfall    Stage/Table      Tide
;;Name           Elev.      Type       Time Series      Gate
;;-------------- ---------- ---------- ---------------- ----
1                0          FREE                        NO

[TIMESERIES]
;;Name           Date       Time       Value     
;;-------------- ---------- ---------- ----------


[REPORT]
INPUT      YES
CONTROLS   YES
SUBCATCHMENTS ALL
NODES ALL
LINKS ALL

[TAGS]

[MAP]
DIMENSIONS -1584.362 0.000 11584.362 10000.000
Units      None

[COORDINATES]
;;Node           X-Coord            Y-Coord           
;;-------------- ------------------ ------------------
1                3573.388           1234.568          

[VERTICES]
;;Link           X-Coord            Y-Coord           
;;-------------- ------------------ ------------------

[Polygons]
;;Subcatchment   X-Coord            Y-Coord           
;;-------------- ------------------ ------------------
parkinglot       3737.997           4828.532          
parkinglot       5205.761           4362.140          
parkinglot       5521.262           5459.534          
parkinglot       4506.173           5802.469          
parkinglot       4478.738           5733.882          
parkinglot       4368.999           5706.447          
parkinglot       3998.628           5829.904          

[SYMBOLS]
;;Gage           X-Coord            Y-Coord           
;;-------------- ------------------ ------------------
07/04/11_Storm     2475.995           6790.123          


[BACKDROP]
FILE       "C:\Users\mtryby\Desktop\SWCValidation\Models\PorousPave\06 Boone\boonePrsPvmnt.jpg"
DIMENSIONS -1584.362 945.621 11584.362 9054.379


