from dataclasses import dataclass

@dataclass
class CSV:
    fileName: str
    indexName: str
    dataOffset: int
    separator: str