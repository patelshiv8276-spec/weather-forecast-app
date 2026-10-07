import os
import customtkinter as ctk
import requests
from dotenv import load_dotenv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Set theme and appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Weather Application & Forecast (°F / mph)")
        self.geometry("750x550")
        self.resizable(False, False)

        # Main Layout: Left side for current weather, Right side for graph
        self.left_frame = ctk.CTkFrame(self, width=280)
        self.left_frame.pack(side="left", fill="both", padx=15, pady=15, expand=False)

        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", padx=15, pady=15, expand=True)

        # --- LEFT FRAME: Search & Current Weather ---
        self.title_label = ctk.CTkLabel(
            self.left_frame, text="Weather App", font=ctk.CTkFont(size=22, weight="bold")
        )
        self.title_label.pack(pady=(15, 10))

        self.city_entry = ctk.CTkEntry(
            self.left_frame, placeholder_text="Enter city...", width=220, height=35
        )
        self.city_entry.pack(pady=5)
        self.city_entry.bind("<Return>", lambda e: self.fetch_weather())

        self.search_btn = ctk.CTkButton(
            self.left_frame, text="Search", width=220, height=35, command=self.fetch_weather
        )
        self.search_btn.pack(pady=10)

        # Weather Details Card
        self.card = ctk.CTkFrame(self.left_frame, corner_radius=12)
        self.card.pack(pady=10, padx=10, fill="both", expand=True)

        self.city_label = ctk.CTkLabel(self.card, text="--", font=ctk.CTkFont(size=18, weight="bold"))
        self.city_label.pack(pady=(15, 2))

        self.temp_label = ctk.CTkLabel(self.card, text="--°F", font=ctk.CTkFont(size=40, weight="bold"))
        self.temp_label.pack(pady=5)

        self.desc_label = ctk.CTkLabel(self.card, text="Enter city name", font=ctk.CTkFont(size=12, slant="italic"))
        self.desc_label.pack(pady=2)

        self.humidity_label = ctk.CTkLabel(self.card, text="Humidity: --", font=ctk.CTkFont(size=12))
        self.humidity_label.pack(pady=3)

        self.wind_label = ctk.CTkLabel(self.card, text="Wind: --", font=ctk.CTkFont(size=12))
        self.wind_label.pack(pady=3)

        # --- RIGHT FRAME: Matplotlib Plot Area ---
        self.graph_title = ctk.CTkLabel(
            self.right_frame, text="5-Day Temperature Trend (°F)", font=ctk.CTkFont(size=16, weight="bold")
        )
        self.graph_title.pack(pady=(10, 5))

        # Initialize Matplotlib Figure
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.fig.patch.set_facecolor('#2b2b2b')  # Dark background matching CustomTkinter
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('#1e1e1e')
        self.ax.tick_params(colors='white', labelsize=8)
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        # Embed Matplotlib Canvas into Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

    def fetch_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            self.desc_label.configure(text="Please enter a city.")
            return

        if not API_KEY:
            self.desc_label.configure(text="API key missing in .env")
            return

        params = {"q": city, "appid": API_KEY, "units": "imperial"}

        try:
            # 1. Fetch Current Weather
            res_curr = requests.get(WEATHER_URL, params=params)
            res_curr.raise_for_status()
            data_curr = res_curr.json()

            self.city_label.configure(text=f"{data_curr['name']}, {data_curr['sys']['country']}")
            self.temp_label.configure(text=f"{round(data_curr['main']['temp'])}°F")
            self.desc_label.configure(text=data_curr['weather'][0]['description'].capitalize())
            self.humidity_label.configure(text=f"Humidity: {data_curr['main']['humidity']}%")
            self.wind_label.configure(text=f"Wind: {round(data_curr['wind']['speed'])} mph")

            # 2. Fetch 5-Day Forecast
            res_fore = requests.get(FORECAST_URL, params=params)
            res_fore.raise_for_status()
            data_fore = res_fore.json()

            # Parse timestamps and temperatures
            dates = []
            temps = []
            for item in data_fore["list"][::2]:
                dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
                dates.append(dt.strftime("%d %b\n%H:%M"))
                temps.append(item["main"]["temp"])

            # 3. Update Matplotlib Plot
            self.ax.clear()
            self.ax.plot(dates, temps, color='#3a7ebf', marker='o', linewidth=2, markersize=4)
            self.ax.set_ylabel("Temp (°F)", color='white', fontsize=10)
            self.ax.tick_params(colors='white', labelsize=7)
            self.ax.set_xticklabels(dates, rotation=45, ha='right')
            self.fig.tight_layout()
            
            # Redraw canvas
            self.canvas.draw()

        except requests.exceptions.HTTPError:
            self.desc_label.configure(text="City not found.")
        except requests.exceptions.RequestException:
            self.desc_label.configure(text="Network error.")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()