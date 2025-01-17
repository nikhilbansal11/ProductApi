import os
from flask import Flask, request, jsonify
import logging
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

@app.route('/product', methods=['POST'])
def predict():
    """Prediction endpoint"""
    try:
        response = {
  "products": [
    {
      "product_name": "QuantumFlux",
      "product_image_link": "https://example-store.com/images/electronics/quantumflux.jpg",
      "product_description": "QuantumFlux: The Ultimate Power Solution\n\nQuantumFlux is an innovative power source that harnesses the principles of quantum entanglement for superior performance. With unparalleled efficiency, it delivers stable and uninterrupted power to your electronic devices. Experience faster charging speeds, prolonged battery life, and reduced energy consumption. QuantumFlux empowers your electronics to operate at their peak, maximizing functionality and minimizing downtime.",
      "customer_comments": [
        {
          "comment": "QuantumFlux's quantum computing platform is a huge disappointment. The promised speed and accuracy are nowhere to be found. Simulations run extremely slow, and the results are unreliable. Save your money and time; this platform is not ready for real-world applications.",
          "label": "Negative"
        },
        {
          "comment": "I was excited to try QuantumFlux, but the product was a huge disappointment. It froze constantly, and I couldn't rely on it for important tasks. The customer support was terrible too; they were slow to respond and couldn't help me resolve my issues. I'm very disappointed and would not recommend this product to anyone.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 746.12,
        "discounted_price": 659.31
      },
      "product_rating": {
        "rating": 4.3,
        "out_of": 5
      },
      "category": "Electronics",
      "number_of_ratings_reviews": 260,
      "availability_status": "In Stock"
    },
    {
      "product_name": "Allure Luxe",
      "product_image_link": "https://retail-images.com/products/fashion/allure-luxe.jpg",
      "product_description": "Indulge in the world of high fashion with Allure Luxe. Our curated selection showcases the latest runway trends and must-have pieces from the most coveted designers. Discover exclusive collections, limited-edition items, and insider access to the fashion elite. Elevate your wardrobe and make a statement with the most stylish and sophisticated pieces that embody the essence of luxury.",
      "customer_comments": [
        {
          "comment": "Generic Generate a realistic negative customer review for Allure Luxe. Keep it under 50 words.",
          "label": "Negative"
        },
        {
          "comment": "Allure Luxe offers high-quality jewelry at accessible prices. The pieces I've purchased have been stylish and well-crafted, with a few minor exceptions. While some items have lasted well, others have shown signs of wear and tear faster than expected. Overall, it's a decent option for affordable jewelry, but longevity may vary.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 26.11,
        "discounted_price": 19.11
      },
      "product_rating": {
        "rating": 4.4,
        "out_of": 5
      },
      "category": "Fashion",
      "number_of_ratings_reviews": 942,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "ZenAir Purifier",
      "product_image_link": "https://store-assets.org/photos/home appliances/zenair-purifier.jpg",
      "product_description": "Breathe easy with ZenAir Purifier! This innovative appliance removes allergens, dust, smoke, and unpleasant odors, leaving you with a fresher, healthier home environment. Its advanced filtration system captures 99.9% of airborne particles as small as 0.3 microns, ensuring maximum air purification. With its sleek design and whisper-quiet operation, ZenAir effortlessly integrates into any home décor, offering a peaceful and rejuvenating indoor atmosphere.",
      "customer_comments": [
        {
          "comment": "\"Since installing the ZenAir Purifier, I've noticed a significant improvement in my indoor air quality. The air is fresher and cleaner, and I no longer experience allergy symptoms. The purifier is quiet and easy to maintain, making it a great addition to my home.\"",
          "label": "Positive"
        },
        {
          "comment": "ZenAir Purifier is a disappointment. It failed to remove odors and improve air quality despite running continuously. The filter clogged quickly, requiring frequent replacements, adding to the already high cost. The purifier was noisy and disruptive, making it difficult to use in bedrooms or living areas.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 2813.15,
        "discounted_price": 2236.78
      },
      "product_rating": {
        "rating": 4.3,
        "out_of": 5
      },
      "category": "Home Appliances",
      "number_of_ratings_reviews": 387,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "The Essence of the Cosmos",
      "product_image_link": "https://retail-images.com/products/books/the-essence-of-the-cosmos.jpg",
      "product_description": "Embark on an awe-inspiring journey through the enigmatic tapestry of the cosmos with \"The Essence of the Cosmos.\" This captivating book explores the fundamental principles and profound mysteries of the universe, from the boundless expanse of galaxies to the intricate dance of subatomic particles. Delve into the latest scientific discoveries, philosophical contemplations, and tantalizing questions that have captivated humankind for centuries.",
      "customer_comments": [
        {
          "comment": "The Essence of the Cosmos is a captivating journey through the wonders of the universe. Its immersive writing and stunning visuals left me awe-inspired. It ignited my curiosity and deepened my appreciation for the cosmos we live in. I highly recommend this remarkable book to anyone seeking to expand their understanding of our place in the universe.",
          "label": "Positive"
        },
        {
          "comment": "The Essence of the Cosmos is a captivating read that explores the mysteries of the universe. While the author's theories are intriguing, some may find them a bit speculative at times. The writing style is clear and engaging, but the lack of concrete evidence to support some ideas could leave some readers unconvinced.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 41.25,
        "discounted_price": 34.87
      },
      "product_rating": {
        "rating": 4.9,
        "out_of": 5
      },
      "category": "Books",
      "number_of_ratings_reviews": 58,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "EdgeXtreme Mountain Bike",
      "product_image_link": "https://example-store.com/images/sports & outdoors/edgextreme-mountain-bike.jpg",
      "product_description": "Experience the thrill of off-road riding with the EdgeXtreme Mountain Bike. Designed for adventure on rugged trails, it features:\n\n- Durable aluminum frame for strength and agility\n- 27-speed drivetrain for effortless climbing and descents\n- Front suspension fork for smooth absorption of bumps\n- Hydraulic disc brakes for reliable stopping power\n- Sleek, aggressive design for style and performance\n\nConquer any terrain with the EdgeXtreme Mountain Bike, the perfect companion for your next outdoor adventure!",
      "customer_comments": [
        {
          "comment": "EdgeXtreme Mountain Bike is a beast! It handles trails like a dream, giving me a smooth and thrilling ride. The suspension absorbs shocks seamlessly, making even the roughest terrain a breeze. Highly recommended for adventure enthusiasts seeking a top-notch mountain bike experience!",
          "label": "Positive"
        },
        {
          "comment": "The EdgeXtreme Mountain Bike is an absolute beast! It handled the toughest trails with ease, providing a thrilling and effortless ride. The lightweight frame and responsive suspension made every climb and descent a pure joy. Highly recommended for any mountain biking enthusiast looking for a bike that will take their adventures to the next level.",
          "label": "Positive"
        }
      ],
      "product_price": {
        "current_price": 377.32,
        "discounted_price": 345.53
      },
      "product_rating": {
        "rating": 4.8,
        "out_of": 5
      },
      "category": "Sports & Outdoors",
      "number_of_ratings_reviews": 250,
      "availability_status": "In Stock"
    },
    {
      "product_name": "Aetherra Radiance",
      "product_image_link": "https://retail-images.com/products/beauty & personal care/aetherra-radiance.jpg",
      "product_description": "Discover the ethereal glow of Aetherra Radiance! This lightweight, rejuvenating serum harnesses the power of nature to revitalize your skin. Infused with antioxidants and botanical extracts, it soothes irritation, evens skin tone, and restores a youthful radiance. Aetherra Radiance leaves your skin feeling refreshed, hydrated, and irresistibly radiant.",
      "customer_comments": [
        {
          "comment": "Aetherra Radiance offers a sleek and modern design. The interface is easy to use, but the feature set is somewhat limited compared to other similar products. Overall, it's a decent choice for basic lighting needs, but it may not meet the demands of more advanced users.",
          "label": "Neutral"
        },
        {
          "comment": "Aetherra Radiance moisturizer feels lightweight on my skin, and I appreciate that it's non-greasy. While it provides some hydration, I find that I need to reapply throughout the day to maintain moisture. It's a decent moisturizer but didn't meet my expectations based on the price.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 106.54,
        "discounted_price": 94.8
      },
      "product_rating": {
        "rating": 3.2,
        "out_of": 5
      },
      "category": "Beauty & Personal Care",
      "number_of_ratings_reviews": 192,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Sparktacular",
      "product_image_link": "https://retail-images.com/products/toys & games/sparktacular.jpg",
      "product_description": "Unleash the magic with Sparktacular, the enchanting glow-in-the-dark drawing and writing instrument! Create vibrant masterpieces that come alive at night, illuminating your imagination with every stroke. Its easy-to-use design makes it suitable for artists of all ages. Transform your drawings into radiant nighttime wonders with Sparktacular!",
      "customer_comments": [
        {
          "comment": "Sparktacular is the best way to brighten up any event! The fireworks were magnificent, and the customer service was impeccable. They made sure everything went smoothly, and our guests were thrilled. Highly recommend for any special occasion!",
          "label": "Positive"
        },
        {
          "comment": "Sparktacular promised a dazzling display but delivered a fizzling dud. Their fireworks were faulty, resulting in an embarrassing and anticlimactic event. Avoid this unprofessional and unreliable company if you value your special occasion.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 260.34,
        "discounted_price": 227.37
      },
      "product_rating": {
        "rating": 3.8,
        "out_of": 5
      },
      "category": "Toys & Games",
      "number_of_ratings_reviews": 694,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Nature's Embrace",
      "product_image_link": "https://retail-images.com/products/grocery/nature's-embrace.jpg",
      "product_description": "Indulge in the purity of nature with Nature's Embrace. Our organic and minimally processed products are crafted with the utmost care, preserving the freshness and nutritional value of the finest ingredients. From crisp fruits and vegetables to wholesome grains and beverages, our range of organic offerings brings you a symphony of flavors and essential nutrients, ensuring a healthier, more balanced lifestyle.",
      "customer_comments": [
        {
          "comment": "Disappointing experience. The products were overpriced and ineffective. My skin felt more irritated after using the moisturizer. I do not recommend this brand to anyone looking for natural skincare solutions.",
          "label": "Negative"
        },
        {
          "comment": "Nature's Embrace products fell short of expectations. The supplements had a strange aftertaste and did not provide the advertised benefits. Moreover, customer service was unresponsive and unhelpful, making the entire experience unsatisfying.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 42.51,
        "discounted_price": 32.22
      },
      "product_rating": {
        "rating": 3.6,
        "out_of": 5
      },
      "category": "Grocery",
      "number_of_ratings_reviews": 667,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Essence Lounge Chair",
      "product_image_link": "https://retail-images.com/products/furniture/essence-lounge-chair.jpg",
      "product_description": "Indulge in comfort and style with the Essence Lounge Chair. Crafted with soft, plush upholstery, this chair envelops you in a luxurious embrace. Its elegant curves and subtle stitching create a sophisticated aesthetic that complements any décor. Whether you're relaxing with a book or entertaining guests, the Essence Lounge Chair elevates your living space with its timeless appeal.",
      "customer_comments": [
        {
          "comment": "\"The Essence Lounge Chair is a must-have for any home. Its plush cushioning and ergonomic design provide unbeatable comfort. It's the perfect place to relax and unwind after a long day. I highly recommend this chair to anyone looking for a stylish and functional addition to their living space.\"",
          "label": "Positive"
        },
        {
          "comment": "The chair's design is uncomfortable, with a narrow seat and low back. The assembly instructions were unclear, leading to misalignment and instability. Despite being advertised as sturdy, the chair creaks and wobbles while in use. It is an overpriced and frustrating purchase.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 795.8,
        "discounted_price": 601.78
      },
      "product_rating": {
        "rating": 3.2,
        "out_of": 5
      },
      "category": "Furniture",
      "number_of_ratings_reviews": 657,
      "availability_status": "In Stock"
    },
    {
      "product_name": "Pawsitive Companion Care",
      "product_image_link": "https://store-assets.org/photos/pet supplies/pawsitive-companion-care.jpg",
      "product_description": "Pawsitive Companion Care: Give your furry friend the care they deserve! Our comprehensive pet supplies cater to all their needs, from cozy beds and tasty treats to essential grooming tools and health supplements. Keep your beloved companion happy and healthy with our wide range of high-quality products, designed to enhance their well-being and strengthen your bond.",
      "customer_comments": [
        {
          "comment": "Pawsitive Companion Care provided exceptional care for our furry friend! They were professional, compassionate, and went above and beyond to ensure our pet's comfort and well-being. We highly recommend their services for any pet owner looking for reliable and loving care.",
          "label": "Positive"
        },
        {
          "comment": "Pawsitive Companion Care has been a lifesaver for my busy family. Their team is reliable, compassionate, and goes above and beyond to care for our beloved dog. Our furry friend always returns home happy and safe after each visit. Highly recommend for peace of mind and a happy pet!",
          "label": "Positive"
        }
      ],
      "product_price": {
        "current_price": 87.36,
        "discounted_price": 61.74
      },
      "product_rating": {
        "rating": 4.3,
        "out_of": 5
      },
      "category": "Pet Supplies",
      "number_of_ratings_reviews": 38,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Zenith Allure XT",
      "product_image_link": "https://example-store.com/images/electronics/zenith-allure-xt.jpg",
      "product_description": "Immerse yourself in a captivating home entertainment experience with Zenith Allure XT, our cutting-edge TV. Its stunning 4K HDR display delivers exceptional clarity and vivid colors, bringing your movies and shows to life. Enjoy smooth, lag-free gaming and streaming with its powerful processor and optimized OS. The sleek and minimalist design complements any décor, making Zenith Allure XT the perfect addition to your entertainment haven.",
      "customer_comments": [
        {
          "comment": "Zenith Allure XT exceeded my expectations! Its sleek design and user-friendly interface made it a pleasure to use. The images captured were crystal clear and the AI-powered features were incredibly helpful. It's the perfect camera for both professional photographers and casual users alike. Highly recommended!",
          "label": "Positive"
        },
        {
          "comment": "\"Zenith Allure XT is a fantastic product! The sound quality is crystal clear, and the bass is deep and powerful. I've also been impressed with the battery life. It lasts for hours, even when I'm using it heavily. Overall, I'm incredibly happy with my purchase, and I highly recommend this product.\"",
          "label": "Positive"
        }
      ],
      "product_price": {
        "current_price": 1636.04,
        "discounted_price": 1437.3
      },
      "product_rating": {
        "rating": 4.2,
        "out_of": 5
      },
      "category": "Electronics",
      "number_of_ratings_reviews": 413,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Aetherial Embers",
      "product_image_link": "https://retail-images.com/products/fashion/aetherial-embers.jpg",
      "product_description": "Indulge in the ethereal beauty of Aetherial Embers. Handcrafted from the finest gemstones, these enchanting earrings exude a celestial glow. The radiant hues of tourmaline and aquamarine shimmer gracefully, creating a mesmerizing dance of light. Suspended from delicate chains, Aetherial Embers evoke a sense of elegance and ethereal charm, elevating any ensemble to a realm of enchantment.",
      "customer_comments": [
        {
          "comment": "Aetherial Embers offers a decent selection of fantasy candles with unique scents. While the scents are pleasant, the burn time is shorter than expected and the throw is rather weak. The candles are visually appealing, but the overall value for money is just average.",
          "label": "Neutral"
        },
        {
          "comment": "Aetherial Embers' scents are terrible and the candles give me headaches. I bought the \"Enchanted Forest\" candle and it smelled like burnt wood. I tried to exchange it, but the customer service was awful and they refused to help. Save your money and avoid this company.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 285.56,
        "discounted_price": 231.79
      },
      "product_rating": {
        "rating": 4.7,
        "out_of": 5
      },
      "category": "Fashion",
      "number_of_ratings_reviews": 526,
      "availability_status": "In Stock"
    },
    {
      "product_name": "Zenith Elite",
      "product_image_link": "https://example-store.com/images/home appliances/zenith-elite.jpg",
      "product_description": "Zenith Elite: Elevate Your Home Life\n\nDiscover Zenith Elite, the epitome of home appliance excellence. Our premium range empowers you with innovative features, exceptional performance, and sleek designs that seamlessly complement your modern kitchen. Experience effortless cooking, pristine cleaning, and ultimate comfort with our state-of-the-art appliances, engineered to revolutionize your home experience.",
      "customer_comments": [
        {
          "comment": "Zenith Elite is a solid choice for those looking for a reliable and affordable option. While it may not be the most exciting or feature-rich product on the market, it gets the job done without any major issues. If you're looking for a no-frills product that won't break the bank, Zenith Elite is worth considering.",
          "label": "Neutral"
        },
        {
          "comment": "Zenith Elite offers quality financial services, but their fees can be slightly higher than others. The customer service is generally helpful and responsive, although it can be a bit slow at times. Overall, it is a decent option for financial services, but there may be more cost-effective or faster alternatives available.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 1747.47,
        "discounted_price": 1470.46
      },
      "product_rating": {
        "rating": 5.0,
        "out_of": 5
      },
      "category": "Home Appliances",
      "number_of_ratings_reviews": 910,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "The Wanderer's Codex",
      "product_image_link": "https://retail-images.com/products/books/the-wanderer's-codex.jpg",
      "product_description": "Embark on a captivating literary journey with \"The Wanderer's Codex.\" This enthralling collection of tales transports you to distant lands, introduces compelling characters, and ignites your wanderlust. Immerse yourself in a world where history, mythology, and fantasy intertwine, crafting a spellbinding tapestry that captivates the imagination. Whether you're an avid reader or simply seeking an escape, \"The Wanderer's Codex\" offers a compelling and immersive experience.",
      "customer_comments": [
        {
          "comment": "The Wanderer's Codex offers a comprehensive guide to the various paths and landscapes of the world. While it provides valuable information, the writing lacks the engaging prose that would make it a truly captivating read. Overall, it's a functional resource, but it could be improved with a more immersive narrative.",
          "label": "Neutral"
        },
        {
          "comment": "Generic Generate a realistic negative customer review for The Wanderer's Codex. Keep it under 50 words.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 55.29,
        "discounted_price": 44.22
      },
      "product_rating": {
        "rating": 4.3,
        "out_of": 5
      },
      "category": "Books",
      "number_of_ratings_reviews": 401,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Velocity X1 Running Shoes",
      "product_image_link": "https://example-store.com/images/sports & outdoors/velocity-x1-running-shoes.jpg",
      "product_description": "Elevate your runs with the Velocity X1 Running Shoes! Engineered for exceptional speed and agility, these shoes boast responsive cushioning, a breathable mesh upper, and a durable rubber outsole. Experience effortless strides, superior comfort, and enhanced foot protection with the Velocity X1. Ideal for runners looking to push their limits and conquer the tracks or roads with confidence.",
      "customer_comments": [
        {
          "comment": "The Velocity X1 Running Shoes provide decent support and cushioning. They're comfortable for short runs but may not be suitable for long distances. The fit is a bit narrow, so those with wider feet may want to consider a different option. Overall, they're a solid choice for casual runners.",
          "label": "Neutral"
        },
        {
          "comment": "Despite their sleek design, Velocity X1 Running Shoes proved to be extremely uncomfortable. The stiff material rubbed against my feet, causing blisters within the first hour of wear. The lack of arch support left me with aching feet after every run. Sadly, these shoes failed to meet my expectations.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 226.73,
        "discounted_price": 193.18
      },
      "product_rating": {
        "rating": 4.7,
        "out_of": 5
      },
      "category": "Sports & Outdoors",
      "number_of_ratings_reviews": 409,
      "availability_status": "In Stock"
    },
    {
      "product_name": "Celestial Skin Serum",
      "product_image_link": "https://retail-images.com/products/beauty & personal care/celestial-skin-serum.jpg",
      "product_description": "Experience radiant, ethereal skin with Celestial Skin Serum. Infused with starflower oil, hyaluronic acid, and vitamin C, this celestial concoction deeply hydrates, plumps, and brightens your complexion. Its lightweight formula absorbs effortlessly, leaving behind a velvety-smooth canvas free of blemishes, fine lines, and wrinkles. Unveiling the luminosity of your celestial self, Celestial Skin Serum transforms your skin into a radiant masterpiece.",
      "customer_comments": [
        {
          "comment": "Celestial Skin Serum is a waste of money. After using it for a month, I saw no improvement in my skin's appearance. It's a scam!",
          "label": "Negative"
        },
        {
          "comment": "Celestial Skin Serum left my skin feeling soft and refreshed. However, the results were not as dramatic as I had hoped. While I noticed a slight improvement in my skin's texture, the fine lines and wrinkles remained visible.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 104.58,
        "discounted_price": 81.16
      },
      "product_rating": {
        "rating": 4.8,
        "out_of": 5
      },
      "category": "Beauty & Personal Care",
      "number_of_ratings_reviews": 942,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Astro Bots: Cosmic Crusaders",
      "product_image_link": "https://retail-images.com/products/toys & games/astro-bots:-cosmic-crusaders.jpg",
      "product_description": "Join the brave Astro Bots as they embark on interstellar adventures in this captivating game for PS VR! Explore vibrant planets, solve puzzles, and engage in thrilling battles with quirky characters and stunning visuals. The intuitive controls and immersive VR gameplay will transport you to the heart of the Astro Bots' heroic journey.",
      "customer_comments": [
        {
          "comment": "Disappointed with the repetitive levels and lackluster combat. The initially promising visuals quickly become stale, and the game fails to deliver on its potential. Not recommended for those seeking an engaging and challenging VR experience.",
          "label": "Negative"
        },
        {
          "comment": "Astro Bots is a fun and polished VR platformer, but its repetitive missions and lack of variety hold it back from being truly great. The platforming is solid and the graphics are impressive, but the overall experience is a bit too shallow. If you're looking for a quick and easy VR fix, Astro Bots is worth checking out, but don't expect anything groundbreaking.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 50.88,
        "discounted_price": 46.11
      },
      "product_rating": {
        "rating": 3.2,
        "out_of": 5
      },
      "category": "Toys & Games",
      "number_of_ratings_reviews": 801,
      "availability_status": "In Stock"
    },
    {
      "product_name": "Quinoa Symphony",
      "product_image_link": "https://retail-images.com/products/grocery/quinoa-symphony.jpg",
      "product_description": "Experience a medley of flavors with Quinoa Symphony! Our expertly crafted blend of red, black, white, and tri-color quinoa offers a symphony of textures and nutty undertones. Rich in protein, fiber, and minerals, it's a versatile culinary canvas that complements salads, bowls, and entrees. Unleash your culinary creativity and elevate your meals with Quinoa Symphony!",
      "customer_comments": [
        {
          "comment": "Quinoa Symphony offers a decent selection of quinoa-based dishes. While the flavors were nothing special, the portions were generous and the prices reasonable. The ambiance was a bit bland, but overall it was a solid dining experience.",
          "label": "Neutral"
        },
        {
          "comment": "Quinoa Symphony offers a decent selection of quinoa dishes. The quinoa is cooked well, but the flavors are a bit bland. The service is friendly and efficient, but the prices are a bit high for what you get. Overall, it's a decent option for a quick and healthy meal, but there are better options out there.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 62.07,
        "discounted_price": 47.09
      },
      "product_rating": {
        "rating": 3.0,
        "out_of": 5
      },
      "category": "Grocery",
      "number_of_ratings_reviews": 898,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Elevate Luxe",
      "product_image_link": "https://example-store.com/images/furniture/elevate-luxe.jpg",
      "product_description": "Elevate your living space with Elevate Luxe, our premium furniture collection. Crafted from luxurious materials, each piece exudes elegance and comfort. Experience superior craftsmanship in every detail, from plush upholstery to intricate wood carvings. Elevate Luxe transcends ordinary furnishings, transforming your home into an oasis of sophistication and style. Upgrade your space with furniture that is both stunning and inviting.",
      "customer_comments": [
        {
          "comment": "Elevate Luxe offers a wide range of luxury items, but the prices can be quite high. The quality is generally good, but I've had a few issues with customer service. Overall, it's a decent option if you're willing to pay a premium.",
          "label": "Neutral"
        },
        {
          "comment": "Highly disappointed with Elevate Luxe. The products I ordered arrived damaged and of poor quality. Despite reaching out to customer service, I received no assistance or resolution. Avoid this unreliable retailer for a hassle-free shopping experience.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 1469.37,
        "discounted_price": 1200.53
      },
      "product_rating": {
        "rating": 4.1,
        "out_of": 5
      },
      "category": "Furniture",
      "number_of_ratings_reviews": 565,
      "availability_status": "In Stock"
    },
    {
      "product_name": "Pawsitive Pursuits",
      "product_image_link": "https://retail-images.com/products/pet supplies/pawsitive-pursuits.jpg",
      "product_description": "Maximize your pet's well-being with Pawsitive Pursuits! Our comprehensive line of pet supplies empowers you to provide the best care for your furry companions. From nutritious food and cozy bedding to grooming essentials and interactive toys, we have everything you need to keep your pets happy and healthy. Let Pawsitive Pursuits be your go-to destination for all your pet supply needs. Treat your beloved animals to the highest quality products for a lifetime of love and companionship.",
      "customer_comments": [
        {
          "comment": "Pawsitive Pursuits provides a convenient and reliable pet care service. The staff are friendly and knowledgeable, and they always take good care of my dog. However, their rates are a bit higher than some other services, and their hours can be somewhat limited. Overall, I'm satisfied with their service, but there are a few areas that could be improved.",
          "label": "Neutral"
        },
        {
          "comment": "Pawsitive Pursuits left my dog traumatized. My dog was shaking and panting excessively when I picked him up. The staff was rude and dismissive when I addressed my concerns. I will never take my dog back to them.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 467.97,
        "discounted_price": 431.77
      },
      "product_rating": {
        "rating": 3.4,
        "out_of": 5
      },
      "category": "Pet Supplies",
      "number_of_ratings_reviews": 319,
      "availability_status": "In Stock"
    },
    {
      "product_name": "OmniView Pro",
      "product_image_link": "https://retail-images.com/products/electronics/omniview-pro.jpg",
      "product_description": "Experience seamless visual collaboration with OmniView Pro! This cutting-edge device transforms your workspace into a collaborative hub, enabling real-time content sharing and video conferencing on multiple screens. Its intuitive interface and advanced features make it the perfect solution for team-based projects, presentations, and virtual meetings. Upgrade your workspace today and unleash the power of collaboration with OmniView Pro!",
      "customer_comments": [
        {
          "comment": "Generic Generate a realistic negative customer review for OmniView Pro. Keep it under 50 words.",
          "label": "Negative"
        },
        {
          "comment": "OmniView Pro offers a good range of features for the price. It's easy to install and use, but the image quality could be better. Overall, it's a solid choice for basic surveillance needs.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 225.62,
        "discounted_price": 177.57
      },
      "product_rating": {
        "rating": 4.6,
        "out_of": 5
      },
      "category": "Electronics",
      "number_of_ratings_reviews": 804,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Lunar Luxe",
      "product_image_link": "https://example-store.com/images/fashion/lunar-luxe.jpg",
      "product_description": "Generic Write a concise product description for Lunar Luxe in the Fashion category. Keep it under 100 words.",
      "customer_comments": [
        {
          "comment": "Lunar Luxe's candles are a true delight! The scents are exquisite, filling my home with a soothing and inviting atmosphere. The burn time is impressive, ensuring hours of aromatic bliss. Highly recommend these candles for anyone seeking tranquility and luxury.",
          "label": "Positive"
        },
        {
          "comment": "Generic Generate a realistic negative customer review for Lunar Luxe. Keep it under 50 words.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 295.3,
        "discounted_price": 226.91
      },
      "product_rating": {
        "rating": 3.4,
        "out_of": 5
      },
      "category": "Fashion",
      "number_of_ratings_reviews": 223,
      "availability_status": "In Stock"
    },
    {
      "product_name": "EcoFlow DELTA Pro",
      "product_image_link": "https://store-assets.org/photos/home appliances/ecoflow-delta-pro.jpg",
      "product_description": "Introducing the EcoFlow DELTA Pro - the ultimate power solution for your home! With its massive 3600Wh capacity and expandable design, it can power your home appliances, electronics, and even heavy tools during power outages or off-grid adventures. Its advanced MPPT solar charging and 6500W output make it a reliable and sustainable source of energy. Protect your home and essentials with the EcoFlow DELTA Pro, the ultimate portable power station.",
      "customer_comments": [
        {
          "comment": "\"The EcoFlow DELTA Pro has been a lifesaver during power outages! Its massive capacity and fast charging keep our essentials running smoothly. It's also lightweight and easy to transport, making it a reliable backup for any emergency.\"",
          "label": "Positive"
        },
        {
          "comment": "The EcoFlow DELTA Pro is a well-built and powerful portable power station. It is easy to use and has a variety of features that make it a versatile option for powering various devices. While its price point may be a deterrent for some buyers, it is a solid choice for those who need a reliable and portable power source.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 1759.79,
        "discounted_price": 1350.2
      },
      "product_rating": {
        "rating": 3.3,
        "out_of": 5
      },
      "category": "Home Appliances",
      "number_of_ratings_reviews": 801,
      "availability_status": "In Stock"
    },
    {
      "product_name": "The Ancient Tome of Secrets",
      "product_image_link": "https://product-photos.net/img/books/the-ancient-tome-of-secrets.jpg",
      "product_description": "Unveil the secrets of ancient wisdom with \"The Ancient Tome of Secrets.\" This enigmatic book holds the keys to forgotten knowledge, cryptic puzzles, and untold tales. Delve into its pages and embrace the power of ancient wisdom. From alchemical formulas to cosmic mysteries, this tome is a treasure chest of hidden lore that will ignite your curiosity and leave you spellbound.",
      "customer_comments": [
        {
          "comment": "\"The Ancient Tome of Secrets is an astounding book that has unlocked a new realm of knowledge for me. Its pages are filled with wisdom and secrets that have been hidden for centuries. I highly recommend it to anyone seeking enlightenment and self-discovery.\"",
          "label": "Positive"
        },
        {
          "comment": "\"Abysmal read. The 'ancient secrets' were nothing but common knowledge, poorly disguised. Language was convoluted and confusing, making it a tortuous experience. Avoid at all costs, unless you enjoy wasting your time and money.\"",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 27.74,
        "discounted_price": 24.3
      },
      "product_rating": {
        "rating": 4.6,
        "out_of": 5
      },
      "category": "Books",
      "number_of_ratings_reviews": 292,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Zenith Pro X",
      "product_image_link": "https://product-photos.net/img/sports & outdoors/zenith-pro-x.jpg",
      "product_description": "Zenith Pro X: Conquer any terrain with this ultra-rugged smartwatch engineered for adventure seekers. Its military-grade durability, precise GPS tracking, and advanced health monitoring features empower you to navigate the outdoors with confidence and precision. Whether you're hiking, biking, or exploring new frontiers, Zenith Pro X keeps pace with your every adventure.",
      "customer_comments": [
        {
          "comment": "Zenith Pro X failed to deliver on its promises. The cord is flimsy and keeps detaching, making it difficult to use. The sound is average at best and doesn't justify the high price. Save your money and look for other options.",
          "label": "Negative"
        },
        {
          "comment": "The Zenith Pro X is an exceptional product that has exceeded my expectations. It's incredibly user-friendly, and its features have greatly enhanced my productivity. I highly recommend it to anyone seeking a top-notch device.",
          "label": "Positive"
        }
      ],
      "product_price": {
        "current_price": 920.68,
        "discounted_price": 769.92
      },
      "product_rating": {
        "rating": 4.2,
        "out_of": 5
      },
      "category": "Sports & Outdoors",
      "number_of_ratings_reviews": 960,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Luminescent Radiance Elixir",
      "product_image_link": "https://product-photos.net/img/beauty & personal care/luminescent-radiance-elixir.jpg",
      "product_description": "Indulge in radiant beauty with our Luminescent Radiance Elixir. Enriched with a potent blend of vitamins, antioxidants, and botanical extracts, it nourishes your skin from within, revealing a luminous, even-toned complexion. Its lightweight formula absorbs effortlessly, leaving a velvety-soft finish that reflects light for a natural, healthy glow. Experience the transformative power of our elixir for a radiant, youthful appearance.",
      "customer_comments": [
        {
          "comment": "Luminescent Radiance Elixir is an average serum. It left my skin feeling slightly smoother, but the effects were subtle and not as radiant as advertised. The consistency is a bit thick, which made it difficult to spread evenly. Overall, it's an okay product, but I wouldn't recommend it for remarkable results or repurchase.",
          "label": "Neutral"
        },
        {
          "comment": "Generic Generate a realistic neutral customer review for Luminescent Radiance Elixir. Keep it under 50 words.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 103.31,
        "discounted_price": 82.3
      },
      "product_rating": {
        "rating": 3.7,
        "out_of": 5
      },
      "category": "Beauty & Personal Care",
      "number_of_ratings_reviews": 520,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Cosmic Xplorer",
      "product_image_link": "https://example-store.com/images/toys & games/cosmic-xplorer.jpg",
      "product_description": "Embark on intergalactic adventures with Cosmic Xplorer! This futuristic spaceship toy features an ergonomic design for easy handling, flashing LED lights, and realistic sound effects that enhance gameplay. Its adjustable landing gear allows for smooth takeoffs and landings, inspiring imaginative and immersive play. With Cosmic Xplorer, young astronauts can explore the vastness of space, develop their creativity, and soar to new heights of fun.",
      "customer_comments": [
        {
          "comment": "Cosmic Xplorer offers a decent virtual reality experience, with a good selection of games and activities. However, the graphics could be better, and the headset can be uncomfortable to wear for long periods. The customer service is also a bit slow to respond. Overall, it's an okay option for casual VR users, but there are better options available for more serious gamers.",
          "label": "Neutral"
        },
        {
          "comment": "Cosmic Xplorer is an amazing product that has helped me explore the vastness of space from the comfort of my own home. The immersive experience and accurate simulations make me feel like I'm actually venturing into the cosmos. I would highly recommend Cosmic Xplorer to anyone who is passionate about space exploration.",
          "label": "Positive"
        }
      ],
      "product_price": {
        "current_price": 230.1,
        "discounted_price": 202.77
      },
      "product_rating": {
        "rating": 4.7,
        "out_of": 5
      },
      "category": "Toys & Games",
      "number_of_ratings_reviews": 555,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Gourmet Delite",
      "product_image_link": "https://product-photos.net/img/grocery/gourmet-delite.jpg",
      "product_description": "Indulge in the finest culinary selection with Gourmet Delite. Our premium grocery line offers a curated collection of gourmet foods, artisan cheeses, and specialty ingredients. From exotic spices to artisanal chocolates, we bring the flavors of the world to your kitchen. Elevate your dining experience and delight your palate with every bite. Experience the difference of Gourmet Delite - where taste is an art.",
      "customer_comments": [
        {
          "comment": "Gourmet Delite left a bad taste in my mouth. The food was bland and overpriced, and the service was terrible. I had to wait an hour for my meal, and when it finally arrived, it was cold and unappetizing. I will never return.",
          "label": "Negative"
        },
        {
          "comment": "Gourmet Delite bietet köstliche Mahlzeiten, aber der Service kann manchmal langsam sein. Die Portionen sind großzügig, aber die Preise sind etwas hoch. Insgesamt ist es ein solides Essenserlebnis, das man genießen kann, wenn man Zeit hat.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 76.29,
        "discounted_price": 72.01
      },
      "product_rating": {
        "rating": 4.7,
        "out_of": 5
      },
      "category": "Grocery",
      "number_of_ratings_reviews": 784,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Zenith Comfort Sofa",
      "product_image_link": "https://retail-images.com/products/furniture/zenith-comfort-sofa.jpg",
      "product_description": "Indulge in unmatched comfort with the Zenith Comfort Sofa. Upholstered in premium fabric, this sofa invites you to sink into its plush cushions, providing a relaxing haven after a long day. The sleek lines and modern design seamlessly complement any living space, while its sturdy frame ensures years of enjoyment. Choose from a variety of colors to match your taste and create the perfect sanctuary for relaxation.",
      "customer_comments": [
        {
          "comment": "The Zenith Comfort Sofa offers a comfortable seating experience with ample cushioning. Its neutral color easily blends into any decor, and its sturdy construction ensures longevity. While assembly was straightforward, the sofa's firm cushions may not be ideal for everyone. Overall, it's a solid choice for those seeking a durable and versatile seating solution.",
          "label": "Neutral"
        },
        {
          "comment": "Generic Generate a realistic negative customer review for Zenith Comfort Sofa. Keep it under 50 words.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 2090.34,
        "discounted_price": 1580.44
      },
      "product_rating": {
        "rating": 4.5,
        "out_of": 5
      },
      "category": "Furniture",
      "number_of_ratings_reviews": 600,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Pawsitively Perfect",
      "product_image_link": "https://retail-images.com/products/pet supplies/pawsitively-perfect.jpg",
      "product_description": "Introducing Pawsitively Perfect, the ultimate solution for your furry friend's hygiene! Say goodbye to messy baths and smelly odors with our gentle and effective dry shampoo. Its hypoallergenic formula refreshes and cleanses your pet's coat, leaving it soft, shiny, and smelling its best. No-rinse convenience makes it a breeze to use, and the antistatic properties reduce tangles and mats. Keep your pet Pawsitively Perfect with every use!",
      "customer_comments": [
        {
          "comment": "Pawsitively Perfect has been a lifesaver for our furry friend, Max! Their groomers are incredibly gentle and patient, ensuring a stress-free experience for our anxious pup. Max always comes back looking and feeling his best, and we couldn't be happier with the services we've received. Highly recommend!",
          "label": "Positive"
        },
        {
          "comment": "Pawsitively Perfect provides reliable pet sitting services. My dog seemed comfortable and well-cared for during my absence. Communication could be improved, as I had to reach out to confirm arrangements a few times. Overall, a satisfactory experience.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 192.97,
        "discounted_price": 139.04
      },
      "product_rating": {
        "rating": 4.1,
        "out_of": 5
      },
      "category": "Pet Supplies",
      "number_of_ratings_reviews": 973,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "NeoTech SmartLink",
      "product_image_link": "https://retail-images.com/products/electronics/neotech-smartlink.jpg",
      "product_description": "Revolutionize your home network with NeoTech SmartLink! This cutting-edge router delivers lightning-fast Wi-Fi 6 speeds, ensuring seamless streaming and online gaming. Its advanced mesh technology extends coverage throughout your entire home, eliminating dead zones. With parental controls and enhanced security features, you can enjoy a secure and connected home experience. Get rid of your old router and upgrade to NeoTech SmartLink today for a connected future!",
      "customer_comments": [
        {
          "comment": "NeoTech SmartLink failed to live up to expectations. The device was constantly disconnecting, rendering it unreliable for home automation. Poor customer service further exacerbated the experience, with long wait times and unhelpful responses. I would not recommend this product.",
          "label": "Negative"
        },
        {
          "comment": "NeoTech SmartLink offers a convenient solution for smart home integration, but its reliability can be inconsistent at times. Functionality can be great when it works, but occasional glitches can lead to frustration. Overall, it's a decent option but could improve with enhanced stability.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 828.19,
        "discounted_price": 651.78
      },
      "product_rating": {
        "rating": 3.4,
        "out_of": 5
      },
      "category": "Electronics",
      "number_of_ratings_reviews": 338,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Astral Aura",
      "product_image_link": "https://store-assets.org/photos/fashion/astral-aura.jpg",
      "product_description": "Embrace ethereal beauty with Astral Aura, a limited-edition celestial collection. Crafted from shimmering fabrics and adorned with intricate beadwork, each piece captures the mystery and magic of the night sky. From ethereal gowns to celestial-inspired accessories, let Astral Aura elevate your style to cosmic heights.",
      "customer_comments": [
        {
          "comment": "Astral Aura offers a decent selection of spiritual goods. While some items, like their crystals, are of good quality, others, such as their candles, are overpriced and underwhelming. Overall, an average experience with some hits and misses.",
          "label": "Neutral"
        },
        {
          "comment": "Astral Aura offers a decent selection of crystals and other metaphysical items. Their prices are average, and the quality of their products is hit or miss. I've had some good experiences with them, but I've also been disappointed on occasion. Overall, I would say they're a mediocre store that's worth checking out if you're in the area.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 312.69,
        "discounted_price": 226.0
      },
      "product_rating": {
        "rating": 3.9,
        "out_of": 5
      },
      "category": "Fashion",
      "number_of_ratings_reviews": 244,
      "availability_status": "In Stock"
    },
    {
      "product_name": "QuantumClean X2000",
      "product_image_link": "https://example-store.com/images/home appliances/quantumclean-x2000.jpg",
      "product_description": "Experience the cutting-edge QuantumClean X2000, a revolutionary home appliance that harnesses the power of electrolysis to provide unparalleled cleaning. With its advanced technology, it effortlessly removes dirt, stains, and allergens from your fabrics, leaving them hygienically clean and rejuvenated. Its sleek design and user-friendly interface make it a seamless addition to any home. Upgrade your cleaning routine today with QuantumClean X2000 and unlock the future of spotless living.",
      "customer_comments": [
        {
          "comment": "Generic Generate a realistic negative customer review for QuantumClean X2000. Keep it under 50 words.",
          "label": "Negative"
        },
        {
          "comment": "The QuantumClean X2000 is a decent cleaning device. It's easy to use and does a good job on most surfaces. However, I found it struggled with particularly stubborn stains. Overall, it's a solid option for basic cleaning tasks.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 2461.12,
        "discounted_price": 1863.16
      },
      "product_rating": {
        "rating": 4.2,
        "out_of": 5
      },
      "category": "Home Appliances",
      "number_of_ratings_reviews": 777,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Emberlight Chronicles",
      "product_image_link": "https://product-photos.net/img/books/emberlight-chronicles.jpg",
      "product_description": "Immerse yourself in Emberlight Chronicles, a captivating fantasy trilogy where ancient prophecies collide with destiny. Follow the epic journeys of three extraordinary heroes as they uncover their true powers and confront the sinister forces that threaten the realms of Emberlight and beyond. With heart-pounding battles, intricate world-building, and unforgettable characters, Emberlight Chronicles will leave you enthralled from beginning to end.",
      "customer_comments": [
        {
          "comment": "Generic Generate a realistic negative customer review for Emberlight Chronicles. Keep it under 50 words.",
          "label": "Negative"
        },
        {
          "comment": "Generic Generate a realistic negative customer review for Emberlight Chronicles. Keep it under 50 words.",
          "label": "Negative"
        }
      ],
      "product_price": {
        "current_price": 27.94,
        "discounted_price": 23.42
      },
      "product_rating": {
        "rating": 3.7,
        "out_of": 5
      },
      "category": "Books",
      "number_of_ratings_reviews": 591,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "ApexFlex Pro",
      "product_image_link": "https://retail-images.com/products/sports & outdoors/apexflex-pro.jpg",
      "product_description": "ApexFlex Pro: Unleash Your Fitness Potential!\n\nElevate your workouts with ApexFlex Pro, the ultimate resistance band system. Combining the benefits of free weights and machines, it provides versatile and effective full-body workouts. Its adjustable resistance levels cater to all fitness abilities, enabling you to challenge yourself and achieve your fitness goals. With its portable design and comprehensive exercise guide, you can enjoy gym-quality workouts anytime, anywhere.",
      "customer_comments": [
        {
          "comment": "Purchased the ApexFlex Pro back brace after suffering from chronic back pain. Despite following the instructions diligently, I experienced no improvement. In fact, the brace seemed to worsen my pain, causing discomfort and irritation. I'm extremely disappointed with this product and would not recommend it to anyone.",
          "label": "Negative"
        },
        {
          "comment": "ApexFlex Pro offers a decent workout but lacks some features found in premium models. The resistance is smooth and the app integration is helpful, but the seat could be more comfortable and the range of motion is limited. Overall, it's a solid budget option for home gym enthusiasts with modest expectations.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 117.84,
        "discounted_price": 111.59
      },
      "product_rating": {
        "rating": 4.7,
        "out_of": 5
      },
      "category": "Sports & Outdoors",
      "number_of_ratings_reviews": 120,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Celestial Radiance",
      "product_image_link": "https://store-assets.org/photos/beauty & personal care/celestial-radiance.jpg",
      "product_description": "Unlock an ethereal glow with Celestial Radiance, a luxurious skincare serum infused with a symphony of botanical extracts. Its potent formula replenishes moisture, diminishes fine lines, and evens skin tone, leaving your complexion radiant and revitalized. Experience the transformative power of celestial radiance and embrace a visage that reflects the essence of starlight.",
      "customer_comments": [
        {
          "comment": "Celestial Radiance's products have a pleasant aroma and are easy to use. However, I found that some of their claims about the benefits were exaggerated. While I've noticed a slight improvement in my skin's radiance, the results were not as dramatic as advertised.",
          "label": "Neutral"
        },
        {
          "comment": "Celestial Radiance offers okay products. They're not bad, but they're not amazing either. The price is reasonable, but I've found similar products elsewhere that I like more. I wouldn't go out of my way to recommend them, but if you're looking for a decent product at a fair price, they're worth considering.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 16.61,
        "discounted_price": 14.28
      },
      "product_rating": {
        "rating": 4.4,
        "out_of": 5
      },
      "category": "Beauty & Personal Care",
      "number_of_ratings_reviews": 357,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Generic Generate a realistic product name for the category: Toys & Games. Response should be just the name, no additional text.",
      "product_image_link": "https://example-store.com/images/toys & games/generic-generate-a-realistic-product-name-for-the-category:-toys-&-games.-response-should-be-just-the-name,-no-additional-text..jpg",
      "product_description": "Galaxy Explorer Spaceship",
      "customer_comments": [
        {
          "comment": "Interactive Alphabet Learning Animal Train",
          "label": "Positive"
        },
        {
          "comment": "Rainbow Unicorn Plush Toy",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 12.33,
        "discounted_price": 9.86
      },
      "product_rating": {
        "rating": 3.5,
        "out_of": 5
      },
      "category": "Toys & Games",
      "number_of_ratings_reviews": 380,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Gourmet Fusion Bites",
      "product_image_link": "https://example-store.com/images/grocery/gourmet-fusion-bites.jpg",
      "product_description": "Indulge in a culinary adventure with Gourmet Fusion Bites! These bite-sized morsels blend exotic flavors from around the world, creating a harmonious symphony of tastes. Each bite is a delectable fusion of textures and spices, tantalizing your taste buds and leaving you craving for more. Crafted with premium ingredients and intricate artistry, these bites are perfect for elevating any occasion, from sophisticated parties to intimate gatherings.",
      "customer_comments": [
        {
          "comment": "Gourmet Fusion Bites offers a unique culinary experience with their fusion dishes. The flavors are bold and creative, but the execution can be inconsistent at times. Some dishes impress with their harmonious blend of flavors, while others fall short due to overpowering spices or overcooked ingredients. Overall, the concept is promising, but the restaurant needs to refine its execution to deliver a consistently satisfying experience.",
          "label": "Neutral"
        },
        {
          "comment": "Gourmet Fusion Bites offers a variety of unique and flavorful options. The ingredients are fresh and the flavor combinations are well-executed. However, the portions are a bit small and the prices are on the higher side. Overall, it's a decent option for a quick bite, but not the best value for your money.",
          "label": "Neutral"
        }
      ],
      "product_price": {
        "current_price": 34.08,
        "discounted_price": 28.05
      },
      "product_rating": {
        "rating": 4.8,
        "out_of": 5
      },
      "category": "Grocery",
      "number_of_ratings_reviews": 147,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "Elysian Comfort",
      "product_image_link": "https://product-photos.net/img/furniture/elysian-comfort.jpg",
      "product_description": "Experience ultimate comfort with Elysian Comfort's premium furniture line. Our meticulously crafted pieces combine luxurious materials with ergonomic design, providing unparalleled support and relaxation. From plush sofas to cozy armchairs, each item is engineered to enhance your well-being and bring a touch of elegance to your living space. Immerse yourself in a haven of serenity with Elysian Comfort.",
      "customer_comments": [
        {
          "comment": "I highly recommend Elysian Comfort! Their customer service is exceptional, and they went above and beyond to help me find the perfect mattress for my needs. The mattress is incredibly comfortable, and I've noticed a significant improvement in my sleep quality. Thank you, Elysian Comfort!",
          "label": "Positive"
        },
        {
          "comment": "\"Elysian Comfort's mattresses are a dream! The plush, pressure-relieving material cradles my body like a cloud. I wake up feeling refreshed and rejuvenated every morning. Highly recommend!\"",
          "label": "Positive"
        }
      ],
      "product_price": {
        "current_price": 677.2,
        "discounted_price": 599.93
      },
      "product_rating": {
        "rating": 3.9,
        "out_of": 5
      },
      "category": "Furniture",
      "number_of_ratings_reviews": 805,
      "availability_status": "Limited Availability"
    },
    {
      "product_name": "Pawsitively Pampered",
      "product_image_link": "https://product-photos.net/img/pet supplies/pawsitively-pampered.jpg",
      "product_description": "Indulge your furry friend with Pawsitively Pampered! Our premium range of pet supplies is designed to make your companion's life a blissful paradise. From plush beds and cozy blankets to nutritious treats and toys that stimulate their minds, we have everything you need to keep your pet happy, healthy, and spoiled rotten. Spoil your precious pet with the paw-some pampering they deserve!",
      "customer_comments": [
        {
          "comment": "Pawsitively Pampered provides basic pet care services. While my pet was well-cared for, the staff seemed rushed and impersonal. The facilities were clean, but nothing special. Overall, it's an average pet care provider that gets the job done.",
          "label": "Neutral"
        },
        {
          "comment": "Pawsitively Pampered exceeded my expectations! My pup came home looking and feeling his best. The staff was friendly and professional, and they clearly love animals. I highly recommend their services for anyone looking for a top-notch grooming experience for their furry friend.",
          "label": "Positive"
        }
      ],
      "product_price": {
        "current_price": 197.91,
        "discounted_price": 183.09
      },
      "product_rating": {
        "rating": 3.8,
        "out_of": 5
      },
      "category": "Pet Supplies",
      "number_of_ratings_reviews": 944,
      "availability_status": "Out of Stock"
    },
    {
      "product_name": "SonicWave X4",
      "product_image_link": "https://example-store.com/images/electronics/sonicwave-x4.jpg",
      "product_description": "Indulge in unparalleled sound with the SonicWave X4. Its advanced acoustic design delivers breathtaking clarity, deep bass, and wide soundstage. Enjoy your favorite music, podcasts, and audiobooks like never before. Seamlessly connect via Bluetooth 5.0 and experience ultimate wireless freedom. The slim, ergonomic earbuds provide a comfortable and secure fit for optimal listening pleasure.",
      "customer_comments": [
        {
          "comment": "The SonicWave X4 is a decent toothbrush, but it's not the best I've tried. The cleaning power is good, but the battery life is a bit short. Overall, it's a good option for the price, but there are better options out there if you're willing to spend more.",
          "label": "Neutral"
        
        } 
      ]
    }
    }
        
        return jsonify(response), 200

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
