import pandas as pd

school_df = pd.read_csv('schools.csv', header=None)

# Assign column names based on the first row
school_df.columns = school_df.iloc[0]

# Drop the first row since it now contains column names
school_df = school_df[1:]

# Convert relevant columns to numeric type, handling errors with coerce
numeric_columns = ['average_math', 'average_reading', 'average_writing', 'percent_tested']
school_df[numeric_columns] = school_df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Calculate the max possible score (assuming each subject has a max score of 800)
max_possible_score = 800

# Filter rows where the results are at least 80% of the max possible score
filtered_df = school_df[school_df['average_math'] >= 0.8 * max_possible_score]

# Create the best_math_schools DataFrame with "school_name" and "average_math" columns
best_math_schools_df = filtered_df[['school_name', 'average_math']]

# Sort the DataFrame by "average_math" in descending order
best_math_schools_df = best_math_schools_df.sort_values(by='average_math', ascending=False)

# Display the resulting DataFrame
print(best_math_schools_df)

# Calculate the total SAT score by summing scores across the three sections
school_df['total_SAT'] = school_df['average_math'] + school_df['average_reading'] + school_df['average_writing']

# Select the top 10 performing schools based on total SAT scores
top_10_schools = school_df[['school_name', 'total_SAT']].sort_values(by='total_SAT', ascending=False).head(10)

# Display the resulting DataFrame
print(top_10_schools)

# Group by borough and calculate mean and standard deviation for total_SAT
borough_stats = school_df.groupby('borough')['total_SAT'].agg(['mean', 'std', 'count']).round(2)

# Find the borough with the largest standard deviation
largest_std_dev = borough_stats[borough_stats['std'] == borough_stats['std'].max()]

# Rename columns and display the resulting DataFrame
largest_std_dev = largest_std_dev.rename(columns={'mean': 'num_schools', 'std': 'std_SAT'})
print(largest_std_dev)