ptf #
;UMD Bioswale storm 01/11/2006
 
[OPTIONS]
;;Option             Value
FLOW_UNITS           LPS
INFILTRATION         GREEN_AMPT
FLOW_ROUTING         DYNWAVE
LINK_OFFSETS         DEPTH
MIN_SLOPE            0
ALLOW_PONDING        YES
SKIP_STEADY_STATE    NO
 
START_DATE           01/11/2006
START_TIME           14:24:00
REPORT_START_DATE    01/11/2006
REPORT_START_TIME    14:24:00
END_DATE             01/12/2006
END_TIME             12:00:00
SWEEP_START          01/01
SWEEP_END            12/31
DRY_DAYS             0
REPORT_STEP          00:02:00
WET_STEP             00:02:00
DRY_STEP             00:02:00
ROUTING_STEP         0:00:05
 
INERTIAL_DAMPING     PARTIAL
NORMAL_FLOW_LIMITED  BOTH
FORCE_MAIN_EQUATION  H-W
VARIABLE_STEP        0.00
LENGTHENING_STEP     0
MIN_SURFAREA         1.14
MAX_TRIALS           8
HEAD_TOLERANCE       0.0015
SYS_FLOW_TOL         5
LAT_FLOW_TOL         5
MINIMUM_STEP         0.5
THREADS              1
 
[EVAPORATION]
;;Data Source    Parameters
;;-------------- ----------------
CONSTANT         0.0
DRY_ONLY         NO
 
[RAINGAGES]
;;Name           Format    Interval SCF      Source
;;-------------- --------- ------ ------ ----------
01-11-2006_Storm INTENSITY 0:01     1.0      TIMESERIES Storm73
 
[SUBCATCHMENTS]
;;Name           Rain Gage        Outlet           Area     %Imperv  Width    %Slope   CurbLen  SnowPack
;;-------------- ---------------- ---------------- -------- -------- -------- -------- -------- ----------------
Roadway          01-11-2006_Storm   LID              0.224    100      143.000000     .100000000        0
;Swale
LID              01-11-2006_Storm   Out1             0.312    0        15.76    1.6      0
 
[SUBAREAS]
;;Subcatchment   N-Imperv   N-Perv     S-Imperv   S-Perv     PctZero    RouteTo    PctRouted
;;-------------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
Roadway          .020000000       0.24       1          5          100        OUTLET
LID              0.01       0.24       0.05       5.0000000000    100        OUTLET
 
[INFILTRATION]
;;Subcatchment   Suction    Ksat       IMD
;;-------------- ---------- ---------- ----------
Roadway          99.441     #Ryhydrlc_cndctvty#      0.378
LID              275.90000 3.0000000000 #LDntl_mstr_dfct#
 
[LID_CONTROLS]
;;Name           Type/Layer Parameters
;;-------------- ---------- ----------
Swale            VS
Swale            SURFACE    2164.000000 .2000000000 .4100000000 1.600000000 3.250000000
 
[LID_USAGE]
;;Subcatchment   LID Process      Number  Area       Width      InitSat    FromImp    ToPerv     RptFile                  DrainTo
;;-------------- ---------------- ------- ---------- ---------- ---------- ---------- ---------- ------------------------ ----------------
LID              Swale            1       3120       15.76      #LDprcnt_ntlly_strtd#          100        0          ".\UMD0111.txt"
 
[OUTFALLS]
;;Name           Elevation  Type       Stage Data       Gated    Route To
;;-------------- ---------- ---------- ---------------- -------- ----------------
Out1             0          FREE                        NO
 
[TIMESERIES]
;;Name           Date       Time       Value
;;-------------- ---------- ---------- ----------
;01/11/2006 MD Grass Swale w/o Pretreatment (mm/hr)
Storm73          1/11/2006  15:46      1.91
Storm73          1/11/2006  15:47      1.91
Storm73          1/11/2006  15:48      1.91
Storm73          1/11/2006  15:49      1.91
Storm73          1/11/2006  15:50      1.91
Storm73          1/11/2006  15:51      1.91
Storm73          1/11/2006  15:52      1.91
Storm73          1/11/2006  15:53      1.91
Storm73          1/11/2006  15:54      1.91
Storm73          1/11/2006  15:55      1.91
Storm73          1/11/2006  15:56      1.91
Storm73          1/11/2006  15:57      1.9
Storm73          1/11/2006  15:58      1.91
Storm73          1/11/2006  15:59      1.91
Storm73          1/11/2006  16:0       1.9
Storm73          1/11/2006  16:1       1.9
Storm73          1/11/2006  16:2       1.91
Storm73          1/11/2006  16:3       1.9
Storm73          1/11/2006  16:4       1.91
Storm73          1/11/2006  16:5       7.62
Storm73          1/11/2006  16:6       7.62
Storm73          1/11/2006  16:7       7.62
Storm73          1/11/2006  16:8       7.62
Storm73          1/11/2006  16:9       7.62
Storm73          1/11/2006  16:10      7.62
Storm73          1/11/2006  16:11      7.62
Storm73          1/11/2006  16:12      7.62
Storm73          1/11/2006  16:13      7.62
Storm73          1/11/2006  16:14      7.62
Storm73          1/11/2006  16:15      3.81
Storm73          1/11/2006  16:16      3.81
Storm73          1/11/2006  16:17      3.81
Storm73          1/11/2006  16:18      3.81
Storm73          1/11/2006  16:19      15.24
Storm73          1/11/2006  16:20      15.24
Storm73          1/11/2006  16:21      3.81
Storm73          1/11/2006  16:22      3.81
Storm73          1/11/2006  16:23      3.81
Storm73          1/11/2006  16:24      3.81
Storm73          1/11/2006  16:25      3.81
Storm73          1/11/2006  16:26      3.81
Storm73          1/11/2006  16:27      3.81
Storm73          1/11/2006  16:28      3.81
Storm73          1/11/2006  16:29      3.81
Storm73          1/11/2006  16:30      3.81
Storm73          1/11/2006  16:31      3.81
Storm73          1/11/2006  16:32      3.81
Storm73          1/11/2006  16:33      3.81
Storm73          1/11/2006  16:34      3.81
Storm73          1/11/2006  16:35      3.81
Storm73          1/11/2006  16:36      3.81
Storm73          1/11/2006  16:37      3.81
Storm73          1/11/2006  16:38      3.81
Storm73          1/11/2006  16:39      3.81
Storm73          1/11/2006  16:40      3.81
Storm73          1/11/2006  16:41      7.62
Storm73          1/11/2006  16:42      7.62
Storm73          1/11/2006  16:43      3.81
Storm73          1/11/2006  16:44      3.81
Storm73          1/11/2006  16:45      3.81
Storm73          1/11/2006  16:46      3.81
Storm73          1/11/2006  16:47      7.62
Storm73          1/11/2006  16:48      7.62
Storm73          1/11/2006  16:49      3.81
Storm73          1/11/2006  16:50      3.81
Storm73          1/11/2006  16:51      3.81
Storm73          1/11/2006  16:52      3.81
Storm73          1/11/2006  16:53      3.81
Storm73          1/11/2006  16:54      3.81
Storm73          1/11/2006  16:55      3.81
Storm73          1/11/2006  16:56      3.81
Storm73          1/11/2006  16:57      2.54
Storm73          1/11/2006  16:58      2.54
Storm73          1/11/2006  16:59      2.54
Storm73          1/11/2006  17:0       2.54
Storm73          1/11/2006  17:1       2.54
Storm73          1/11/2006  17:2       2.54
Storm73          1/11/2006  17:3       1.52
Storm73          1/11/2006  17:4       1.52
Storm73          1/11/2006  17:5       1.52
Storm73          1/11/2006  17:6       1.52
Storm73          1/11/2006  17:7       1.52
Storm73          1/11/2006  17:8       1.52
Storm73          1/11/2006  17:9       1.52
Storm73          1/11/2006  17:10      1.52
Storm73          1/11/2006  17:11      1.52
Storm73          1/11/2006  17:12      1.52
Storm73          1/11/2006  17:13      1.52
 
[REPORT]
;;Reporting Options
INPUT      YES
CONTROLS   YES
SUBCATCHMENTS ALL
NODES ALL
LINKS ALL
 
[TAGS]
 
[MAP]
DIMENSIONS 0.000 0.000 10000.000 10000.000
Units      Meters
 
[COORDINATES]
;;Node           X-Coord            Y-Coord
;;-------------- ------------------ ------------------
Out1             8321.033           233.702
 
[VERTICES]
;;Link           X-Coord            Y-Coord
;;-------------- ------------------ ------------------
 
[Polygons]
;;Subcatchment   X-Coord            Y-Coord
;;-------------- ------------------ ------------------
Roadway          3523.985           5067.651
Roadway          4200.492           5375.154
Roadway          2490.775           8683.887
Roadway          1838.868           8314.883
LID              7915.129           676.507
LID              8124.231           811.808
LID              5405.904           5067.651
LID              5258.303           5018.450
 
[SYMBOLS]
;;Gage           X-Coord            Y-Coord
;;-------------- ------------------ ------------------
01-11-2006_Storm 3831.488           8622.386
 
 
[BACKDROP]
FILE       "\\Aa.ad.epa.gov\ord\CIN\Users\main\L-P\mplatz\Net MyDocuments\EPA\Tryby\SWMM Validation Study\Models\BioSwale\09 UMD Grass Swale\UMDSwale Background.JPG"
DIMENSIONS 205.993 0.000 9794.007 10000.000
