import requests
import time
API_KEY = 'fca3f495ae75453b976162534240704'
def get_weather_by_city(city_name):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
def display_weather(weather_data):
    if weather_data:
        weather = weather_data['current']['condition']['text']
        temp = round(weather_data['current']['temp_f'])
        print(f"The weather is: {weather}")
        print(f"The temperature is: {temp}°F")
    else:
        print("Weather data not available")
def add_to_favorites(city_name, favorites):
    favorites.append(city_name)
    print(f"{city_name} added to favorites")
def remove_from_favorites(city_name, favorites):
    if city_name in favorites:
        favorites.remove(city_name)
        print(f"{city_name} removed from favorites")
    else:
        print(f"{city_name} not found in favorites")
def list_favorites(favorites):
    if favorites:
        print("Favorites:")
        for city in favorites:
            print(city)
    else:
        print("No favorites added yet")
def main():
    favorites = []
    while True:
        print("Choose an action:")
        print("1. Check the weather")
        print("2. Show favorites")
        print("3. Add to favorites")
        print("4. Remove from favorites")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            city_name = input("Enter the city name: ")
            weather_data = get_weather_by_city(city_name)
            display_weather(weather_data)
        elif choice == '2':
            list_favorites(favorites)
        elif choice == '3':
            city_name = input("Enter the city name to add to favorites: ")
            add_to_favorites(city_name, favorites)
        elif choice == '4':
            city_name = input("Enter the city name to remove from favorites: ")
            remove_from_favorites(city_name, favorites)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice")
        time.sleep(15)
if __name__ == "__main__":
    main()