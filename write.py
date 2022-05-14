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
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    header =  ['datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous']
    with open(filename, mode="w") as csv_file:
        approach_writer = csv.DictWriter(csv_file, delimiter=",", quotechar="\"", 
                                     quoting=csv.QUOTE_MINIMAL, fieldnames=header)
        # approach_writer.writerow(header)
        approach_writer.writeheader()
        for approach in results:
            approach_writer.writerow(get_approach_output(approach))

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

            approach_writer.writerow(approach)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    # file_name = filename if filename else "search_results.json"
    # print(results)
    with open(filename, mode="w") as json_file:
        if (results is None) or (results and len(results) == 0):
            json_file.write("[]")
        else:
            json_file.write("[")

            for approach in results:
                # print(f"json: {json.dumps(get_approach_output(approach))}")
                json_file.write(json.dumps(get_approach_output(approach)))

                if any(True for _ in results):
                    json_file.write(f",{os.linesep}")

            json_file.write("]")


def get_approach_output(approach:dict) -> dict:
    approach = approach.serialize()
    return dict(datetime_utc=approach["datetime_utc"],
                distance_au=approach["distance_au"],
                velocity_km_s=approach["velocity_km_s"],
                designation=approach["neo"]["designation"],
                name=approach["neo"]["name"],                                    
                diameter_km=approach["neo"]["diameter_km"],
                potentially_hazardous=approach["neo"]["potentially_hazardous"])
