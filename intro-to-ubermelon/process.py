log_file = open("um-server-01.txt")  # open 'um-server-01.txt' for parsing

# Take 'um-server-01.txt' as an argument for below function
def generate_sales_reports(log_file):
    for line in log_file:           # iterate over each line in input file
        line = line.rstrip()        # strip out any white spaces from each line
        day = line[0:3]             # select the first 3 character of each line and set it equal to 'day' variable
        if day == "Mon":            # Check to see 'day' variable matches our critieria
            print(line)             # print out each line if the day for the line matches our criteria


generate_sales_reports(log_file)    # calls our 'generate-sales-reports' function with the input file as an argument
