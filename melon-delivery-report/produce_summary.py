
def display_deliveries(the_file):
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        melon, count, amount = words[0], words[1], words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")


print("Day 1")
the_file = open("um-deliveries-day-1.txt")
display_deliveries(the_file)
the_file.close()

print("Day 2")
the_file = open("um-deliveries-day-2.txt")
display_deliveries(the_file)
the_file.close()

print("Day 3")
the_file = open("um-deliveries-day-3.txt")
display_deliveries(the_file)
the_file.close()
