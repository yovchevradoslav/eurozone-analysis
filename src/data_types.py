from dataclasses import dataclass

@dataclass
class CSV:
    source: str
    indexName: str
    dataOffset: int
    separator: str