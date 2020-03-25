""" Plot data and save data as figures """

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
        fname=os.path.join("04-graphics-outputs", "01-double-up-gpx-data-figure.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(
        f"Saved plot as PNG: {os.path.join('04-graphics-outputs', '01-double-up-gpx-data-figure.png')}")


# Plot cadence, distinguishing up/down movement
with plt.style.context('dark_background'):

    fig, ax = plt.subplots(figsize=(20, 10))

    ax.scatter(
        vertical_up_df.time, vertical_up_df.cadence, color='green',
        label='Running Up', zorder=3, s=16)

    ax.scatter(
        vertical_down_df.time, vertical_down_df.cadence, color='purple',
        label='Running Down', zorder=2, s=16)

    plt.xlim(double_up_df_enhance.time.min(), double_up_df_enhance.time.max())

    ax.set_xlabel("Time (US Eastern)")
    ax.set_ylabel("Cadence (steps/minute)")
    ax.set_title("Mansfield Double Up Course, 2017\nCadence Throughout the Course", size=20)
    ax.xaxis.label.set_size(20)
    ax.yaxis.label.set_size(20)
    ax.title.set_size(24)
    ax.tick_params(labelsize=16)

    ax.legend(borderpad=0.75,
              edgecolor='white',
              fontsize=16,
              shadow=True)

    # Define the date format
    date_form = DateFormatter("%H:%M AM")
    ax.xaxis.set_major_formatter(date_form)

try:
    plt.savefig(
        fname=os.path.join("04-graphics-outputs", "02-double-up-gpx-data-figure.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(
        f"Saved plot as PNG: {os.path.join('04-graphics-outputs', '02-double-up-gpx-data-figure.png')}")

# Plot accumulated distance, distinguishing up/down movement
with plt.style.context('dark_background'):

    fig, ax = plt.subplots(figsize=(20, 10))

    ax.scatter(
        vertical_up_df.time, vertical_up_df.distance_mile, color='green',
        label='Running Up', zorder=3, s=16)

    ax.scatter(
        vertical_down_df.time, vertical_down_df.distance_mile, color='purple',
        label='Running Down', zorder=2, s=16)

    plt.xlim(double_up_df_enhance.time.min(), double_up_df_enhance.time.max())

    ax.set_xlabel("Time (US Eastern)")
    ax.set_ylabel("Total Distance (miles)")
    ax.set_title("Mansfield Double Up Course, 2017\nDistance Throughout the Course", size=20)
    ax.xaxis.label.set_size(20)
    ax.yaxis.label.set_size(20)
    ax.title.set_size(24)
    ax.tick_params(labelsize=16)

    ax.legend(borderpad=0.75,
              edgecolor='white',
              fontsize=16,
              shadow=True)

    # Define the date format
    date_form = DateFormatter("%H:%M AM")
    ax.xaxis.set_major_formatter(date_form)

try:
    plt.savefig(
        fname=os.path.join("04-graphics-outputs", "03-double-up-gpx-data-figure.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(
        f"Saved plot as PNG: {os.path.join('04-graphics-outputs', '03-double-up-gpx-data-figure.png')}")


# Plot normalized energry, distinguishing up/down movement
with plt.style.context('dark_background'):

    fig, ax = plt.subplots(figsize=(20, 10))

    ax.scatter(
        vertical_up_df.time, vertical_up_df.energy_norm, color='green',
        label='Running Up', zorder=3, s=16)  # , linewidth=2)

    ax.scatter(
        vertical_down_df.time, vertical_down_df.energy_norm, color='purple',
        label='Running Down', zorder=2, s=16)

    plt.xlim(double_up_df_enhance.time.min(), double_up_df_enhance.time.max())

    ax.set_xlabel("Time (US Eastern)")
    ax.set_ylabel("Normalized energy (% of max)")
    ax.set_title("Mansfield Double Up Course, 2017\nEnergy Throughout the Course", size=20)
    ax.xaxis.label.set_size(20)
    ax.yaxis.label.set_size(20)
    ax.title.set_size(24)
    ax.tick_params(labelsize=16)

    ax.legend(borderpad=0.75,
              edgecolor='white',
              fontsize=16,
              shadow=True)

    # Define the date format
    date_form = DateFormatter("%H:%M AM")
    ax.xaxis.set_major_formatter(date_form)

try:
    plt.savefig(
        fname=os.path.join("04-graphics-outputs", "04-double-up-gpx-data-figure.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(
        f"Saved plot as PNG: {os.path.join('04-graphics-outputs', '04-double-up-gpx-data-figure.png')}")

# Plot horizontal speed, distinguishing up/down movement
with plt.style.context('dark_background'):

    fig, ax = plt.subplots(figsize=(20, 10))

    ax.scatter(
        vertical_up_df.time, vertical_up_df.speed_mph, color='green',
        label='Running Up', zorder=3, s=16)  # , linewidth=2)

    ax.scatter(
        vertical_down_df.time, vertical_down_df.speed_mph, color='purple',
        label='Running Down', zorder=2, s=16)

    plt.xlim(double_up_df_enhance.time.min(), double_up_df_enhance.time.max())

    ax.set_xlabel("Time (US Eastern)")
    ax.set_ylabel("Horizontal speed (mph)")
    ax.set_title("Mansfield Double Up Course, 2017\nSpeed Throughout the Course", size=20)
    ax.xaxis.label.set_size(20)
    ax.yaxis.label.set_size(20)
    ax.title.set_size(24)
    ax.tick_params(labelsize=16)

    ax.legend(borderpad=0.75,
              edgecolor='white',
              fontsize=16,
              shadow=True)

    # Define the date format
    date_form = DateFormatter("%H:%M AM")
    ax.xaxis.set_major_formatter(date_form)

try:
    plt.savefig(
        fname=os.path.join("04-graphics-outputs", "05-double-up-gpx-data-figure.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(
        f"Saved plot as PNG: {os.path.join('04-graphics-outputs', '05-double-up-gpx-data-figure.png')}")

# Plot course lat/lon and distinguish up/down
with plt.style.context('dark_background'):

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 20))

    # Subplot 1
    double_up_gdf.plot(
        ax=ax1, markersize=2, color='r', zorder=2, label='Course')

    ax1.set_xlabel("Longitude")
    ax1.set_ylabel("Latitude")
    ax1.set_title("Mansfield Double Up Course, 2017", size=20)
    ax1.grid(True, zorder=1)
    ax1.xaxis.label.set_size(20)
    ax1.yaxis.label.set_size(20)
    ax1.title.set_size(24)
    ax1.tick_params(labelsize=16)

    ax1.legend(borderpad=0.75,
               edgecolor='white',
               fontsize=16,
               shadow=True)

    # Add course direction arrows
    ax1.annotate(
        s='Start/\nFinish',
        xy=(-72.79, double_up_df_enhance.latitude[0] + .0002),
        xytext=(-72.79, double_up_df_enhance.latitude[0] + 0.0075),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'g',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    ax1.annotate(
        s='', xy=(-72.805, 44.5225), xytext=(-72.795, 44.5275),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'purple',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    ax1.annotate(
        s='', xy=(-72.825, 44.5175), xytext=(-72.815, 44.5175),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'purple',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    ax1.annotate(
        s='', xy=(-72.835, 44.5375), xytext=(-72.835, 44.5275),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'purple',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    ax1.annotate(
        s='', xy=(-72.815, 44.54575), xytext=(-72.825, 44.54575),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'purple',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    ax1.annotate(
        s='', xy=(-72.815, 44.5375), xytext=(-72.815, 44.5425),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'purple',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    ax1.annotate(
        s='', xy=(-72.815, 44.5275), xytext=(-72.815, 44.5325),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'purple',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    ax1.annotate(
        s='', xy=(-72.815, 44.5275), xytext=(-72.815, 44.5325),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'purple',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    ax1.annotate(
        s='', xy=(-72.808, 44.5375), xytext=(-72.812, 44.5325),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'purple',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    ax1.annotate(
        s='', xy=(-72.795, 44.5375), xytext=(-72.805, 44.5425),
        arrowprops={
            'arrowstyle': '-|>',
            'lw': 3,
            'ec': 'purple',
            'shrinkA': 2},
        ha='center',
        fontsize=16)

    # Subplot 2
    double_up_gdf[double_up_gdf.vertical_speed_ft_per_sec >= 0].plot(
        ax=ax2, markersize=4, color='g', label="Running Up", zorder=3)
    double_up_gdf[double_up_gdf.vertical_speed_ft_per_sec < 0].plot(
        ax=ax2, markersize=4, color='purple', label="Running Down", zorder=2)

    ax2.legend(borderpad=0.75,
               edgecolor='white',
               fontsize=16,
               shadow=True)

    ax2.set_xlabel("Longitude")
    ax2.set_ylabel("Latitude")
    ax2.grid(True, zorder=1)
    ax2.xaxis.label.set_size(20)
    ax2.yaxis.label.set_size(20)
    ax2.title.set_size(24)
    ax2.tick_params(labelsize=16)

try:
    plt.savefig(
        fname=os.path.join("04-graphics-outputs", "06-double-up-gpx-data-figure.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(
        f"Saved plot as PNG: {os.path.join('04-graphics-outputs', '06-double-up-gpx-data-figure.png')}")

# Plot course lat/lon with cadence
with plt.style.context('dark_background'):

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 20))

    # Subplot 1
    double_up_gdf[double_up_gdf.cadence >= double_up_gdf.cadence.median()].plot(
        ax=ax1, markersize=4, color='g', label="> Median Cadence", zorder=3)
    double_up_gdf[double_up_df_enhance.cadence < double_up_df_enhance.cadence.median()].plot(
        ax=ax1, markersize=4, color='purple', label="< Median Cadence", zorder=2)

    ax1.legend(borderpad=0.75,
               edgecolor='white',
               fontsize=16,
               shadow=True)

    ax1.set_xlabel("Longitude")
    ax1.set_ylabel("Latitude")
    ax1.set_title("Mansfield Double Up Course, 2017\nCadence", size=20)
    ax1.grid(True, zorder=1)
    ax1.xaxis.label.set_size(20)
    ax1.yaxis.label.set_size(20)
    ax1.title.set_size(24)
    ax1.tick_params(labelsize=16)

    # Subplot 2
    double_up_gdf[double_up_gdf.cadence >= double_up_gdf.cadence.max()*0.75].plot(
        ax=ax2, markersize=4, color='#1a9641', label="> 75% Max Cadence", zorder=5)
    double_up_gdf[(double_up_gdf.cadence < double_up_gdf.cadence.max()*0.75) & (double_up_gdf.cadence >= double_up_gdf.cadence.max()*0.5)].plot(
        ax=ax2, markersize=4, color='#a6d96a', label="50%-75% Max Cadence", zorder=4)
    double_up_gdf[(double_up_gdf.cadence < double_up_gdf.cadence.max()*0.50) & (double_up_gdf.cadence >= double_up_gdf.cadence.max()*0.25)].plot(
        ax=ax2, markersize=4, color='#fdae61', label="25%-50% Max Cadence", zorder=3)
    double_up_gdf[double_up_gdf.cadence < double_up_gdf.cadence.max()*0.25].plot(
        ax=ax2, markersize=4, color='#d7191c', label="< 25% Max Cadence", zorder=6)

    ax2.legend(borderpad=0.75,
               edgecolor='white',
               fontsize=16,
               shadow=True)

    ax2.set_xlabel("Longitude")
    ax2.set_ylabel("Latitude")
    ax2.grid(True, zorder=1)
    ax2.xaxis.label.set_size(20)
    ax2.yaxis.label.set_size(20)
    ax2.title.set_size(24)
    ax2.tick_params(labelsize=16)

try:
    plt.savefig(
        fname=os.path.join("04-graphics-outputs", "07-double-up-gpx-data-figure.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(
        f"Saved plot as PNG: {os.path.join('04-graphics-outputs', '07-double-up-gpx-data-figure.png')}")


# Plot course lat/lon with speed
with plt.style.context('dark_background'):

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 20))

    # Subplot 1
    double_up_gdf[double_up_gdf.speed_mph >= double_up_gdf.speed_mph.median()].plot(
        ax=ax1, markersize=4, color='g', label="> Median Speed", zorder=3)
    double_up_gdf[double_up_gdf.speed_mph < double_up_gdf.speed_mph.median()].plot(
        ax=ax1, markersize=4, color='purple', label="< Median Speed", zorder=2)

    ax1.legend(borderpad=0.75,
               edgecolor='white',
               fontsize=16,
               shadow=True)

    ax1.set_xlabel("Longitude")
    ax1.set_ylabel("Latitude")
    ax1.set_title("Mansfield Double Up Course, 2017\nSpeed", size=20)
    ax1.grid(True, zorder=1)
    ax1.xaxis.label.set_size(20)
    ax1.yaxis.label.set_size(20)
    ax1.title.set_size(24)
    ax1.tick_params(labelsize=16)

    # Subplot 2
    double_up_gdf[double_up_gdf.speed_mph >= double_up_gdf.speed_mph.max()*0.75].plot(
        ax=ax2, markersize=4, color='#1a9641', label="> 75% Max Speed", zorder=5)
    double_up_gdf[(double_up_gdf.speed_mph < double_up_gdf.speed_mph.max()*0.75) & (double_up_gdf.speed_mph >= double_up_gdf.speed_mph.max()*0.5)].plot(
        ax=ax2, markersize=4, color='#a6d96a', label="50%-75% Max Speed", zorder=4)
    double_up_gdf[(double_up_gdf.speed_mph < double_up_gdf.speed_mph.max()*0.50) & (double_up_gdf.speed_mph >= double_up_gdf.speed_mph.max()*0.25)].plot(
        ax=ax2, markersize=4, color='#fdae61', label="25%-50% Max Speed", zorder=4)
    double_up_gdf[double_up_gdf.speed_mph < double_up_gdf.speed_mph.max()*0.25].plot(
        ax=ax2, markersize=4, color='#d7191c', label="< 25% Max Speed", zorder=2)

    ax2.legend(borderpad=0.75,
               edgecolor='white',
               fontsize=16,
               shadow=True)

    ax2.set_xlabel("Longitude")
    ax2.set_ylabel("Latitude")
    ax2.grid(True, zorder=1)
    ax2.xaxis.label.set_size(20)
    ax2.yaxis.label.set_size(20)
    ax2.title.set_size(24)
    ax2.tick_params(labelsize=16)

try:
    plt.savefig(
        fname=os.path.join("04-graphics-outputs", "08-double-up-gpx-data-figure.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(
        f"Saved plot as PNG: {os.path.join('04-graphics-outputs', '08-double-up-gpx-data-figure.png')}")

# Plot course lat/lon with normalized energy
with plt.style.context('dark_background'):

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 20))

    # Subplot 1
    double_up_gdf[double_up_gdf.energy_norm >= 0.5].plot(
        ax=ax1, markersize=4, color='g', label="> 50% Max Energy", zorder=3)
    double_up_gdf[double_up_gdf.energy_norm < 0.5].plot(
        ax=ax1, markersize=4, color='purple', label="< 50% Max Energy", zorder=2)

    ax1.legend(borderpad=0.75,
               edgecolor='white',
               fontsize=16,
               shadow=True)

    ax1.set_xlabel("Longitude")
    ax1.set_ylabel("Latitude")
    ax1.set_title("Mansfield Double Up Course, 2017\nEnergy", size=20)
    ax1.grid(True, zorder=1)
    ax1.xaxis.label.set_size(20)
    ax1.yaxis.label.set_size(20)
    ax1.title.set_size(24)
    ax1.tick_params(labelsize=16)

    # Subplot 2
    double_up_gdf[double_up_gdf.energy_norm >= 0.75].plot(
        ax=ax2, markersize=4, color='#1a9641', label="> 75% Max Energy", zorder=5)
    double_up_gdf[(double_up_gdf.energy_norm < 0.75) & (double_up_gdf.energy_norm >= 0.5)].plot(
        ax=ax2, markersize=4, color='#a6d96a', label="50%-75% Max Energy", zorder=5)
    double_up_gdf[(double_up_gdf.energy_norm < 0.5) & (double_up_gdf.energy_norm >= 0.25)].plot(
        ax=ax2, markersize=4, color='#fdae61', label="25%-50% Max Energy", zorder=3)
    double_up_gdf[double_up_gdf.energy_norm <= 0.25].plot(
        ax=ax2, markersize=4, color='#d7191c', label="< 25% Max Energy", zorder=2)

    ax2.legend(borderpad=0.75,
               edgecolor='white',
               fontsize=16,
               shadow=True)

    ax2.set_xlabel("Longitude")
    ax2.set_ylabel("Latitude")
    ax2.grid(True, zorder=1)
    ax2.xaxis.label.set_size(20)
    ax2.yaxis.label.set_size(20)
    ax2.title.set_size(24)
    ax2.tick_params(labelsize=16)

try:
    plt.savefig(
        fname=os.path.join("04-graphics-outputs", "09-double-up-gpx-data-figure.png"), facecolor='k', dpi=300, bbox_inches="tight")
except Exception as error:
    print(f"Could not save plot as PNG. ERROR: {error}")
else:
    print(
        f"Saved plot as PNG: {os.path.join('04-graphics-outputs', '09-double-up-gpx-data-figure.png')}")
