import argparse
import json
import sys
from review_generator import ReviewGenerator

def main():
    # Ensure stdout handles UTF-8 (especially for Windows console displaying the star character)
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    parser = argparse.ArgumentParser(
        description="Deterministic Custom Review Generator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "--product-id", 
        type=str, 
        required=True,
        help="The unique ID of the product. This acts as the seed for deterministic generation."
    )
    parser.add_argument(
        "--count", 
        type=int, 
        default=4,
        help="Number of reviews to generate."
    )
    parser.add_argument(
        "--export", 
        type=str, 
        help="Optional path to a JSON file to export the reviews."
    )

    args = parser.parse_args()

    # Generate the reviews
    print(f"Generating {args.count} reviews for product ID: '{args.product_id}'...")
    reviews = ReviewGenerator.generate(args.product_id, args.count)
    average = ReviewGenerator.average_rating(reviews)

    # Print to console
    print(f"\nAverage Rating: {average} / 5.0")
    print("-" * 40)
    
    for r in reviews:
        print(f"[{r.rating}★] {r.title}")
        print(f"By {r.author} {'(Verified)' if r.verified else ''}")
        print(f"{r.body}")
        print("-" * 40)

    # Export if requested
    if args.export:
        try:
            with open(args.export, 'w') as f:
                json.dump([r.to_dict() for r in reviews], f, indent=2)
            print(f"\nSuccessfully exported reviews to {args.export}")
        except Exception as e:
            print(f"\nError exporting to {args.export}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
