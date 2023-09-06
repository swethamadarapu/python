import re

my_string = "2020/01/21 03:23:02 pid 35530 john@john+proj_alpha+var1+1 123.12.111.001 [Unnamed P4Perl script/v76] 'user-changes -m 1 //depot/icm/proj/proj_alpha/var1/type_b/john_cell/...#have'"

match = re.search(r' ([0-9]*)ms\+([0-9]*)ms/([0-9]*)ms\+([0-9]*)ms\n', my_string)
print(match)

if match:
    name = match.group(4)
    print(name)
