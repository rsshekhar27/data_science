# 6. Perform Operations on Files
# 6.1: From the raw data below create a Pandas Series 'Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'
# a) Print all elements in lower case
# b) Print all the elements in upper case
# c) Print the length of all the elements
# 6.2: From the raw data below create a Pandas Series ' Atul', 'John ', ' jack ', 'Sam'
# a) Print all elements after stripping spaces from the left and right
# b) Print all the elements after removing spaces from the left only
# c) Print all the elements after removing spaces from the right only
# 6.3: - Create a series from the raw data below 'India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'
# a) split the individual strings wherever ‘_’ comes and create a list out of it.
# b) Access the individual element of a list
# c) Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements
# 6.4: Create a series and replace either X or dog with XX-XX
# 'A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'
# 6.5: Create a series and remove dollar from the numeric values '12', '-$10', '$10,000'
# 6.6:- Create a series and reverse all lower case words 'india 1998', 'big country', np.nan
# 6.7: Create pandas series and print true if value is alphanumeric in series or false if value is not alpha numeric in series.
# '1', '2', '1a', '2b', '2003c'
# 6.8: Create pandas series and print true if value is containing ‘A’
# '1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'
# 6.9: Create pandas series and print in three columns value 0 or 1 is a or b or c exists in values 'a', 'a|b', np.nan, 'a|c'
# 6.10: Create pandas dataframe having keys and ltable and rtable as below - 'key': ['One', 'Two'], 'ltable': [1, 2] 'key': ['One', 'Two'], 'rtable': [4, 5] Merge both the tables based of key

import pandas as pd
import numpy as np

# 6.1 
series_1 = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
print(series_1)

# a) Print all elements in lower case
series_lower_cases = [str(ele).lower() for ele in series_1]
print(series_lower_cases)

# b) Print all the elements in upper case
series_upper_cases = [str(ele).upper() for ele in series_1]
print(series_upper_cases)

# c) Print the length of all the elements
print(len(series_1))

#################################################################

# 6.2 
series_2 = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
print(series_2)

# a) Print all elements after stripping spaces from the left and right
series_stripped = [str(ele).strip() for ele in series_2]
print(series_stripped)

# b) Print all the elements after removing spaces from the left only
series_lstripped = [str(ele).lstrip() for ele in series_2]
print(series_lstripped)

# c) Print all the elements after removing spaces from the right only
series_rstripped = [str(ele).rstrip() for ele in series_2]
print(series_rstripped)

#################################################################

# 6.3
series_3 = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
print(series_3)

# a) split the individual strings wherever ‘_’ comes and create a list out of it.
list_splited = [str(ele).split("_") for ele in series_3]
print(list_splited)

flatten_list = []

# b) Access the individual element of a list
for sublist in list_splited:
    for l in sublist:
        flatten_list.append(l)
        print(l)

# c) Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements
print(flatten_list)