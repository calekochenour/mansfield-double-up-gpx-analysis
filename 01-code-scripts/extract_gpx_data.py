""" Extracts data from GPX file and writes data to CSV """

# Imports
import os
import pandas as pd
import mansfield_gpx as mfx

# Define relative path to GPX file
double_up_gpx_path = os.path.join(
    "02-raw-data", "mansfield-double-up-course.gpx")

# Define list of GPX attributes
attribute_list = [
    "latitude", "longitude", "elevation", "time",
    "cadence", "distance", "altitude", "energy",
    "speed", "verticalSpeed"
]

# Extract gpx data to dataframe
double_up_gpx_df = pd.DataFrame({
    attribute: mfx.extract_gpx_data(double_up_gpx_path, attribute)
    for attribute in attribute_list
})

# Write extracted GPX data to CSV
df_out_path = os.path.join(
    "03-processed-data", "mansfield-double-up-course-data.csv")

try:
    double_up_gpx_df.to_csv(
        path_or_buf=df_out_path, sep=',', header=True, index=False)
except Exception as error:
    print(f"Could not write to CSV. ERROR: {error}")
else:
    print(f"Wrote GPX attributes to CSV: {df_out_path}")
