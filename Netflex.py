# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df=pd.read_csv("netflix_titles.csv")


# %%
df.info()

# %%
print(df.shape)


# %%
print(df.columns.to_list())

# %%
print(df.duplicated().sum())

# %%
df['date_added'] = df['date_added'].str.strip()




# %%
df['date_added'] = pd.to_datetime(df['date_added'], format='mixed', errors='coerce')
df['date_added']=pd.to_datetime(df['date_added'])

# %%

df['director']=df['director'].fillna('Unknown')
df['cast']=df['cast'].fillna('Unknown')
df['country']=df['country'].fillna('Unknown')



# %%
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])


# %%
df= df.dropna(subset=['date_added', 'duration'])


# %%
print(df.isnull().sum())

# %%
df.columns
print(df.dtypes)

# %%
df['duration'].head(10)

# %%
df['duration_type'] = df['duration'].apply(lambda x: 'Season' if 'Season' in x else 'Minute')


# %%
df['duration_int'] = df['duration'].str.extract('(\d+)').astype(int)


# %%
df[['duration','duration_type','duration_int']].head()


# %%


# داده‌ها
type_counts = df['type'].value_counts()


plt.figure(figsize=(6,4), facecolor="#141414")


bars = plt.bar(type_counts.index, type_counts.values, 
               color="#E50914", width=0.5)


plt.title("Number of Netflix content by type", color="white", fontsize=14, pad=10)
plt.xlabel("Type", color="white", fontsize=12)
plt.ylabel("Count", color="white", fontsize=12)

plt.xticks(color="white", fontsize=10)
plt.yticks(color="white", fontsize=10)

ax = plt.gca()
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color("white")
ax.spines['left'].set_color("white")
ax.set_facecolor("#141414")

plt.tight_layout()
plt.show()


# %%
df['added_year']=df['date_added'].dt.year


# %% [markdown]
# Counting the number of content per year

# %%
YearCounts=df['added_year'].value_counts().sort_index()

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(12,5), facecolor="#141414")
plt.plot(YearCounts.index, YearCounts.values, marker='o', color="#E50914", linewidth=2)

plt.title("Counting the number of content per year", color="white")
plt.xlabel("Add year", color="white")
plt.ylabel("Content count", color="white")

plt.xticks(color="white")
plt.yticks(color="white")

plt.grid(True, color="#333333")  # شبکه‌ی ظریف خاکستری تیره
plt.gca().set_facecolor("#141414")

plt.show()



# %%
df['genres'] = df['listed_in'].str.split(', ')
genres_df = df.explode('genres')


# %%
genre_counts = genres_df['genres'].value_counts()


# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6), facecolor="#141414")
plt.bar(genre_counts.index[:10], genre_counts.values[:10], color="#E50914", width=0.5)

plt.title("Top genres in Netflix", color="white")
plt.xlabel("Genres", color="white")
plt.ylabel("Count", color="white")

plt.xticks(rotation=45, color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#141414")

plt.show()



# %%


PopularCountries = df['country'].value_counts().head(10)

plt.figure(figsize=(12,6), facecolor="#141414")
plt.bar(PopularCountries.index, PopularCountries.values, color="#E50914", width=0.5)

plt.title("Top 10 Countries with Most Netflix Content", color="white")
plt.xlabel("Country", color="white")
plt.ylabel("Count", color="white")

plt.xticks(rotation=45, color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#141414")

plt.show()


# %%
import matplotlib.pyplot as plt

Rating = df['rating'].value_counts()

plt.figure(figsize=(12,6), facecolor="#141414")
plt.bar(Rating.index, Rating.values, color="#E50914", width=0.5)

plt.title("Netflix Content Ratings", color="white")
plt.xlabel("Rating", color="white")
plt.ylabel("Count", color="white")

plt.xticks(rotation=45, color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#141414")

plt.show()


# %%
import matplotlib.pyplot as plt

Rating = df['rating'].value_counts()

plt.figure(figsize=(6,6), facecolor="#141414")

# نمودار دایره‌ای با رنگ‌های تیره و قرمز
plt.pie(
    Rating.values,
    labels=Rating.index,
    autopct='%1.1f%%',
    colors=["#E50914", "#B81D24", "#831010", "#404040", "#737373", "#999999"],  # طیف قرمز-خاکستری
    textprops={'color': 'white'}
)

plt.title("Netflix Ratings Distribution", color="white", fontsize=14)
plt.tight_layout()
plt.show()



# %%

plt.figure(figsize=(10,5), facecolor="#141414")
plt.hist(movies['duration_int'], bins=30, color="#E50914", edgecolor="white")

plt.title('Netflix Movie Duration Distribution', color="white")
plt.xlabel('Time (min)', color="white")
plt.ylabel('Movie Count', color="white")

plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#141414")

plt.tight_layout()
plt.show()



# %%

shows = df[df['type'] == 'TV Show']

plt.figure(figsize=(10,5), facecolor="#141414")
plt.hist(shows['duration_int'], bins=20, color="#E50914", edgecolor="white")

plt.title('Distribution of the Number of Seasons of Netflix Series', color="white")
plt.xlabel('Number of Seasons', color="white")
plt.ylabel('Number of Series', color="white")

plt.xticks(color="white")
plt.yticks(color="white")
plt.gca().set_facecolor("#141414")

plt.tight_layout()
plt.show()



# %%
Rating_Type=df.groupby(['type','rating']).size().unstack(fill_value=0)


# %%


Rating_Type.plot(kind='bar', figsize=(12,6), color="#E50914")

plt.title("Netflix Rating Types", color="white")
plt.xlabel("Rating Type", color="white")
plt.ylabel("Count", color="white")

plt.xticks(rotation=0, color="white")
plt.yticks(color="white")

plt.gca().set_facecolor("#141414")
plt.gcf().set_facecolor("#141414")

plt.tight_layout()
plt.show()



# %%


YearType = df.groupby(['added_year', 'type']).size().unstack(fill_value=0)

plt.figure(figsize=(12,5), facecolor="#141414")
YearType.plot(kind='line', color=["#E50914", "#B81D24"], linewidth=2)

plt.title("Netflix Content by Year and Type", color="white")
plt.xlabel("Year", color="white")
plt.ylabel("Content Count", color="white")

plt.xticks(color="white")
plt.yticks(color="white")

plt.grid(True, color="#333333")
plt.gca().set_facecolor("#141414")
plt.gcf().set_facecolor("#141414")

plt.tight_layout()
plt.show()



