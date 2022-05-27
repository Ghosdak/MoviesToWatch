import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
movies_title = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
print(movies_title)

with open("movies.txt", mode='w', encoding='UTF-8') as file:
    for movie in reversed(movies_title):
        file.write(f"{movie}\n")