starting_address = int(starting_address[p_mask-1:],2)
ending_address = AND(comp(mask),address)
ending_address = int(ending_address[p_mask-1:],2)
print(starting_address,ending_address)