::Purpose: Calls swmm when using two events for calibration
::Usage: swmm.bat "event1.inp event1.rpt event1.out" "event2.inp event2.rpt event2.out"

.\swmm5110_test.exe %~1
TIMEOUT /T 0.5 /NOBREAK

