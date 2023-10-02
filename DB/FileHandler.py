import csv
from model.DayWeather import DayWeatherData  # Assuming you have the DayWeatherData class defined

class FileHandler:
    def __init__(self) -> None:
        pass
        
        
    def readFile(self, fileName):
        
        '''
            @param fileName: The path to the CSV file containing weather data (str).            
            @desc: This method reads weather data from a CSV file, creates DayWeatherData objects
                for valid rows, and returns a list of DayWeatherData objects.
            @return: A list of DayWeatherData objects representing the weather data.
        '''
        weatherDataList = []
        
        
        try:        
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
        except FileNotFoundError:
            print(f"File not found: {fileName}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
        
        return weatherDataList
