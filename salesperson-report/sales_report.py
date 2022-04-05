"""Generate sales report showing total melons each salesperson sold."""

# improvement: consolidate the 2 separate lists as 1 dictionary
sales_info = {}

# Open 'sales-report.txt' for parsing
f = open('sales-report.txt')

# iterate over each line of the input file for data processing
# improvement: update code to perform read/write operations to new dictionary
for line in f:
    line = line.rstrip()            # strip out white space at end of each line
    entries = line.split('|')       # splits each line using '|' as delimiter, store result as a list
    salesperson = entries[0]        # First element of the list contains the salesperson's name, save that as 'salesperson' variable
    melons_sold = int(entries[2])   # convert the number of melons sold into Integer data type and save it as 'melons_sold' variable

    # Add salesperson and melons sold info to 'sales_info' dictionary if they don't have an existing entry, 
    # otherwise update their amount of melons sold
    sales_info[salesperson] = melons_sold if salesperson not in sales_info else sales_info[salesperson] + melons_sold

# Iterate over 'sales_info' dictionary, and print out each salesperson and their amount of melons sold
for key, value in sales_info.items():
    print(f'{key} sold {value} melons')
