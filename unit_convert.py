# -*- coding: UTF-8 -*-
"""Easy way of converting units."""

from __future__ import division

__version__ = '1.1.0'

from collections import defaultdict, namedtuple
from copy import deepcopy


class Unit:
    Data = 0
    Distance = 1
    Time = 3
    Mass = 4
    Temperature = 5


ConversionValue = namedtuple('ConversionValue', 'value offset', defaults=[0])


class UnitConvert(object):
    Data = {
        'b': {
            Unit.Data: ConversionValue(1),
        },
        'bytes': {
            Unit.Data: ConversionValue(1),
        },
        'kb': {
            Unit.Data: ConversionValue(1024),
        },
        'kilobytes': {
            Unit.Data: ConversionValue(1024),
        },
        'mb': {
            Unit.Data: ConversionValue(1048576),
        },
        'megabytes': {
            Unit.Data: ConversionValue(1048576),
        },
        'gb': {
            Unit.Data: ConversionValue(1073741824),
        },
        'gigabytes': {
            Unit.Data: ConversionValue(1073741824),
        },
        'tb': {
            Unit.Data: ConversionValue(1099511627776),
        },
        'terabytes': {
            Unit.Data: ConversionValue(1099511627776),
        },
        'pb': {
            Unit.Data: ConversionValue(1125899906842624),
        },
        'petabytes': {
            Unit.Data: ConversionValue(1125899906842624),
        },
        'nm': {
            Unit.Distance: ConversionValue(0.000000001),
        },
        'nanometres': {
            Unit.Distance: ConversionValue(0.000000001),
        },
        'μm': {
            Unit.Distance: ConversionValue(0.000001),
        },
        'micrometres': {
            Unit.Distance: ConversionValue(0.000001),
        },
        'mm': {
            Unit.Distance: ConversionValue(0.001),
        },
        'millimetres': {
            Unit.Distance: ConversionValue(0.001),
        },
        'cm': {
            Unit.Distance: ConversionValue(0.01),
        },
        'centimetres': {
            Unit.Distance: ConversionValue(0.01),
        },
        'i': {
            Unit.Distance: ConversionValue(0.0254),
        },
        'inches': {
            Unit.Distance: ConversionValue(0.0254),
        },
        'ft': {
            Unit.Distance: ConversionValue(0.3048),
        },
        'feet': {
            Unit.Distance: ConversionValue(0.3048),
        },
        'm': {
            Unit.Distance: ConversionValue(1),
            Unit.Time: ConversionValue(60),
        },
        'metres': {
            Unit.Distance: ConversionValue(1),
        },
        'meters': {
            Unit.Distance: ConversionValue(1),
        },
        'yd': {
            Unit.Distance: ConversionValue(0.914400),
        },
        'yards': {
            Unit.Distance: ConversionValue(0.914400),
        },
        'km': {
            Unit.Distance: ConversionValue(1000),
        },
        'kilometres': {
            Unit.Distance: ConversionValue(1000),
        },
        'kilometers': {
            Unit.Distance: ConversionValue(1000),
        },
        'miles': {
            Unit.Distance: ConversionValue(1609.34),
        },
        'lightyears': {
            Unit.Distance: ConversionValue(9460528405000000),
        },
        'au': {
            Unit.Distance: ConversionValue(149598550000),
        },
        'astronomical_units': {
            Unit.Distance: ConversionValue(149598550000),
        },
        'parsec': {
            Unit.Distance: ConversionValue(30856776000000000),
        },
        'ns': {
            Unit.Time: ConversionValue(0.000000001),
        },
        'nanoseconds': {
            Unit.Time: ConversionValue(0.000000001),
        },
        'μs': {
            Unit.Time: ConversionValue(0.000001),
        },
        'microseconds': {
            Unit.Time: ConversionValue(0.000001),
        },
        'ms': {
            Unit.Time: ConversionValue(0.001),
        },
        'milliseconds': {
            Unit.Time: ConversionValue(0.001),
        },
        'seconds': {
            Unit.Time: ConversionValue(1),
        },
        's': {
            Unit.Time: ConversionValue(1),
        },
        'minutes': {
            Unit.Time: ConversionValue(60),
        },
        'hours': {
            Unit.Time: ConversionValue(3600),
        },
        'h': {
            Unit.Time: ConversionValue(3600),
        },
        'days': {
            Unit.Time: ConversionValue(86400),
        },
        'd': {
            Unit.Time: ConversionValue(86400),
        },
        'weeks': {
            Unit.Time: ConversionValue(604800),
        },
        'w': {
            Unit.Time: ConversionValue(604800),
        },
        'months': {
            Unit.Time: ConversionValue(2627424),
        },
        'years': {
            Unit.Time: ConversionValue(31536000),
        },
        'y': {
            Unit.Time: ConversionValue(31536000),
        },
        'decades': {
            Unit.Time: ConversionValue(315360000),
        },
        'centurys': {
            Unit.Time: ConversionValue(3153600000),
        },
        'g': {
            Unit.Mass: ConversionValue(1),
        },
        'grams': {
            Unit.Mass: ConversionValue(1),
        },
        'kg': {
            Unit.Mass: ConversionValue(10000),
        },
        'kilograms': {
            Unit.Mass: ConversionValue(10000),
        },
        'oz': {
            Unit.Mass: ConversionValue(28.349523),
        },
        'ounces': {
            Unit.Mass: ConversionValue(28.349523),
        },
        'lbs': {
            Unit.Mass: ConversionValue(453.59237),
        },
        'pounds': {
            Unit.Mass: ConversionValue(453.59237),
        },
        't': {
            Unit.Mass: ConversionValue(1000000),
        },
        'tons': {
            Unit.Mass: ConversionValue(907185),
        },
        'tonnes': {
            Unit.Mass: ConversionValue(1000000),
        },
        'st': {
            Unit.Mass: ConversionValue(6350.29318),
        },
        'stones': {
            Unit.Mass: ConversionValue(6350.29318),
        },
        'k': {
            Unit.Temperature: ConversionValue(1, 273.15),
        },
        'kelvin': {
            Unit.Temperature: ConversionValue(1, 273.15),
        },
        'c': {
            Unit.Temperature: ConversionValue(1),
        },
        'celcius': {
            Unit.Temperature: ConversionValue(1),
        },
        'f': {
            Unit.Temperature: ConversionValue(5 / 9, 32),
        },
        'farenheit': {
            Unit.Temperature: ConversionValue(5 / 9, 32),
        },
    }

    def __init__(self, *args, **kwargs):
        """Convert input kwargs into a sum of possible output values.

        It does this by keeping track of the possible "types" (eg. "m"
        can be metre or minute). By then providing another keyword such
        as "cm", it's obvious time is not intended.

        Multiple inputs of the same type will be added together.

        Args:
            Unit type followed by its size.
            Example: UnitConvert('bytes', 52, 'mb', 1)

        Kwargs:
            Unit types and their size.
            Example: UnitConvert(bytes=52, mb=1)
        """
        self._types = None
        self._totals = defaultdict(int)

        # Convert args to kwargs
        unit_type = None
        for i, item in enumerate(args):
            if i % 2:
                if unit_type in kwargs:
                    kwargs[unit_type] += item
                else:
                    kwargs[unit_type] = item
            else:
                unit_type = item

        # Get value from kwargs (eg. {"bytes": 123, "mb": 1})
        for unit, value in kwargs.items():
            unit = unit.lower()
            if unit in self.Data:
                unit_data = self.Data[unit]

                # Find common type
                unit_types = set(unit_data.keys())
                if self._types is None:
                    self._types = unit_types
                else:
                    self._types &= unit_types

                # Add to totals
                for value_type, conversion_value in unit_data.items():
                    self._totals[value_type] += float((value - conversion_value.offset) * conversion_value.value)

        if not self._types:
            raise ValueError('input values do not have a common type')

    def _op(self, value, op):
        """Perform an operation to combine two UnitConvert instances."""
        if not isinstance(value, UnitConvert):
            raise TypeError('must be a UnitConvert instance')

        new = deepcopy(self)
        new._types &= value._types
        if not new._types:
            raise ValueError('no common types')

        for k, v in value._totals.items():
            new._totals[k] = getattr(new._totals[k], op)(v)

        return new

    def __add__(self, value):
        """Add two UnitConvert instances together."""
        return self._op(value, '__add__')

    def __sub__(self, value):
        """Subtract one UnitConvert instance from another."""
        return self._op(value, '__sub__')

    def __mul__(self, value):
        """Multiply all values by an amount."""
        new = deepcopy(self)
        for k in new._totals:
            new._totals[k] *= value
        return new
    __rmul__ = __mul__

    def __floordiv__(self, value):
        """Divide all values by an amount."""
        new = deepcopy(self)
        for k in new._totals:
            new._totals[k] //= value
        return new

    def __rfloordiv__(self, value):
        """Divide all values by an amount."""
        new = deepcopy(self)
        for k in new._totals:
            new._totals[k] = value // new._totals[k]
        return new

    def __truediv__(self, value):
        """Divide all values by an amount."""
        new = deepcopy(self)
        for k in new._totals:
            new._totals[k] /= value
        return new

    def __rtruediv__(self, value):
        """Divide all values by an amount."""
        new = deepcopy(self)
        for k in new._totals:
            new._totals[k] = value / new._totals[k]
        return new

    def __pow__(self, value):
        """Raise all values to a power."""
        new = deepcopy(self)
        for k in new._totals:
            new._totals[k] **= value
        return new

    def __rpow__(self, value):
        """Raise a number to the power of all values."""
        new = deepcopy(self)
        for k in new._totals:
            new._totals[k] = value ** new._totals[k]
        return new

    def __getattr__(self, attr):
        """Convert to an output value.

        This is left in for legacy purposes but `__getitem__` is
        recommended instead.
        """
        if attr in self.Data:
            return self.__getitem__(attr)
        return super(UnitConvert, self).__getattribute__(attr)

    def __getitem__(self, item):
        """Convert to an output value."""
        possible_units = set(self.Data.get(item, {})) & self._types

        # An invalid unit was chosen
        if not possible_units:
            raise ValueError('unable to convert to "{}"'.format(item))

        # There's too many types to guess
        # One example would be "m" to "m"
        if len(possible_units) > 1:
            raise ValueError('unit type not clear')
        unit = possible_units.pop()

        original_value = self._totals[unit]
        conversion_value = self.Data[item][unit]
        return original_value / conversion_value.value + conversion_value.offset

    def keys(self):
        """Return a list of all available unit types."""
        return [k for k, v in self.Data.items() if self._types & set(v)]

    def values(self):
        """Return a list of all available unit values."""
        return list(map(self.__getitem__, self.keys()))

    def items(self):
        """Return a mapping of unit types to values."""
        keys = self.keys()
        return dict(zip(keys, map(self.__getitem__, keys)))

    def get(self, item, default=None):
        """Get a conversion if available or fallback to the default value."""
        try:
            return self.__getattr__(item)
        except ValueError:
            return default
