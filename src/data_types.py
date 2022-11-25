from dataclasses import dataclass

@dataclass
class CSVTimeseries:
    """
    Used when the timeseries are placed as columns
    """
    name: str
    source: str
    indexName: str
    dataOffset: int
    separator: str

@dataclass
class CSVSequence:
    """
    Used when timeseries are placed as a sequence
    """
    name: str
    source: str
    indexName: str
    dateColumnName: str
    valueColumntName: str
    separator: str

@dataclass
class TSV:
    name: str
    source: str
    indexName: str


