from dataclasses import dataclass
from typing import List

from pyArango import document



@dataclass
class ArangoPrepDocument:
    affecting_collection: str
    title: str
    impact_rating: int
    insertion_time: str
    defining_traits: List[str]
    dictionized_base_data: dict = {"title": title, "impact_rating": impact_rating, "insertion_time": insertion_time}
    real_arango_document_object: document.Document = None
