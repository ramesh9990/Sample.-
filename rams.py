import tkinter as tk
from tkinter import messagebox


API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()
        
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        
        result_label.config(text=f"Temperature: {temp} °C\nCondition: {weather_desc.capitalize()}")
        
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found. Please check the city name.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# Set up the GUI
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter city name:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

root.mainloop()
