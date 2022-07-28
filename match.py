from pull import pull_data
import random
p1 = pull_data("Ben Shelton", 500)

p2 = pull_data("Tim Van Rijthoven", 500)

# p1['1st%'] = ((p1["1st%"])+(1-p2["1streturn"]))/2
# p1['2nd%'] = ((p1["2nd%"])+(1-p2["2ndreturn"]))/2
# p2['1st%'] = ((p2["1st%"])+(1-p1["1streturn"]))/2
# p2['2nd%'] = ((p2["2nd%"])+(1-p1["2ndreturn"]))/2
# p1["ace"] =  ((p1["ace"])+(p2["returnace"]))/2
# p2["ace"] =  ((p2["ace"])+(p1["returnace"]))/2
# p1["bp"] = ((1-p2["bp_saved"])+p1["bp"])/2
# p2["bp"] = ((1-p1["bp_saved"])+p2["bp"])/2

print(p1)
print(p2)