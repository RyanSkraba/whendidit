from unittest import TestCase

import avro
import os
import tempfile
import whendidit

class TestHappen(TestCase):

    def test_adds_to_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            filename = os.path.join(tmp_dir, 'events.avro')

            # Add one event to the file.
            s = whendidit.happen("One", 123, 456, filename)

            reader = avro.datafile.DataFileReader(open(filename, "rb"), avro.io.DatumReader())
            events = [user for user in reader]
            reader.close()
            self.assertEqual(len(events), 1)

            # Add another event to the same file.
            s = whendidit.happen("Two", 234, 567, filename)

            reader = avro.datafile.DataFileReader(open(filename, "rb"), avro.io.DatumReader())
            events = [user for user in reader]
            reader.close()
            self.assertEqual(len(events), 2)
