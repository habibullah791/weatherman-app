import os
import calendar
import json

from DB.FileHandler import FileHandler


class Utils:
    def __init__(self):
        self.fileHandler = FileHandler()


    def getFileName(self, year, month):
        '''
        @param year: The year for which the weather data is needed (int).
        @param month: The month for which the weather data is needed (int).

        @desc: This method constructs the filename for weather data based on the provided
            year and month and returns the full path to the file.

        @return: The full path to the weather data file (str).
        '''
        
        try:
            directory = 'data/weatherfiles'
            month = int(month)
            year = int(year)

            # Validate the month input (1-12)
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")

            # Trim the month number to a three-letter month abbreviation
            month_abbr = calendar.month_abbr[month][:3]

            # Generate a pattern for the filename based on the year and month abbreviation
            fileName = f'Murree_weather_{year}_{month_abbr}.txt'

            # Concatenate the directory path and filename
            fullPath = os.path.join(directory, fileName)

            return fullPath
        except ValueError as e:
            print(f"Error: {e}")
            return None  # Return None to indicate an error


    def convertToJSON(self, weatherDataList):
        '''
            @param weatherDataList: A list of weather data to be converted to JSON (list).        
            @desc: This method converts a list of weather data into a JSON-formatted string.        
            @return: A JSON-formatted string representing the weather data (str).
        '''
        weatherDataListJSON = json.dumps(weatherDataList, indent=2)
        return weatherDataListJSON


    def cal_HighestLowestTemperatureHumidity(self, year, month):
        
        '''
            @param year: The year for which to calculate the highest and lowest temperature
                        and humidity (int).
            @param month: The month for which to calculate the highest and lowest temperature
                        and humidity (int).            
            @desc: This method calculates and returns the highest and lowest temperature and humidity
                recorded for a given month and year based on the weather data in the associated file.
            
            @return: A list containing dictionaries with the following information:
                    - Highest temperature and the corresponding date (dict).
                    - Lowest temperature and the corresponding date (dict).
                    - Highest humidity and the corresponding date (dict).
        '''
        fileName = self.getFileName(year, month)
        dayWeatherList = self.fileHandler.readFile(fileName)

        highTemp = {'highest_temp': 0, 'date': ''}
        lowTemp = {'lowest_temp': 1000, 'date': ''}
        highHumid = {'highest_humid': 0, 'date': ''}

        for dayWeather in dayWeatherList:
            maxTemp = dayWeather.Max_TemperatureC
            minTemp = dayWeather.Min_TemperatureC
            maxHumid = dayWeather.Max_Humidity
            date = dayWeather.PKT

            if maxTemp > highTemp['highest_temp']:
                highTemp['highest_temp'] = maxTemp
                highTemp['date'] = date

            if minTemp < lowTemp['lowest_temp']:
                lowTemp['lowest_temp'] = minTemp
                highTemp['date'] = date

            if maxHumid > highHumid['highest_humid']:
                highHumid['highest_humid'] = maxHumid
                highTemp['date'] = date

        calculation = [highTemp, lowTemp, highHumid]

        return calculation


    def cal_TemperatureStat(self, year, month, category):
        
        '''
            @param year: The year for which to calculate temperature statistics (int).
            @param month: The month for which to calculate temperature statistics (int).
            @param category: The category of temperature statistics to calculate, one of:
                            - 'highestTemp': Calculate the highest temperature (str).
                            - 'lowestTemp': Calculate the lowest temperature (str).
                            - 'meanTemp': Calculate the mean temperature (str).
            
            @desc: This method calculates and returns temperature statistics for a given month
                and year based on the weather data in the associated file.
            
            @return: A dictionary containing the calculated temperature statistic and the
                    corresponding date (dict).
        '''
        fileName = self.getFileName(year, month)
        dayWeatherList = self.fileHandler.readFile(fileName)

        if category == 'highestTemp':
            highTemp = {'highest_temp': 0, 'date': ''}

            for dayWeather in dayWeatherList:
                maxTemp = dayWeather.Max_TemperatureC
                date = dayWeather.PKT

                if maxTemp > highTemp['highest_temp']:
                    highTemp['highest_temp'] = maxTemp
                    highTemp['date'] = date
            return highTemp

        elif category == 'lowestTemp':
            lowTemp = {'lowest_temp': 1000, 'date': ''}

            for dayWeather in dayWeatherList:
                maxTemp = dayWeather.Max_TemperatureC
                date = dayWeather.PKT

                if maxTemp < lowTemp['lowest_temp']:
                    lowTemp['lowest_temp'] = maxTemp
                    lowTemp['date'] = date
            return lowTemp

        elif category == 'meanTemp':
            meanTempt = {'mean_temp': 0, 'date': ''}

            for dayWeather in dayWeatherList:
                meanTemp = dayWeather.Mean_TemperatureC
                date = dayWeather.PKT

                if meanTemp > meanTempt['mean_temp']:
                    meanTempt['mean_temp'] = meanTemp
                    meanTempt['date'] = date
            return meanTempt



    def cal_HumidStat(self, year, month, category):
        '''
            @param year: The year for which to calculate humidity statistics (int).
            @param month: The month for which to calculate humidity statistics (int).
            @param category: The category of humidity statistics to calculate, one of:
                            - 'highestHumid': Calculate the highest humidity (str).
                            - 'lowestHumid': Calculate the lowest humidity (str).
                            - 'meanHumid': Calculate the mean humidity (str).
            
            @desc: This method calculates and returns humidity statistics for a given month
                and year based on the weather data in the associated file.
            
            @return: A dictionary containing the calculated humidity statistic and the
                    corresponding date (dict).
        '''
        fileName = self.getFileName(year, month)
        dayWeatherList = self.fileHandler.readFile(fileName)

        if category == 'highestHumid':
            highHumid = {'highest_humid': 0, 'date': ''}

            for dayWeather in dayWeatherList:
                maxTemp = dayWeather.Max_Humidity
                date = dayWeather.PKT

                if maxTemp > highHumid['highest_humid']:
                    highHumid['highest_humid'] = maxTemp
                    highHumid['date'] = date
            return highHumid

        elif category == 'lowestHumid':
            lowHumid = {'lowest_humid': 1000, 'date': ''}

            for dayWeather in dayWeatherList:
                maxTemp = dayWeather.Min_Humidity
                date = dayWeather.PKT

                if maxTemp < lowHumid['lowest_humid']:
                    lowHumid['lowest_humid'] = maxTemp
                    lowHumid['date'] = date
            return lowHumid

        elif category == 'meanHumid':
            meanHumid = {'mean_humid': 0, 'date': ''}

            for dayWeather in dayWeatherList:
                meanTemp = dayWeather.Mean_Humidity
                date = dayWeather.PKT

                if meanTemp > meanHumid['mean_humid']:
                    meanHumid['mean_humid'] = meanTemp
                    meanHumid['date'] = date
            return meanHumid


    def cal_AvgHighestLowestTemperatureHumidity(self, year, month):
        '''
            @param year: The year for which to calculate average temperature and humidity (int).
            @param month: The month for which to calculate average temperature and humidity (int).
            
            @desc: This method calculates and returns the average highest temperature, lowest temperature,
                and humidity for a given month and year based on the weather data in the associated file.
            
            @return: A list containing dictionaries with the following average information:
                    - Average highest temperature (dict).
                    - Average lowest temperature (dict).
                    - Average humidity (dict).
        '''
        
        fileName = self.getFileName(year, month)
        dayWeatherList = self.fileHandler.readFile(fileName)

        avgHighTemp = {'avg_highest_temp': 0}
        avgLowTemp = {'avg_lowest_temp': 0}
        avgHighHumid = {'avg_highest_humid': 0}

        for data in dayWeatherList:
            avgHighTemp['avg_highest_temp'] += data.Max_TemperatureC
            avgLowTemp['avg_lowest_temp'] += data.Min_TemperatureC
            avgHighHumid['avg_highest_humid'] += data.Mean_TemperatureC

        avgHighTemp['avg_highest_temp'] = int(avgHighTemp['avg_highest_temp'] / len(dayWeatherList))
        avgLowTemp['avg_lowest_temp'] = int(avgLowTemp['avg_lowest_temp'] / len(dayWeatherList))
        avgHighHumid['avg_highest_humid'] = int(avgHighHumid['avg_highest_humid'] / len(dayWeatherList))

        avCal = [avgHighTemp, avgLowTemp, avgHighHumid]

        return avCal
    
    
    def cal_AvgTemperatureHumidStat(self, year, month, category):
        '''
            @param year: The year for which to calculate average temperature or humidity statistics (int).
            @param month: The month for which to calculate average temperature or humidity statistics (int).
            @param category: The category of statistics to calculate, one of:
                            - 'highestTemp': Calculate the average highest temperature (str).
                            - 'meanTemp': Calculate the average mean temperature (str).
                            - 'lowestTemp': Calculate the average lowest temperature (str).
                            - 'highestHumid': Calculate the average highest humidity (str).
                            - 'lowestHumid': Calculate the average lowest humidity (str).
                            - 'meanHumid': Calculate the average mean humidity (str).
            
            @desc: This method calculates and returns the average temperature or humidity statistic
                for a given month and year based on the weather data in the associated file.
            
            @return: A dictionary containing the calculated average temperature or humidity statistic (dict).
        '''
        fileName = self.getFileName(year, month)
        dayWeatherList = self.fileHandler.readFile(fileName)        
        
        if category == 'highestTemp':
            avgHighTemp = {'avg_highest_temp': 0}
            for data in dayWeatherList:
                avgHighTemp['avg_highest_temp'] += data.Max_TemperatureC
            avgHighTemp['avg_highest_temp'] = int(avgHighTemp['avg_highest_temp'] / len(dayWeatherList))
            return avgHighTemp
        
        elif category == 'meanTemp':
            avgMeanTemp = {'avg_highest_temp': 0}
            for data in dayWeatherList:
                avgMeanTemp['avg_highest_temp'] += data.Mean_TemperatureC
            avgMeanTemp['avg_highest_temp'] = int(avgMeanTemp['avg_highest_temp'] / len(dayWeatherList))
            return avgMeanTemp
        
        elif category == 'lowestTemp':
            avgLowTemp = {'avg_lowest_temp': 0}
            for data in dayWeatherList:
                avgLowTemp['avg_lowest_temp'] += data.Min_TemperatureC
            avgLowTemp['avg_lowest_temp'] = int(avgLowTemp['avg_lowest_temp'] / len(dayWeatherList))
            return avgLowTemp
        
        elif category == 'highestHumid':
            avgHighHumid = {'avg_highest_humid': 0}
            for data in dayWeatherList:
                avgHighHumid['avg_highest_humid'] += data.Max_TemperatureC
            avgHighHumid['avg_highest_humid'] = int(avgHighHumid['avg_highest_humid'] / len(dayWeatherList))
            return avgHighHumid
            
        
        elif category == 'lowestHumid':
            avglowHumid = {'avg_highest_humid': 0}
            for data in dayWeatherList:
                avglowHumid['avg_highest_humid'] += data.Min_TemperatureC
            avglowHumid['avg_highest_humid'] = int(avglowHumid['avg_highest_humid'] / len(dayWeatherList))
            return avglowHumid
            
        
        elif category == 'meanHumid':
            avgMeanHumid = {'avg_highest_humid': 0}
            for data in dayWeatherList:
                avgMeanHumid['avg_highest_humid'] += data.Mean_TemperatureC
            avgMeanHumid['avg_highest_humid'] = int(avgMeanHumid['avg_highest_humid'] / len(dayWeatherList))
            return avgMeanHumid
            