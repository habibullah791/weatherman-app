import os
import calendar
import json

from DB.FileHandler import FileHandler
from model.DayWeather import DayWeatherData

fileHandler = FileHandler()


class Utils:
    def __init__(self) -> None:
        pass

    def getFileName(self, year, month):
        directory = "data/weatherfiles"
        month = int(month)
        year = int(year)

        # Triming the month number to a three-letter month abbreviation
        month_abbr = calendar.month_abbr[month][:3]

        # Generate a pattern for the filename based on the year and month abbreviation
        fileName = f"Murree_weather_{year}_{month_abbr}.txt"

        # Concatenate the directory path and filename
        fullPath = os.path.join(directory, fileName)

        return fullPath

    # conver it to json
    def convertToJSON(self, weatherDataList):
        weatherDataListJSON = json.dumps(weatherDataList, indent=2)
        return weatherDataListJSON

    # cal high, lowest temp
    def cal_HighestLowestTemperatureHumidity(self, year, month):
        fileName = self.getFileName(year, month)
        dayWeatherList = fileHandler.readFile(fileName)

        highTemp = {"highest_temp": 0, "date": ""}
        lowTemp = {"lowest_temp": 1000, "date": ""}
        highHumid = {"highest_humid": 0, "date": ""}

        for dayWeather in dayWeatherList:
            maxTemp = dayWeather.Max_TemperatureC
            minTemp = dayWeather.Min_TemperatureC
            maxHumid = dayWeather.Max_Humidity
            date = dayWeather.PKT

            if maxTemp > highTemp["highest_temp"]:
                highTemp["highest_temp"] = maxTemp
                highTemp["date"] = date

            if minTemp < lowTemp["lowest_temp"]:
                lowTemp["lowest_temp"] = minTemp
                highTemp["date"] = date

            if maxHumid > highHumid["highest_humid"]:
                highHumid["highest_humid"] = maxHumid
                highTemp["date"] = date

        calculation = [highTemp, lowTemp, highHumid]

        return calculation

    # temp stat
    def cal_TemperatureStat(self, year, month, category):
        fileName = self.getFileName(year, month)
        dayWeatherList = fileHandler.readFile(fileName)

        if category == "highestTemp":
            highTemp = {"highest_temp": 0, "date": ""}

            for dayWeather in dayWeatherList:
                maxTemp = dayWeather.Max_TemperatureC
                date = dayWeather.PKT

                if maxTemp > highTemp["highest_temp"]:
                    highTemp["highest_temp"] = maxTemp
                    highTemp["date"] = date
            return highTemp

        elif category == "lowestTemp":
            lowTemp = {"lowest_temp": 1000, "date": ""}

            for dayWeather in dayWeatherList:
                maxTemp = dayWeather.Max_TemperatureC
                date = dayWeather.PKT

                if maxTemp < lowTemp["lowest_temp"]:
                    lowTemp["lowest_temp"] = maxTemp
                    lowTemp["date"] = date
            return lowTemp

        elif category == "meanTemp":
            meanTempt = {"mean_temp": 0, "date": ""}

            for dayWeather in dayWeatherList:
                meanTemp = dayWeather.Mean_TemperatureC
                date = dayWeather.PKT

                if meanTemp > meanTempt["mean_temp"]:
                    meanTempt["mean_temp"] = meanTemp
                    meanTempt["date"] = date
            return meanTempt

    # temp stat
    def cal_HumidStat(self, year, month, category):
        fileName = self.getFileName(year, month)
        dayWeatherList = fileHandler.readFile(fileName)

        if category == "highestHumid":
            highHumid = {"highest_humid": 0, "date": ""}

            for dayWeather in dayWeatherList:
                maxTemp = dayWeather.Max_Humidity
                date = dayWeather.PKT

                if maxTemp > highHumid["highest_humid"]:
                    highHumid["highest_humid"] = maxTemp
                    highHumid["date"] = date
            return highHumid

        elif category == "lowestHumid":
            lowHumid = {"lowest_humid": 1000, "date": ""}

            for dayWeather in dayWeatherList:
                maxTemp = dayWeather.Min_Humidity
                date = dayWeather.PKT

                if maxTemp < lowHumid["lowest_humid"]:
                    lowHumid["lowest_humid"] = maxTemp
                    lowHumid["date"] = date
            return lowHumid

        elif category == "meanHumid":
            meanHumid = {"mean_humid": 0, "date": ""}

            for dayWeather in dayWeatherList:
                meanTemp = dayWeather.Mean_Humidity
                date = dayWeather.PKT

                if meanTemp > meanHumid["mean_humid"]:
                    meanHumid["mean_humid"] = meanTemp
                    meanHumid["date"] = date
            return meanHumid

    def cal_AvgHighestLowestTemperatureHumidity(self, year, month):
        fileName = self.getFileName(year, month)
        dayWeatherList = fileHandler.readFile(fileName)

        avgHighTemp = {"avg_highest_temp": 0}
        avgLowTemp = {"avg_lowest_temp": 0}
        avgHighHumid = {"avg_highest_humid": 0}

        for data in dayWeatherList:
            avgHighTemp["avg_highest_temp"] += data.Max_TemperatureC
            avgLowTemp["avg_lowest_temp"] += data.Min_TemperatureC
            avgHighHumid["avg_highest_humid"] += data.Mean_TemperatureC

        avgHighTemp["avg_highest_temp"] = int(avgHighTemp["avg_highest_temp"] / len(dayWeatherList))
        avgLowTemp["avg_lowest_temp"] = int(avgLowTemp["avg_lowest_temp"] / len(dayWeatherList))
        avgHighHumid["avg_highest_humid"] = int(avgHighHumid["avg_highest_humid"] / len(dayWeatherList))

        avCal = [avgHighTemp, avgLowTemp, avgHighHumid]

        return avCal
    
    
    def cal_AvgTemperatureHumidStat(self, year, month, category):
        fileName = self.getFileName(year, month)
        dayWeatherList = fileHandler.readFile(fileName)        
        
        if category == 'highestTemp':
            avgHighTemp = {"avg_highest_temp": 0}
            for data in dayWeatherList:
                avgHighTemp["avg_highest_temp"] += data.Max_TemperatureC
            avgHighTemp["avg_highest_temp"] = int(avgHighTemp["avg_highest_temp"] / len(dayWeatherList))
            return avgHighTemp
        
        elif category == 'meanTemp':
            avgMeanTemp = {"avg_highest_temp": 0}
            for data in dayWeatherList:
                avgMeanTemp["avg_highest_temp"] += data.Mean_TemperatureC
            avgMeanTemp["avg_highest_temp"] = int(avgMeanTemp["avg_highest_temp"] / len(dayWeatherList))
            return avgMeanTemp
        
        elif category == 'lowestTemp':
            avgLowTemp = {"avg_lowest_temp": 0}
            for data in dayWeatherList:
                avgLowTemp["avg_lowest_temp"] += data.Min_TemperatureC
            avgLowTemp["avg_lowest_temp"] = int(avgLowTemp["avg_lowest_temp"] / len(dayWeatherList))
            return avgLowTemp
        
        elif category == 'highestHumid':
            avgHighHumid = {"avg_highest_humid": 0}
            for data in dayWeatherList:
                avgHighHumid["avg_highest_humid"] += data.Max_TemperatureC
            avgHighHumid["avg_highest_humid"] = int(avgHighHumid["avg_highest_humid"] / len(dayWeatherList))
            return avgHighHumid
            
        
        elif category == 'lowestHumid':
            avglowHumid = {"avg_highest_humid": 0}
            for data in dayWeatherList:
                avglowHumid["avg_highest_humid"] += data.Min_TemperatureC
            avglowHumid["avg_highest_humid"] = int(avglowHumid["avg_highest_humid"] / len(dayWeatherList))
            return avglowHumid
            
        
        elif category == 'meanHumid':
            avgMeanHumid = {"avg_highest_humid": 0}
            for data in dayWeatherList:
                avgMeanHumid["avg_highest_humid"] += data.Mean_TemperatureC
            avgMeanHumid["avg_highest_humid"] = int(avgMeanHumid["avg_highest_humid"] / len(dayWeatherList))
            return avgMeanHumid
            