from python_amazon_fees.parse import AmazonFeesCalculator

def handler(length,
            width,
            height,
            weight,
            is_media=False,
            is_apparel=False,
            is_pro=False):
    calculator = AmazonFeesCalculator(length, width, height, weight, is_media, is_apparel, is_pro)
    return calculator.fees()

print(handler(1,1,1,1))
