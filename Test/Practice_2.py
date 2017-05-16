from swmmbinreader import SWMMBinReader
output = SWMMBinReader()
output.OpenBinFile(r"/Users/surajkamble/Documents/SWMM2PEST/SWMMC-master/01-11-06/VillBTI0603.out")

LinkIDs = output._get_TimeSeries()
print(LinkIDs)
