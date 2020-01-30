whendidit
=========

A python script that remembers when something happened and how long it took.

* Python packaging tutorials and best practices:
  - [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/)
  - [Hitchhiker's Guide - Structuring Your Project](https://docs.python-guide.org/writing/structure/)
  - [Sample Module Repository](https://github.com/navdeep-G/samplemod)

* [Another Avro getting started](http://layer0.authentise.com/getting-started-with-avro-and-python-3.html)

```
import whendidit

whendidit.happen("Meeting starts")
whendidit.happen("First slide")
whendidit.happen("Meeting ends")
whendidit.readAll()
```