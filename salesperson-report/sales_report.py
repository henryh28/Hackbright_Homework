"""Generate sales report showing total melons each salesperson sold."""

# Create 2 separate lists to track salespeople & corresponding amount 
# of melons sold for each salesperson
salespeople = []
melons_sold = []

# Open 'sales-report.txt' for parsing
f = open('sales-report.txt')

# iterate over each line of the input file for data processing
for line in f:
    line = line.rstrip()            # strip out white space at end of each line
    entries = line.split('|')       # splits each line using '|' as delimiter, store result as a list
    salesperson = entries[0]        # First element of the list contains the salesperson's name, save that as 'salesperson' variable
    melons = int(entries[2])        # convert the number of melons sold into Integer data type and save it as 'melons' variable

    # Find the index of a salesperson if they exist in the 'salespeople' list, and use that index to update amount 
    # of melons sold in 'melons_sold' list
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
        
    else: # Otherwise, add their name to 'salespeople' list and amount of melons sold to 'melons_sold' list
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Iterate over 'salespeople' list, using current index to print out the salesperson's name and corresponding amount of melons sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')