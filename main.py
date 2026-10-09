import lasio
import numpy as np

FILE_LAS = "data/15_9-19A/06.LFP/159-19A_LFP.las"
FILE_CPI = "data/15_9-19A/05.PETROPHYSICAL INTERPRETATION/CPI/15_9-19_A_CPI.las"

las = lasio.read(FILE_LAS, engine="normal")
cpi = lasio.read(FILE_CPI, engine="normal")
df = las.df()
df_cpi = cpi.df()
df_s = df[["LFP_BADDATA", "LFP_CALI", "LFP_GR", "LFP_RT", "LFP_RHOB", "LFP_NPHI"]]
df_s["CPI_VSH"] = df_cpi["VSH"].reindex(df_s.index, method="nearest", tolerance=0.01)



depth = las.index
bottom = np.nanmax(depth)
stop = las.well["STOP"].value
gr_zero = (df["LFP_GR"] == 0)
gr_high = (df["LFP_GR"] > 300)
nphi_spike = df["LFP_NPHI"] > 1
df_s.loc[nphi_spike, "LFP_NPHI"] = np.nan
df_s.loc[gr_zero, "LFP_GR"] = np.nan

    
#crv = cpi.curves
print(df_s.loc[3703:3705])