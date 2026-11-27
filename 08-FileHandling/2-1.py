from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 2, item 1: movie details.
movie_title = 'Inception'
director = 'Christopher Nolan'
lead_actor = 'Leonardo DiCaprio'
file_name = BASE / 'movie_details.txt'
with file_name.open('w', encoding='utf-8') as file:
    file.write(f'Movie Title: {movie_title}\n')
    file.write(f'Director: {director}\n')
    file.write(f'Lead Actor: {lead_actor}\n')
print(f'Movie details have been written to {file_name.name}.')
