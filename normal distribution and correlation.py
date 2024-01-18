import pandas as pd

# Read the CSV file into a pandas DataFrame without specifying header names
school_df = pd.read_csv('schools.csv', header=None)

# Assign column names based on the first row
school_df.columns = school_df.iloc[0]

# Drop the first row since it now contains column names
school_df = school_df[1:]

# Convert relevant columns to numeric type, handling errors with coerce
numeric_columns = ['average_math', 'average_reading', 'average_writing', 'percent_tested']
school_df[numeric_columns] = school_df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Filter rows where the average_math is greater than 500
filtered_df = school_df[school_df['average_math'] > 500]

# Display the filtered DataFrame
print("\nFiltered DataFrame:")
print(filtered_df)

# Assuming you want to perform an ordered merge based on the 'school_name' column
ordered_merge_result = pd.merge_ordered(school_df, school_df, on='school_name')

# Display the ordered merge result
print("\nOrdered Merge Result:")
print(ordered_merge_result)

# Calculate mean and standard deviation of the 'average_math' column
mean_value = school_df['average_math'].mean()
std_deviation = school_df['average_math'].std()

print("\nMean of 'average_math':", mean_value)
print("Standard Deviation of 'average_math':", std_deviation)