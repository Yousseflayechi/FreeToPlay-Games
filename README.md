# FreeToPlay Games API Scraper

This Python project is a basic script that interacts with the FreeToGame API to retrieve information about free-to-play games and randomly selects and displays a game title from the fetched data based on a chosen platform.

## Getting Started

To run this project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/FreeToPlay-Games-API-Scraper.git
   ```

2. Change to the project directory:

   ```bash
   cd FreeToPlay-Games-API-Scraper
   ```

3. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

4. Install the required packages using pip:

   ```bash
   pip install requests
   ```

5. Run the script:

   ```bash
   python main.py
   ```

6. Follow the on-screen instructions to input your preferred platform.

7. The script will fetch data from the FreeToGame API based on your chosen platform, store the game information in a list, and then randomly select and display a game title from the fetched data.

## How It Works

- The script uses the `requests` library to send a GET request to the FreeToGame API, requesting data for free-to-play games on a specific platform.

- The fetched data is processed to extract relevant information such as game ID, title, thumbnail URL, game URL, and release date.

- This information is stored in a list of dictionaries, with each dictionary representing a game.

- A random game title is then selected from the list and displayed on the console.

## Configuration

You can modify the `url` variable to change the base URL of the API if needed.

```python
url = "https://www.freetogame.com/api/games?platform="
```

## Dependencies

- Python 3.x
- `requests` library

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FreeToGame API](https://www.freetogame.com/api) for providing access to free-to-play game data.

Feel free to extend or modify this project to suit your needs, and don't forget to check the [FreeToGame API documentation](https://www.freetogame.com/api) for more information on available endpoints and data.
