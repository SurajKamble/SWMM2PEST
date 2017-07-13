time_series = "E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\Time_Series.txt"
measured = "E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\Measured.txt"
before_calibration = "E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\Before_Calibration.txt"
after_calibration = "E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\After_Calibration.txt"


with open(time_series, 'r') as time_series_fname:

    time_series_data = time_series_fname.readlines()


for i in range(len(time_series_data)):
    time_series_data[i] = (time_series_data[i].strip())


print("Time Series Data:")
print(time_series_data)
print(len(time_series_data))



with open(measured, 'r') as measured_fname:

    measured_data = measured_fname.readlines()

for i in range(len(measured_data)):
    measured_data[i] = float(measured_data[i].strip())

print("Measured Data:")
print(len(measured_data))
print(measured_data)


with open(before_calibration, 'r') as before_calibration_fname:

    before_calibration_data = before_calibration_fname.readlines()

for i in range(len(before_calibration_data)):
    before_calibration_data[i] = float(before_calibration_data[i].strip())

print("Before Calibration Data:")
print(len(before_calibration_data))
print(before_calibration_data)


with open(after_calibration, 'r') as after_calibration_fname:

    after_calibration_data = after_calibration_fname.readlines()

for i in range(len(after_calibration_data)):
    temp = (after_calibration_data[i].strip("-\n"))

    after_calibration_data[i] = float(temp)

print("After Calibration Data:")
print(len(after_calibration_data))
print(after_calibration_data)
