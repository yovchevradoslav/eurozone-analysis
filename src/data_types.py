from dataclasses import dataclass

@dataclass
class CSV:
    source: str
    indexName: str
    dataOffset: int
    separator: str

@dataclass
class TSV:
    source: str
    indexName: str

