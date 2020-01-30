import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json
import os.path
import time

schema = avro.schema.Parse(json.dumps(
    {
        "namespace": "com.skraba.whendidit",
        "type": "record",
        "name": "Event",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "start", "type": "long"},
            {"name": "duration", "type": "long"}
        ]
    }))


def happen(name, start=None, duration=0, filename="/tmp/events.avro"):
    """Write an event in the file."""
    if start is None:
        start = int(time.time() * 1000.0)

    # Set to None to append
    create_schema = None if os.path.isfile(filename) else schema

    writer = DataFileWriter(open(filename, "a+b"), DatumWriter(), create_schema)
    writer.append({"name": name, "start": start, "duration": duration})
    writer.close()


def readAll(filename="/tmp/events.avro"):
    reader = DataFileReader(open(filename, "rb"), DatumReader())
    for user in reader:
        print(user)
    reader.close()
