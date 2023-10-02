from controller import WeatherDataController
from flask import Blueprint, request, jsonify

# Create a Blueprint object
weatherManApp = Blueprint('weatherManApp', __name__)



@weatherManApp.route('temperature/highest_lowest_temperature')
def getTemperatureHumidityStats():
    '''
    Get temperature and humidity stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing temperature and humidity statistics.
    '''
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getTemperatureHumidityStats(year, month)
    
    return data




@weatherManApp.route('temperature/highest_temperature')
def getHighestTemperatureStats():
    '''
        Get Highest, temperature stats for a specific month and year.

            @params:
                - year (int): The year for which to retrieve statistics.
                - month (int): The month for which to retrieve statistics.

            @Returns:
                JSON data containing temperature and humidity statistics.
'''
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getHighestTemperatureStats(year, month)
    
    return data


@weatherManApp.route('temperature/lowest_temperature')
def getLowestTemperatureStats():
    '''
        Get Lowest temperature stats for a specific month and year.

            @params:
                - year (int): The year for which to retrieve statistics.
                - month (int): The month for which to retrieve statistics.

            @Returns:
                JSON data containing temperature and humidity statistics.
'''
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getLowestTemperatureStats(year, month)
    
    return data


@weatherManApp.route('temperature/mean_temperature')
def getMeanTemperatureStats():
    '''
        Get Mean temperature stats for a specific month and year.

            @params:
                - year (int): The year for which to retrieve statistics.
                - month (int): The month for which to retrieve statistics.

            @Returns:
                JSON data containing temperature and humidity statistics.
'''
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getMeanTemperatureStats(year, month)
    
    return data

@weatherManApp.route('humidity/highest_humidity')
def getHighestHumidityStats():
    '''
    Get Highest stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing humidity statistics.
    '''
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getHighestHumidityStats(year, month)
    
    return data


@weatherManApp.route('humidity/lowest_humidity')
def getLowestHumidityStats():
    '''
        Get Highest, Lowest Humidity stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing humidity statistics.
    '''
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getLowestHumidityStats(year, month)
    
    return data


@weatherManApp.route('humidity/mean_humidity')
def getMeanHumidityStats():
    '''
        Get Mean Humidity stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing humidity statistics.
    '''
    
    weatherController = WeatherDataController.WeatherDataControler()
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getMeanHumidityStats(year, month)
    
    return data




@weatherManApp.route('temperature_humid/avg_highest_lowest_temperature_humidity')
def getAvgTemperatureHumidityStats():
    '''
        Get Average of Highest, Lowest temperature and Humidity stats for a specific month and year.

            @params:
                - year (int): The year for which to retrieve statistics.
                - month (int): The month for which to retrieve statistics.

            @Returns:
                JSON data containing temperature and humidity statistics.
    '''

    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgTemperatureHumidityStats(year, month)
    
    return data



@weatherManApp.route('temperature/avg_highest_temperature')
def getAvgHighestTemperatureStats():
    '''
    Get Average Highest Temperature stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing Temperature humidity statistics.
    '''
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgHighestTemperatureStats(year, month)
    
    return data

@weatherManApp.route('temperature/avg_mean_temperature')
def getAvgMeanTemperatureStats():
    '''
    Get Average Mean Temperature stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing Temperature humidity statistics.
    '''
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgMeanTemperatureStats(year, month)
    
    return data


@weatherManApp.route('temperature/avg_lowest_temperature')
def getAvgLowestTemperatureStats():
    '''
    Get Average Lowest Temperature stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing Temperature humidity statistics.
    '''
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgLowestTemperatureStats(year, month)
    
    return data


@weatherManApp.route('humidity/avg_highest_humidity')
def getAvgHighestHumidityStats():
    '''
    Get Average Highest Humidity stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing Humidity humidity statistics.
    '''
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgHighestHumidityStats(year, month)
    
    return data


@weatherManApp.route('humidity/avg_lowest_humidity')
def getAvgLowestHumidityStats():
    '''
    Get Average Lowest Humidity stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing Humidity humidity statistics.
    '''
    
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgLowestHumidityStats(year, month)
    
    return data


@weatherManApp.route('humidity/avg_mean_humidity')
def getAvgMeanHumidityStats():
    '''
    Get Average Mean Humidity stats for a specific month and year.

        @params:
            - year (int): The year for which to retrieve statistics.
            - month (int): The month for which to retrieve statistics.

        @Returns:
            JSON data containing Humidity humidity statistics.
    '''
    
    weatherController = WeatherDataController.WeatherDataControler()
    
    year = request.args.get('year')
    month = request.args.get('month')
    
    data = weatherController.getAvgMeanHumidityStats(year, month)
    
    return data

