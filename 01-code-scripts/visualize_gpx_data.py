""" """

# Imports
import os
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pandas as pd
import geopandas as gpd
from pandas.plotting import register_matplotlib_converters

# Datetime converters; matplotlib/pandas
register_matplotlib_converters()

# Define path to enhanced GPX attributes CSV
gpx_attributes_enhance_csv = os.path.join(
    "03-processed-data", "mansfield-double-up-course-data-enhanced.csv")

# Load enhanced GPX attributes into dataframe
double_up_df_enhance = pd.read_csv(
    filepath_or_buffer=gpx_attributes_enhance_csv, delimiter=',', header=0, parse_dates=['time'])

# Create dataframes for UP (vertical speed >= 0)
#  and DOWN (vertical speed < 0); for plotting purposes
vertical_up_df = double_up_df_enhance[
    double_up_df_enhance.vertical_speed_ft_per_sec >= 0]

vertical_down_df = double_up_df_enhance[
    double_up_df_enhance.vertical_speed_ft_per_sec < 0]

# Create geodataframe from dataframe; for plotting purposes
crs = {'init': 'epsg:4326'}
double_up_gdf = gpd.GeoDataFrame(
    double_up_df_enhance,
    geometry=gpd.points_from_xy(
        double_up_df_enhance.longitude,
        double_up_df_enhance.latitude)
)

# Drop latitude/longitude (redundant with geometry)
double_up_gdf.drop(columns=["latitude", "longitude"], inplace=True)

""" Plotting """
# Plot all raw data attributes over time
with plt.style.context('dark_background'):

    fig, ax = plt.subplots(6, 1, figsize=(20, 20))

    plt.suptitle("Mansfield Double Up, 2017\nCourse Route Attributes", size=24)

    plt.subplots_adjust(hspace=0.5)

    ax[0].plot(
        double_up_df_enhance.time, double_up_df_enhance.cadence,
        label='Cadence', lw=1.5)

    ax[1].plot(
        double_up_df_enhance.time, double_up_df_enhance.distance_mile,
        label='Distance', lw=1.5)
    ax[1].fill_between(
        double_up_df_enhance.time, double_up_df_enhance.distance_mile, alpha=0.5)

    ax[2].plot(
        double_up_df_enhance.time, double_up_df_enhance.energy_norm,
        label='Normalized Energy', lw=1.5)

    ax[3].plot(
        double_up_df_enhance.time, double_up_df_enhance.speed_mph,
        label='Speed', lw=1.5)

    ax[4].plot(
        double_up_df_enhance.time, double_up_df_enhance.vertical_speed_ft_per_sec,
        label='Vertical Speed', lw=1.5, zorder=2)

    ax[5].plot(double_up_df_enhance.time, double_up_df_enhance.elevation_ft,
               label='Elevation', lw=1.5)

    # Define the date format
    date_form = DateFormatter("%H:%M AM")

    ax[0].set_ylabel("Cadence\n(steps/minute)")
    ax[1].set_ylabel("Total distance\n(miles)")
    ax[2].set_ylabel("Normalized energy\n(fraction of max)")
    ax[3].set_ylabel("Horizontal Speed\n(mph)")
    ax[4].set_ylabel("Vertical Speed\n(feet/second)")
    ax[5].set_ylabel("Elevation\n(feet)")

    for axes in ax:
        axes.xaxis.set_major_formatter(date_form)
        axes.legend(loc='best',
                    borderpad=0.75,
                    edgecolor='white',
                    fontsize=12,
                    shadow=True)
        axes.xaxis.label.set_size(14)
        axes.yaxis.label.set_size(14)
        axes.title.set_size(24)
        axes.tick_params(labelsize=12)
        axes.set_xlabel("Time (US Eastern)")


""" Save plots as figures """
try:
    plt.savefig(
        fname=os.path.join("04-graphics-outputs", "double-up-raw-attributes.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(f"Saved plot as PNG: 04-graphics-outputs", "double-up-raw-attributes.png")
