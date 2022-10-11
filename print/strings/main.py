# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from gettext import find
from operator import index


scorer1 = "Ruud Gullit"
scorer2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = scorer1 + " " + str(goal_0) + ", " + scorer2 + " " +  str(goal_1)
report = scorer1 + f" scored in the {str(goal_0)}nd minute\n" +  scorer2 + f" scored in the {str(goal_1)}th minute"

player = scorer1
first_name = scorer1[:scorer1.find(" ")]
last_name_len= len(scorer1[scorer1.find(" ") + 1:])
last_name = scorer1[scorer1.find(" "):]
name_short = first_name[:1] + "." + last_name

chantsingle = (first_name + "! ") 
chantwithspace = len(first_name) * chantsingle 
chant = chantwithspace[:-1] #delete last space character
good_chant = chant[:-1] != " "


