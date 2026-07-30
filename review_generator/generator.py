from typing import List
from .models import Review
from .engine import hash_seed, LCG
from .data import (
    FIRST_NAMES, LAST_NAMES, TITLES_5, TITLES_4, TITLES_3,
    OPENERS, MIDDLES, CLOSERS, RATING_POOL
)

class ReviewGenerator:
    """
    Generator class that constructs deterministic reviews.
    """
    
    @staticmethod
    def generate(product_id: str, count: int = 4) -> List[Review]:
        """
        Generate deterministic reviews for a given product ID.
        
        Args:
            product_id (str): The product's unique ID (used as seed).
            count (int): Number of reviews to generate. Default is 4.
            
        Returns:
            List[Review]: A list of generated Review objects.
        """
        if not product_id:
            return []

        # Convert to string to ensure consistent hashing
        seed = hash_seed(str(product_id))
        rng = LCG(seed)

        reviews = []
        for i in range(count):
            # Advance RNG deterministically for each review slot
            first_name = rng.pick(FIRST_NAMES)
            last_name = rng.pick(LAST_NAMES)
            author = f"{first_name} {last_name[0]}."

            rating = rng.pick(RATING_POOL)

            # Pick title based on rating
            if rating == 5:
                title_pool = TITLES_5
            elif rating == 4:
                title_pool = TITLES_4
            else:
                title_pool = TITLES_3
                
            title = rng.pick(title_pool)

            # Assemble body
            opener = rng.pick(OPENERS)
            middle = rng.pick(MIDDLES)
            closer = rng.pick(CLOSERS)
            body = f"{opener} {middle} {closer}"

            review = Review(
                id=f"gen-{product_id}-{i}",
                author=author,
                rating=rating,
                title=title,
                body=body,
                verified=True,
                date=""
            )
            reviews.append(review)

        return reviews

    @staticmethod
    def average_rating(reviews: List[Review]) -> float:
        """
        Compute the average rating from a set of generated reviews.
        
        Args:
            reviews (List[Review]): The list of reviews.
            
        Returns:
            float: The average rating rounded to 1 decimal place.
        """
        if not reviews:
            return 4.5
        total = sum(r.rating for r in reviews)
        return round(total / len(reviews), 1)
