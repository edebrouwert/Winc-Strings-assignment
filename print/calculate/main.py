# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
from audioop import avg


broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7
sum_one_each = broccoli + leek + potato + brussel_sprout
avg_price = sum_one_each / 4
num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10
sum_total = (broccoli * num_broccolis) + (brussel_sprout * num_brussel_sprouts) + (leek * num_leeks) + (potato * num_potatoes)
discount_percentage = 0.3
discounted_sum_total = sum_total - (discount_percentage * sum_total)
print(round(discounted_sum_total,2))
