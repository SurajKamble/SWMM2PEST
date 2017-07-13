Open <b>SWMM2PEST.exe</b> to run the application.

<b>Prerequisites</b>

1.	Add PEST to path in environmental variables.
2.	Add SWMM to path in environmental variables. SWMM2PEST is not compatible with the latest version of SWMM i.e., 5.1.012 because of some issues. Please use the previous version of SWMM or use SWMM5110_test.exe provided with SWMM2PEST.

<b>Parameter Data Section</b>

1.	Provide SWMM input file (.inp).
2.	Make sure the output file name mentioned in the input file represents the output file location. 
3.	Click on the subcatchment/LID name to display the parameter and their values.
4.	Click on the parameter value label that you want to select for estimation. A dialog box will be displayed.
5.	Enter the lower and upper bound for the selected parameter.
6.	After finishing click “Ok”.

<b>Observation Data Section</b>

1.	Provide SWMM output file (.txt).
2.	Select the output parameter for PEST to calibrate against i.e., the output parameter for which you have the measured or field values.

<b>Control Data Section</b>

1.	Provide the file containing measured or field values for the selected output parameter.
2.	The field values’ time stamp must begin with start time of the output file.
