**Cale Kochenour** \
April 2020

# Extracting and Analyzing GPX Data from the Mansfield Double Up

## 1.0 Problem

This analysis attempts to answer the following questions: What is the nature of metrics for a runner in the Mansfield Double Up, and how do these metrics vary throughout the race?

## 2.0 Background

The [Mansfield Double Up](http://www.nativeendurance.com/mansfielddoubleup.html) is a trail/mountain race in Stowe, Vermont, hosted by [Native Endurance](http://www.nativeendurance.com/). This race covers ~11 miles and ~5,000 feet of elevation gain/loss. The "Double Up" is a very appropriate name; the race starts and finishes at the same point and ascends Mount Mansfield (Vermont's highest mountain) from both the East and West sides throughout the race. In addition, runners are almost always running up or down, and very little of the course covers flat terrain.

I have had the privilege of running this race from the inaugural year in 2016 through 2018. Beyond understanding the qualitative physical effort required complete the race, I am intrigued about what insights GPX data can offer about the quantitative nature of the course.

The GPX file analyzed in the project was provided by [Native Endurance](http://www.nativeendurance.com/), and it contains data from a runner who completed the race in 2017. Understanding what physical metrics are captured in this data and how they vary throughout the race provides a quantitative look at the race, beyond just the latitude, longitude, and overall time the runner took to complete the race.

## 3.0 Assumptions

This analysis assumes the GPX data is accurate, and any uncertainties form this data will be carried throughout the analysis. In addition, no data was changed or omitted from the analysis; the project analyzes the raw data.

## 4.0 Techniques and Tools

### 4.1 Techniques

The workflow uses the following techniques to solve the problem:

* Extract GPX data;
* Process GPX data;
* Visualize GPX data; and,
* Upload data to ArcGIS Online.

### 4.2 Tools

The analysis uses the following packages and classes, as imported in Section 5.1:

* *os*
* *sys*
* *re*
* *datetime*
* *matplotlib.pyplot*
* *matplotlib.dates*
* *pandas*
* *pandas.plotting*
* *geopandas*
* *gpxpy*
* *arcgis*
* *arcgis.gis*

## 5.0 Solution

### 5.1 Package Imports

This section imports all packages and classes that are necessary to run the notebook and complete the analysis.

### 5.2 Function Definitions

This section defines functions that allow for extracting GPX data and uploading files to ArcGIS Online (AGOL).

### 5.3 Environment Setup/User Input

This section contains all of the variables that can be configured to fit a different user's computer and operating system. These variables include the working directory, paths to the GPX file, course zip file, and course shapefile, and the AGOL user name. In addition, a user can change the environmental variables for ArcGIS Pro authentication.

### 5.5 GPX Data Processing

This section creates a copy of the dataframe from the previous section in order to make changes to the representation of the data. No data points were changed or omitted. The following list identifies the changes made to the representation of the data so that it could be interpreted further and plotted:

* Added elevation in feet (default elevation in meters);
* Converted *datetime* objects to a plottable format;
* Changed the hour in the *datetime* to reflect US Eastern time (timezone of the race);
* Added distance in miles (default distance in meters);
* Removed the altitude attribute (duplicate of elevation attribute);
* Normalized the energy so that the maximum value was set to 1 (original units unknown);
* Added speed in miles per hour; and,
* Added vertical speed in feet per second.

The workflow creates two additional dataframes, containing data points where the runner was running up and running down, respectively. These were created to plot the attributes over time while also visually encoding the data with the runner's vertical speed, to show which parts of the race the runner was ascending and descending the mountain.

The workflow also creates a geodataframe with *geopandas* in order to plot the course route and show how the GPX attributes vary throughout the course.

### 5.6 GPX Data Visualization

This section creates visualizations for the GPX data over time and throughout the course.

#### 5.6.1 Data Attribute Plots

This section plots the raw data (cadence, distance, energy, speed, vertical speed, elevation) over time, to see how each varies as the runner completes the course. The first plot contains subplots for all six attributes and how they vary throughout the course. The following four plots show cadence, energy, distance, and speed, and are visually encoded with the runner's vertical speed (ascending or descending).

**PLOTS HERE**

Raw attribute data:
![Plot 1](04-graphics-outputs/01-double-up-gpx-data-figure.png)

![Plot 2](04-graphics-outputs/02-double-up-gpx-data-figure.png)

![Plot 3](04-graphics-outputs/03-double-up-gpx-data-figure.png)

![Plot 4](04-graphics-outputs/04-double-up-gpx-data-figure.png)

![Plot 5](04-graphics-outputs/05-double-up-gpx-data-figure.png)


#### 5.6.2 Course Plots

This section first plots the course route (with latitude/longitude) and adds arrows that indicate the course direction. In a second subplot, the workflow plots the course route again, with a visual encoding of the runner's vertical speed, indicating whether the runner is ascending or descending the mountain.

The workflow then plots cadence, speed, and energy throughout the course route, and visually encodes the route relative to the respective attribute median values (> median, < median) and maximum values (> 75% max, 50-75% max, 25-50% max, < 25% max). These plots show how the attributes vary throughout the course itself, as opposed to over time.  


**PLOTS HERE**

![Plot 6](04-graphics-outputs/06-double-up-gpx-data-figure.png)

![Plot 7](04-graphics-outputs/07-double-up-gpx-data-figure.png)

![Plot 8](04-graphics-outputs/08-double-up-gpx-data-figure.png)

![Plot 9](04-graphics-outputs/09-double-up-gpx-data-figure.png)

## 6.0 Risk Assessment

This analysis assumed that the GPX data was accurate, and the workflow did not alter or omit any data points. Any inconsistencies, uncertainty, or bias within the GPX data was carried throughout the workflow, which could have affected the data visualizations.

## 7.0 Conclusion

This analysis set out to answer the following questions: What is the nature of metrics for a runner in the Mansfield Double Up, and how do these metrics vary throughout the race?

In parsing the GPX file and visualizing the data, this workflow produced a quantitative analysis of the latitude, longitude, elevation, cadence, distance, energy, horizontal speed, and vertical speed for a typical runner throughout completion of the Mansfield Double Up.
