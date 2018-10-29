# Box Calculator

# size of boxes
big = 5
med = 3
small = 1

# Amount of Items
number_items = int(input("How many items?"))

#Big
num_big_box = number_items // big
print ("Number of Big Boxes:", num_big_box)
big_stored_items = num_big_box * big
print ("Number of items stored in Big Boxes:", big_stored_items)
big_remainder = number_items - big_stored_items
print ("Items Remaining:", big_remainder)

#Med
num_med_box = big_remainder // med
print ("Number of Med Boxes:", num_med_box)
med_stored_items = num_med_box * med
print ("Number of items stored in Medium Boxes:", med_stored_items)
med_remainder = big_remainder - med_stored_items
print ("Items Remaining:", med_remainder)


#Small
num_small_box = med_remainder // small
print ("Number of Small Boxes:", num_small_box)
small_stored_items = num_small_box * small
print ("Number of items stored in Small Boxes:", small_stored_items)
small_remainder = med_remainder - small_stored_items
print ("Items Remaining:", small_remainder)

#Total Boxes
Total_boxes = num_big_box + num_med_box + num_small_box
print ("Total boxes used:", Total_boxes)
