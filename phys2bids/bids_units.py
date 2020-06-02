import logging

LGR = logging.getLogger(__name__)

unit_aliases = {
                # kelvin: thermodynamic temperature
                'k': 'K', 'kelvin': 'K', 'kelvins': 'K',
                # mole: amount of substance
                'mol': 'mol', 'mole': 'mol',
                # newton: force, weight
                'newton': 'N', 'newtons': 'N', 'n': 'N',
                # pascal: pressure, stress
                'pascal': 'Pa', 'pascals': 'Pa', 'pa': 'Pa',
                # volt: voltage (electrical potential), emf
                'v': 'V', 'volt': 'V', 'volts': 'V',
                # degree Celsius: temperature relative to 273.15 K
                '°c': '°C', '°celsius': '°C', 'celsius': '°C',
                # ampere: electric current
                'a': 'A', 'ampere': 'A', 'amp': 'A', 'amps': 'A',
                # second: time and hertzs
                '1/hz': 's', '1/hertz': 's', 'hz': 'Hz',
                '1/s': 'Hz', '1/second': 'Hz', '1/seconds': 'Hz',
                '1/sec': 'Hz', '1/secs': 'Hz', 'hertz': 'Hz',
                'second': 's', 'seconds': 's', 'sec': 's',
                'secs': 's', 's': 's',
}

# Init dictionary of aliases for multipliers. Entries are still lowercase
prefix_aliases = {
                    # Multiples - skip "mega" and only up to "tera"
                    'da': 'da', 'deca': 'da', 'h': 'h', 'hecto': 'h',
                    'k': 'k', 'kilo': 'k', 'g': 'G', 'giga': 'G', 't': 'T',
                    'tera': 'T',
                    # Submultipliers
                    'd': 'd', 'deci': 'd', 'c': 'c', 'centi': 'c',
                    'milli': 'm', 'm': 'm', 'µ': 'µ', 'micro': 'µ',
                    'n': 'n', 'nano': 'n', 'p': 'p', 'pico': 'p',
                    'f': 'f', 'femto': 'f', 'a': 'a', 'atto': 'a',
                    'z': 'z', 'zepto': 'z', 'y': 'y', 'yocto': 'y',
}


def bidsify_units(orig_unit):
    """
    Read the input unit of measure and use the dictionary of aliases
    to bidsify its value.
    It is possible to make simple conversions

    Parameters
    ----------
    unit: string
        Unit of measure, might or might not be BIDS compliant.

    Returns
    -------
    new_unit: str
        BIDSified alias of input unit

    Notes
    -----
    This function should implement a double check, one for unit and
    the other for prefixes (e.g. "milli"). However, that is going to be tricky,
    unless there is a weird way to multiply two dictionaries together.
    """
    # call prefix and unit dicts
    # for every unit alias in the dict
    orig_unit = orig_unit.lower()
    for u_key in unit_aliases.keys():
        if orig_unit.endswith(u_key):
            new_unit = unit_aliases[u_key]
            unit = orig_unit[:-len(u_key)]
            if unit != '':
                # for every prefix alias
                prefix = prefix_aliases.get(unit, '')
                if prefix == '':
                    LGR.warning(f'The given unit prefix {unit} does not have aliases, '
                                f'passing it as is')
                    prefix = orig_unit[:len(unit)]
                return prefix + new_unit
            else:
                return new_unit
    LGR.warning(f'The given unit {orig_unit} does not have aliases, '
                f'passing it as is')
    return orig_unit