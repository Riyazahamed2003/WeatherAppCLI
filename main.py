import get_weather_data
import weather_summary

def main():
    weather_data = get_weather_data.get_weather_data()
    weather_summary.print_weather_summary(weather_data)

if __name__ == "__main__":
    main()
