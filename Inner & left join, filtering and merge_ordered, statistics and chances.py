import pandas as pd
from csv import reader

# Read the CSV file into a pandas DataFrame without specifying header names
schools_df = pd.read_csv('schools.csv', header=None)

# Display the first few rows of the DataFrame to inspect the structure
print(schools_df.head())

# Assuming you want to join based on the first column (index 0)
# Perform inner join
inner_join_result = pd.merge(schools_df, schools_df, how='inner', left_on=0, right_on=0)

# Perform left join
left_join_result = pd.merge(schools_df, schools_df, how='left', left_on=0, right_on=0)

# Save or use the results as needed
inner_join_result.to_csv('inner_join_result.csv', index=False)
left_join_result.to_csv('left_join_result.csv', index=False)