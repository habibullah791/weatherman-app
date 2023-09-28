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

