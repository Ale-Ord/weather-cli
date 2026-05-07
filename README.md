# Weather CLI

A simple command-line weather application built with Python using the Open-Meteo API.

## Features

- Search weather by city
- Country filtering support
- Current temperature
- Wind speed and directon
- Real-time weather data
- Command-line interface (CLI)

## Technologies

- Pyrhon
- Requests
- Open-Meteo API
- Git & GitHub


## Instalation

Clone the repository:

```bash
git clone git@github.com:Ale-Ord/weather-cli.git
```

Enter the project directory:

```bash
cd weather-cli
```

Create vitural enviroment:

```bash
python3 -m venv venv
```

Activate vitual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Ren the application:

```bash
python3 weather.py "San José"
```

Example with country code:

```bash
python3 weather.py "San José" CR
```

##Example Output

```text
🌍 San José, Costa Rica
🌡 Temperature: 24°C
💨 Wind Speed: 12 km/h
🧭 Wind Direction: 180°
⏰ Time: 2026-05-07T10:00
```

## Future Improvements

- 5-day forecast
- Weather description
- Colored terminal output
- Vetter error handling
- Save favorite cities

##License

This project is open source and aviable under the MIT License.s

