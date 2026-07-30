from dataclasses import dataclass
from typing import Optional

@dataclass
class Review:
    """
    Represents a single generated review.
    """
    id: str
    author: str
    rating: int
    title: str
    body: str
    verified: bool = True
    date: str = ""

    def to_dict(self) -> dict:
        """Converts the review to a dictionary representation."""
        return {
            "id": self.id,
            "author": self.author,
            "rating": self.rating,
            "title": self.title,
            "body": self.body,
            "verified": self.verified,
            "date": self.date,
        }
