# Import pandas under its usual alias
import pandas as pd

import matplotlib.pyplot as plt

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv('netflix_data.csv')

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df.query('type == "Movie"')

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"])

# Create a title
plt.title('Movie Duration by Year of Release')
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")

# Show the plot
plt.show()

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for index, row in netflix_movies_col_subset.iterrows():
    if row["genre"] == "Children":
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('blue')
    elif row['genre'] == 'Stand-Up':
        colors.append('green')
    else:
        colors.append('black')

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))
genre_color_dict = {'Children': 'red', 'Documentaries': 'blue', 'Stand-Up': 'green', 'Others': 'black'}

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], color=colors)

# Create a title and axis labels and legend

# Create a legend with the genre names and corresponding colors
plt.title('Movie Duration by Year of Release')
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=genre, markerfacecolor=color, markersize=10)
                   for genre, color in genre_color_dict.items()]

plt.legend(handles=legend_elements, loc='upper left')

# Show the plot
plt.show()
# Are we certain that movies are getting shorter?
are_movies_getting_shorter = "No"
print(f"Are movies getting shorter: {are_movies_getting_shorter}")
