import re
import gpxpy


def extract_gpx_data(gpx_file_path, attribute='elevation'):
    """Reads in a GPX file and returns a list of values
    for a specified GPX attribute.

    Parameters
    ----------
    gpx_file_path : str
        File path to the GPX file (.gpx extension).

    attribute: str
        Name of the attribute to extract. Default
        value is 'elevation'. Must match one of the
        entries in the function-defined list.

    Returns
    -------
    data : list
        List containing float values of the extracted
        GPX attributes.
    """
    # Open GPX file in context manager and parse with gpxpy
    with open(gpx_file_path) as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    # Define GPX main attributes
    primary_attributes = [
        "latitude",
        "longitude",
        "elevation",
        "time"
    ]

    # Define GPX extension attributes
    secondary_attributes = [
        "cadence", "distance", "altitude",
        "energy", "speed", "verticalSpeed"
    ]

    # Check if specified attribute is in main
    #  GPX attributes (lat/lon/elevation/time)
    if attribute in primary_attributes:

        # Create list of values for attribute
        data = [{
            "latitude": point.latitude,
            "longitude": point.longitude,
            "elevation": point.elevation,
            "time": point.time
        }.get(attribute)
            for track in gpx.tracks
            for segment in track.segments
            for point in segment.points
        ]

        print(f"SUCCESS: Added {attribute} data to dictionary.")

    # Check if specified attribute is in
    #  GPX extensions (cadence/distance/altitude
    #  /energy/speed/verticalSpeed)
    elif attribute in secondary_attributes:

        # Define pattern for attribute to match on
        pattern = re.compile(f"^.*{attribute}.*$")

        # Create list of values for attribute
        data = [
            float(extension.text)
            for track in gpx.tracks
            for segment in track.segments
            for point in segment.points
            for extension in point.extensions
            if pattern.match(extension.tag)
        ]

        print(f"SUCCESS: Added {attribute} data to dictionary.")

    else:
        data = []
        print("Invalid attribute. Must be one of the following: "
              "latitude, longitude, elevation, time, cadence "
              "distance, altitude, energy, speed, verticalSpeed.")

    # List of attribute values
    return data
