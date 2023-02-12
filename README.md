# unit-convert
Easily convert units to different quantities.

For conveniance, abbreviations are accepted, where an attempt will be made to calculate the type based on the other inputs (eg. "m" can evaluate as either "minute" or "metre").

> **This library is deprecated**: A recommendation is to use [pint](https://github.com/hgrecco/pint) instead.


## Example Usage
```python
>>> from unit_convert import UnitConvert

# Yards + kilometres to miles
>>> UnitConvert(yards=136.23, kilometres=60)['miles']
37.35976780046479

# Bytes to terabytes
>>> UnitConvert('b', 19849347813875, 'megabytes', 512)['tb']
18.053364951617368

# List available conversions
>>> UnitConvert(metres=1).keys()
['nm', 'nanometres', 'μm', 'micrometres', 'mm', 'millimetres', 'cm', 'centimetres', 'i', 'inches', 'ft', 'feet', 'm', 'metres', 'meters', 'yd', 'yards', 'km', 'kilometres', 'kilometers', 'miles', 'lightyears', 'au', 'astronomical_units', 'parsec']
```

Data size, time, distance, mass and temperatures are supported.
