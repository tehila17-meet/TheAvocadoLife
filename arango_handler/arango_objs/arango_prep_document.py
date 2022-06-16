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
    arango_document_object: document.Document = None

    def __post_init__(self):
        self.dictionized_base_data = {"title": self.title, "impact_rating": self.impact_rating,
                                      "insertion_time": self.insertion_time}
