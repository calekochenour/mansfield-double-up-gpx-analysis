# Mansfield Double Up GPX Analysis

This directory contains the code and files that produce a data science analysis of a GPX file from the [Mansfield Double Up](http://www.nativeendurance.com/mansfielddoubleup.html) mountain race in Stowe, Vermont. The project extracts data from the GPX file, processes and organizes the data, visualizes the data, and summarizes the workflow in a Jupyter Notebook.

## Prerequisites

To run this project locally, you will need:

* Conda ([Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://docs.anaconda.com/anaconda/install/))

### Binder Instructions

To run this project in a web browser, click the icon below to launch the project with Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/calekochenour/mansfield-double-up-gpx-analysis/master)

Binder will open a Jupyter Notebook in the current web browser. Click "New" and select "Terminal" to open a terminal in the project folder.

## Quickstart

### Create and Activate Conda Environment

From the terminal, you can create and activate the project Conda environment.

Create environment:

```bash
conda env create -f environment.yml
```

Activate environment:

```bash
conda activate mansfield-gpx-analysis
```

### Run the Analysis

From the terminal, you can run the analysis and produce the project outputs.

Execute the code:

```bash
make
```

## Project Contents

The project contains folders for all stages of the workflow as well as other files necessary to run the analysis.

### `01-code-scripts/`

Contains all Python scripts required to run the analysis.

### `02-raw-data/`

Contains all original/unprocessed data.

### `03-processed-data/`

Contains all processed/created data.

### `04-graphics-outputs/`

Contains all figures.

### `05-papers-writings/`

Contains all paper/report files.

### `Makefile`

Contains instructions to execute the code.

### `environment.yml`

Contains the information required to create the Conda environment.
