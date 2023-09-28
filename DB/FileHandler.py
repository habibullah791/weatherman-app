import csv
from model.DayWeather import DayWeatherData  # Assuming you have the DayWeatherData class defined

class FileHandler:
    def __init__(self) -> None:
        pass
        
        
    def readFile(self, fileName):
        weatherDataList = []
        
        with open(fileName, 'r') as file:
            csvReader = csv.DictReader(file)
            
            for row in csvReader:
                if (
                    row['PKT'] and
                    row['Max TemperatureC'] and
                    row['Mean TemperatureC'] and
                    row['Min TemperatureC'] and
                    row['Max Humidity'] and
                    row[' Mean Humidity'].strip() and  # Removed leading space
                    row[' Min Humidity'].strip()       # Removed leading space
                ):
                    # Create a DayWeatherData object and add it to the list
                    dayWeather = DayWeatherData(
                        row['PKT'],
                        int(row['Max TemperatureC']),
                        int(row['Mean TemperatureC']),
                        int(row['Min TemperatureC']),
                        int(row['Max Humidity']),
                        int(row[' Mean Humidity']),
                        int(row[' Min Humidity'])
                    )
                    weatherDataList.append(dayWeather)
        
        return weatherDataList