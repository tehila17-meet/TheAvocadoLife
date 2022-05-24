from typing import List
from dataclasses import dataclass

@dataclass
class ArangoData():
    caused_collection_name: str
    affected_traits_collections: List[str]





