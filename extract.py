"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, mode="r") as neo_file:
        csvreader = csv.reader(neo_file)
        # Skip Header
        next(csvreader)
        for line in csvreader:
            data = {}
            data["designation"] = line[3]
            data["name"] = None if line[4] == "" else line[4]
            data["diameter"] = line[15]
            data["hazardous"] = True if line[7].strip().upper() == "Y" else False
            neos.append(NearEarthObject(data))

    return neos


def load_approaches(cad_json_path="data/cad.json"):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path, mode="r") as cad_file:
        for rec in json.load(cad_file)["data"]:
            data = {}
            data["designation"] = rec[0]
            data["time"] = rec[3]
            data["distance"] = rec[4]
            data["velocity"] = rec[7]
            approaches.append(CloseApproach(data))

    return approaches
