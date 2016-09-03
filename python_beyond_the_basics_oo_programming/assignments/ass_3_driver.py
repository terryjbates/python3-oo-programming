#!/usr/bin/env python3

from assignment3 import ConfigDict

cc = ConfigDict('config_file.txt')
print(cc['sql_query'])
print(cc['email_to'])
cc['database'] = 'mysql_manage'

print(cc)