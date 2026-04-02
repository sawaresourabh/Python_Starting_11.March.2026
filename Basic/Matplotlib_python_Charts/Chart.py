# this is the very first chart we are going to create using matplotlib library in python.
# todays date is 11th March 2026 and we are going to create a horizontal bar chart to show the total views by genre.

import matplotlib.pyplot as plt

genres = ['History', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller']
views = [3980388, 4633792, 5215443, 6117933, 7392205, 6168403]

plt.barh(genres, views)
plt.xlabel("Total Views")
plt.title("Views by Genre")
plt.show()