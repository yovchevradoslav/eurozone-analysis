from dataclasses import dataclass

@dataclass
class CSVTimeseries:
    """
    Used when the timeseries are placed as columns
    """
    source: str
    indexName: str
    dataOffset: int
    separator: str
    transpose: bool

@dataclass
class CSVSequence:
    """
    Used when timeseries are placed as a sequence
    """
    source: str
    countryColumnName: str
    dateColumnName: str
    valueColumnName: str
    separator: str
    transpose: bool

@dataclass
class TSV:
    source: str
    indexName: str
    transpose: bool


