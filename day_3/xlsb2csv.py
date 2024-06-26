from time import time
import pandas as pd
t_start = time()
print(f"{t_start=}")
df = pd.read_excel("RIRS_RP_KOT_W_WORKU.xlsb", engine="pyxlsb")
t_xlsb = time()
print(f"{t_xlsb=} / {t_xlsb-t_start=}")
# df.to_csv("rirs.csv", date_format='%Y%m%d %H:%m')
df.to_csv("rirs.csv")
t_csv = time()
print(f"{t_csv=} / {t_csv-t_start=}")
