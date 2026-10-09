import lasio
import numpy as np

FILE_LAS = "data/15_9-19A/06.LFP/159-19A_LFP.las"
FILE_CPI = "data/15_9-19A/05.PETROPHYSICAL INTERPRETATION/CPI/15_9-19_A_CPI.las"

las = lasio.read(FILE_LAS, engine="normal")
cpi = lasio.read(FILE_CPI, engine="normal")
depth = las.index
bottom = np.nanmax(depth)
stop = las.well["STOP"].value
crv = cpi.curves
print(crv)