# 🌤️ Modern Weather & 5-Day Forecast Application

A sleek, dark-themed desktop application built with Python, CustomTkinter, and Matplotlib. It fetches real-time meteorological data and 5-day weather trends from the OpenWeatherMap REST API and renders interactive forecast graphs directly within the user interface.

---

## 🌟 Features

- **Real-Time Data Fetching:** Queries OpenWeatherMap REST API endpoints for current weather metrics (Temperature, Humidity, Wind Speed, Weather Conditions).
- **Interactive 5-Day Forecast Chart:** Embedded Matplotlib canvas displaying 5-day / 3-hour interval temperature trends in Imperial units (°F / mph).
- **Modern UI Architecture:** Object-Oriented CustomTkinter desktop interface built with event-driven search bindings (`<Return>` key / button clicks).
- **Secure Key Management:** Uses `python-dotenv` to load API credentials securely from local environment variables, keeping sensitive keys out of source control.
- **Graceful Error Handling:** Robust HTTP error handling for invalid city queries, unactivated/missing API keys, or network connection timeouts.
- **Standalone Binary Executable:** Pre-compiled Windows `.exe` created via PyInstaller for zero-dependency execution.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.10+
- **GUI Framework:** `customtkinter`
- **Data Visualization:** `matplotlib`
- **Networking:** `requests`
- **Environment Management:** `python-dotenv`
- **Compiler:** `pyinstaller`
- **API Provider:** [OpenWeatherMap API](https://openweathermap.org/api)

---

## 📁 Project Structure

```text
weather-forecast-app/
│
├── gui_weather.py      # Main application entry point and GUI logic
├── .env                # Local API key storage (excluded from Git)
├── .gitignore          # Prevents committing build files and secret keys
├── requirements.txt    # Project Python dependencies
└── README.md           # Project documentation

🚀 Getting Started
Prerequisites
Python 3.x installed on your machine.

A free API Key from OpenWeatherMap.

Installation & Setup
Clone the repository:
git clone [[https://github.com/patelshiv8276-spec/weather-forecast-app.git](https://github.com/patelshiv8276-spec/weather-forecast-app.git)
cd weather-forecast-app

Install required dependencies:
pip install customtkinter requests matplotlib python-dotenv pyinstaller

Configure your Environment File:
Create a .env file in the root directory of the project and add your 

OpenWeatherMap API key:
Code snippet
OPENWEATHER_API_KEY=your_actual_api_key_here

Run the Application:
python gui_weather.py

📦 Building a Standalone Executable (.exe)

To bundle the Python application into a single executable file that runs without requiring Python installed:
python -m PyInstaller --noconsole --onefile gui_weather.py

Note: Copy your .env file into the dist/ folder right alongside gui_weather.exe so the standalone application can load your credentials at runtime.

<img width="753" height="582" alt="image" src="https://github.com/user-attachments/assets/ef385204-4085-4c40-a3a7-6b06f3e1c738" />


📄 License
This project is open-source and available under the MIT License.
