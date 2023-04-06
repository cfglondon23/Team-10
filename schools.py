#login for schools

import pandas as pd
names = []
locations = []
emails = []

schools_info = {1: {'email': '', 'password': ''}}
max_key = max(schools_info.keys())
new_key = max_key + 1
schools_info[new_key] = {'email': '', 'password': ''}

schools = pd.DataFrame(schools_info)
schools_transposed = schools.T