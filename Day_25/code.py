import numpy as np
import pandas as pd

ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser.rename("alphabets")
# using series attribute
ser.name = "other_name"
print(ser)
print(ser[:5])

ser_df = pd.DataFrame(ser)
ser_df.reset_index()

# using pandas to_frame()
ser_df = ser.to_frame().reset_index()
print(ser_df)