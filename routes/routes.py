from controller import WeatherDataController
from flask import Blueprint, request, jsonify

# Create a Blueprint object
weatherManApp = Blueprint('weatherManApp', __name__)



@weatherManApp.route('temperature/highest_lowest_temperature')
def getTemperatureHumidityStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getTemperatureHumidityStats(year, month)
    
    return data


@weatherManApp.route('temperature/highest_temperature')
def getHighestTemperatureStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getHighestTemperatureStats(year, month)
    
    return data



@weatherManApp.route('temperature/lowest_temperature')
def getLowestTemperatureStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getLowestTemperatureStats(year, month)
    
    return data


@weatherManApp.route('temperature/mean_temperature')
def getMeanTemperatureStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getMeanTemperatureStats(year, month)
    
    return data

@weatherManApp.route('humidity/highest_humidity')
def getHighestHumidityStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getHighestHumidityStats(year, month)
    
    return data


@weatherManApp.route('humidity/lowest_humidity')
def getLowestHumidityStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getLowestHumidityStats(year, month)
    
    return data


@weatherManApp.route('humidity/mean_humidity')
def getMeanHumidityStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getMeanHumidityStats(year, month)
    
    return data



@weatherManApp.route('temperature_humid/avg_highest_lowest_temperature_humidity')
def getAvgTemperatureHumidityStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgTemperatureHumidityStats(year, month)
    
    return data

@weatherManApp.route('temperature/avg_highest_temperature')
def getAvgHighestTemperatureStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgHighestTemperatureStats(year, month)
    
    return data

@weatherManApp.route('temperature/avg_mean_temperature')
def getAvgMeanTemperatureStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgMeanTemperatureStats(year, month)
    
    return data


@weatherManApp.route('temperature/avg_lowest_temperature')
def getAvgLowestTemperatureStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgLowestTemperatureStats(year, month)
    
    return data


@weatherManApp.route('humidity/avg_highest_humidity')
def getAvgHighestHumidityStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgHighestHumidityStats(year, month)
    
    return data


@weatherManApp.route('humidity/avg_lowest_humidity')
def getAvgLowestHumidityStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgLowestHumidityStats(year, month)
    
    return data


@weatherManApp.route('humidity/avg_mean_humidity')
def getAvgMeanHumidityStats():
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgMeanHumidityStats(year, month)
    
    return data

