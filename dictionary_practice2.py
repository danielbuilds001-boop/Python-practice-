def add_movies(movies):
    title = input("What is the name of the movie (q to quit): ").strip().title()
    if title.lower() == "q":
        return False

    if not title:
        print("The name of the movie cannot be empty.")
        return True

    try:
        year = int(input("Enter the year the movie released: ").strip())
        rating = int(input("Enter the movie rating: ").strip())

    except ValueError:
        print("Invalid input please try again.")
        return True

    movies[title] = {
        "year": year,
        "rating": rating
    }
    print(f'Successfully added {title}')
    return True

def display_movies(movies):
    if not movies:
        print("There are no movies avaliable.")
        return True

    for title,details in movies.items():
        print(f'\n{title}')
        print(f'Year: {details["year"]}')
        print(f'Rating: {details["rating"]}/10')

def main():
    movies = {}
    while True:
        keep_going = add_movies(movies)
        
        if not keep_going:
            break
        if not movies:
            break
            
            return
        display_movies(movies)
        
        return

if __name__ == '__main__':
    main()
    
