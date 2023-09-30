from utils.Utils import Utils
from DB.FileHandler import FileHandler


file_handler = FileHandler()
utils = Utils()


class WeatherDataControler:
    def __init__(self) -> None:
        pass

    def getTemperatureHumidityStats(self, year, month):
        data = utils.cal_HighestLowestTemperatureHumidity(year, month)
        data = utils.convertToJSON(data)

        return data

    def getHighestTemperatureStats(self, year, month):
        category = "highestTemp"
        data = utils.cal_TemperatureStat(year, month, category)
        data = utils.convertToJSON(data)

        return data

    def getLowestTemperatureStats(self, year, month):
        category = "lowestTemp"
        data = utils.cal_TemperatureStat(year, month, category)
        data = utils.convertToJSON(data)

        return data

    def getMeanTemperatureStats(self, year, month):
        category = "meanTemp"
        data = utils.cal_TemperatureStat(year, month, category)
        data = utils.convertToJSON(data)

        return data
    
    
    def getHighestHumidityStats(self, year, month):
        category = "highestHumid"
        data = utils.cal_HumidStat(year, month, category)
        data = utils.convertToJSON(data)

        return data
    
    def getLowestHumidityStats(self, year, month):
        category = "lowestHumid"
        data = utils.cal_HumidStat(year, month, category)
        data = utils.convertToJSON(data)

        return data
    
    def getMeanHumidityStats(self, year, month):
        category = "meanHumid"
        data = utils.cal_HumidStat(year, month, category)
        data = utils.convertToJSON(data)

        return data

    def getAvgTemperatureHumidityStats(self, year, month):
        data = utils.cal_AvgHighestLowestTemperatureHumidity(year, month)
        data = utils.convertToJSON(data)
        
        return data