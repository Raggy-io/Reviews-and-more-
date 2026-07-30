"""
Data pools for review generation.
Contains names, titles, and body fragments used to assemble realistic reviews.
"""

FIRST_NAMES = [
    'Aarav', 'Aditi', 'Aisha', 'Amit', 'Ananya', 'Ankita', 'Arjun', 'Aryan',
    'Deepa', 'Deepika', 'Divya', 'Geeta', 'Ishaan', 'Jaya', 'Kabir', 'Kavita',
    'Kiran', 'Kritika', 'Lakshmi', 'Manish', 'Meera', 'Mihir', 'Mohan', 'Neha',
    'Nisha', 'Pooja', 'Priya', 'Rahul', 'Raj', 'Ravi', 'Rekha', 'Rohit',
    'Sakshi', 'Sanjay', 'Sapna', 'Shilpa', 'Shruti', 'Sneha', 'Sonia', 'Suresh',
    'Swati', 'Tanvi', 'Usha', 'Vandana', 'Varun', 'Vidya', 'Vikram', 'Vinod',
    'Yamini', 'Zara',
]

LAST_NAMES = [
    'Agarwal', 'Bansal', 'Bhat', 'Choudhary', 'Das', 'Desai', 'Dubey', 'Gandhi',
    'Garg', 'Ghosh', 'Gupta', 'Iyer', 'Jain', 'Joshi', 'Kapoor', 'Khanna',
    'Kulkarni', 'Kumar', 'Mehta', 'Mishra', 'Nair', 'Pandey', 'Patel', 'Pillai',
    'Rao', 'Reddy', 'Saxena', 'Sharma', 'Shukla', 'Singh', 'Sinha', 'Srivastava',
    'Tiwari', 'Tripathi', 'Varma', 'Verma',
]

TITLES_5 = [
    'Absolutely love it!',
    'Worth every rupee',
    'Stunning quality',
    'Exceeded my expectations',
    'A true gem for the home',
    'Perfect addition to my collection',
    'Beautifully crafted',
    'Simply gorgeous',
    'Premium feel, premium look',
    'Could not be happier',
    'Arrived quickly and looks amazing',
    'My family is obsessed with it',
    'Best purchase this year',
    'Elegant and timeless',
    'Curated By Banjara never disappoints',
]

TITLES_4 = [
    'Very happy with this purchase',
    'Great quality overall',
    'Looks exactly as pictured',
    'Solid buy, would recommend',
    'Good value for the price',
    'Nice piece, fast delivery',
    'Impressed with the craftsmanship',
    'Almost perfect',
    'Really pleased with this',
    'Loved it, minor packaging issue',
]

TITLES_3 = [
    'Decent product',
    'Good but could be better',
    'Average for the price',
    'Meets expectations',
    'Okay overall',
]

OPENERS = [
    'I ordered this for my dining room and it looks absolutely beautiful.',
    'Bought this as a gift and the recipient was thrilled.',
    'Have been eyeing this for a while and finally placed the order — no regrets!',
    'Just received my order and the quality is impressive.',
    'This arrived well-packaged and in perfect condition.',
    'I was a bit hesitant to order online but I am so glad I did.',
    'Ordered two of these and both are perfect.',
    'My mother gifted this to me and I absolutely adore it.',
    'I replaced my old set with this and the difference is night and day.',
    'This is exactly what I was looking for.',
    'Spotted this on Instagram and had to have it.',
    'I have been collecting pieces from Curated By Banjara and this is my favourite so far.',
]

MIDDLES = [
    'The craftsmanship is really top-notch — you can tell a lot of care has gone into it.',
    'The material feels premium and looks even better in person than in the photos.',
    'The colour is spot on and complements my home decor perfectly.',
    'It is sturdier than I expected, which is always a pleasant surprise.',
    'The finish is very clean and there are no rough edges whatsoever.',
    'It has a warm, earthy feel that suits my home aesthetic beautifully.',
    'The size is just right — not too big, not too small.',
    'My guests keep asking where I got it from!',
    'The packaging was excellent — double-boxed and very secure.',
    'It pairs wonderfully with my existing tableware.',
    'The texture feels great in hand.',
    'Delivery was faster than expected, which was a nice bonus.',
    'The weight is good — solid without being too heavy.',
    'The design is understated but elegant, exactly what I was looking for.',
]

CLOSERS = [
    'Would definitely order from Curated By Banjara again.',
    'Highly recommend to anyone looking for quality home décor.',
    'Will be ordering more pieces soon.',
    'A wonderful purchase overall.',
    'Very satisfied with the whole experience.',
    'Already recommended this to a few friends.',
    'Five stars and will be back for more.',
    'Great addition to my home.',
    'Thoroughly happy with this buy.',
    'Looking forward to exploring more from this brand.',
]

# Weighted rating pool — skewed positive
RATING_POOL = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3]
