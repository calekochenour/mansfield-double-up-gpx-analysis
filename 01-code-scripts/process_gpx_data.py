""" Enhances GPS attribute data and write the enhanced data to a CSV """

# Imports
import os
from datetime import datetime
import pandas as pd

""" Enhance data """
# Define path to GPX attributes CSV
gpx_attributes_csv = os.path.join(
    "03-processed-data", "mansfield-double-up-course-data.csv")

# Load GPX attributes into dataframe
double_up_df_enhance = pd.read_csv(
    filepath_or_buffer=gpx_attributes_csv, delimiter=',', header=0)

# Add elevation in feet
double_up_df_enhance["elevation_ft"] = double_up_df_enhance.elevation.apply(
    lambda x: x * 3.28084)

# Convert dateime object to plottable format (remove timezone)
double_up_df_enhance.time = double_up_df_enhance.time.apply(
    lambda x: datetime.strptime(str(x).replace('+00:00', ''), '%Y-%m-%d %H:%M:%S'))

# Change time to US Eastern, subtract 4 from timestamp hour
double_up_df_enhance.time = double_up_df_enhance.time.apply(
    lambda x: x.replace(hour=x.hour-4))

# Add distance in miles
double_up_df_enhance["distance_mile"] = double_up_df_enhance.distance.apply(
    lambda x: x / 1609.344)

# Drop altitude column (copy of elevation)
double_up_df_enhance.drop(columns='altitude', inplace=True)

# Normalize energy (units unknown)
double_up_df_enhance["energy_norm"] = double_up_df_enhance.energy.apply(
    lambda x: x / double_up_df_enhance.energy.max())

# Add speed in miles per hour
double_up_df_enhance["speed_mph"] = double_up_df_enhance.speed.apply(
    lambda x: x * 2.236936)

# Add vertical speed in ft/second
double_up_df_enhance["vertical_speed_ft_per_sec"] = double_up_df_enhance.verticalSpeed.apply(
    lambda x: x * 3.28084)

""" Write enhanced data to CSV files"""
# Write enhanced data to CSV
df_enhance_out_path = os.path.join(
    "03-processed-data", "mansfield-double-up-course-data-enhanced.csv")

try:
    double_up_df_enhance.to_csv(
        path_or_buf=df_enhance_out_path, sep=',', header=True, index=False)
except Exception as error:
    print(f"Could not write to CSV. ERROR: {error}")
else:
    print(f"Wrote GPX attributes to CSV: {df_enhance_out_path}")
