import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("liqwinners.csv")

char_count = data.groupby(['year', 'character']).size().reset_index(name='count')
years = list(set(char_count['year']))
characters = list(set(char_count['character']))
#print(characters)

count_data = {'year': [], 'character': [], 'count': []}
for year in years:
    year_data = char_count[char_count['year'] == year]
    print(f"Year: {year_data}")
    for character in characters:
        count = year_data[year_data['character'] == character]['count'].values
        print(f"count: {count}")
        count_data['year'].append(year)
        count_data['character'].append(character)
        count_data['count'].append(count[0] if len(count) > 0 else 0)


df = pd.DataFrame(count_data)

fig, ax = plt.subplots(figsize=(10,6))

for character in characters:
    char_data = df[df['character'] == character]
    ax.plot(char_data['year'], char_data['count'], label=character) # label for each character count for the graph


ax.set_xlabel("Year")
ax.set_ylabel("Character")
ax.set_title("Melee Solo Character Win Count")
ax.legend()
plt.xticks(rotation=45)
plt.xticks(years)
plt.show()
print(char_count.to_csv("character_count.csv"))