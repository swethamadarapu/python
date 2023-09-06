import re

string = "2020/01/21 03:23:02 pid 35530 john@john+proj_alpha+var1+1 123.12.111.001 [Unnamed P4Perl script/v76] 'user-changes -m 1 //depot/icm/proj/proj_alpha/var1/type_b/john_cell/...#have' et wait"

# Define a regular expression pattern to match the date and time
pattern = r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}'

# Use the re.search() function to find the first match of the pattern in the string
match = re.search(pattern, string)

# Extract the matched string and print it
read_time = match.group()
print(read_time)

