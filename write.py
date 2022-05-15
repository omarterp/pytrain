"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
import os


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    header =  ['datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous']
    with open(filename, mode="w") as csv_file:
        approach_writer = csv.DictWriter(csv_file, delimiter=",", quotechar="\"", 
                                     quoting=csv.QUOTE_MINIMAL, fieldnames=header)
        # approach_writer.writerow(header)
        approach_writer.writeheader()
        for approach in results:
            approach_writer.writerow(flatten_approach(approach.serialize()))

        def serialize(self):
            """Return serialized json string"""
            neo = dict(designation=self.designation, name=self.name,
                        diameter_km="NaN" if math.isnan(self.diameter) else self.diameter,
                        poptentially_hazardous=self.hazardous)

        def serialize(self):
            """Return serialized json string"""
            approach = dict(datetime_utc=helpers.datetime_to_str(self.time),
                            distance_au=self.distance, velocity_km_s=self.velocity,
                            neo=self.neo.serialize())
            return approach


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # if filename == None or not isinstance(filename, str):
    #     raise ValueError(f"filename must be a string: filename:{filename}")
    approaches = []
    for approach in results:
        approaches.append(approach.serialize())

    with open(filename, mode="w") as json_file:
        json.dump(approaches, json_file)


def flatten_approach(approach:dict) -> dict:
    """Flatten approach to facilitate writing to a csv.

    :param approach: A serialized approach, represented by a dictionary.
    """
    return dict(datetime_utc=approach["datetime_utc"],
                distance_au=approach["distance_au"],
                velocity_km_s=approach["velocity_km_s"],
                designation=approach["neo"]["designation"],
                name=approach["neo"]["name"],                         
                diameter_km=approach["neo"]["diameter_km"],
                potentially_hazardous=approach["neo"]["potentially_hazardous"])