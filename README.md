# Weather Man App API Documentation

This README file provides documentation for the APIs used in the Weather Man Flask console base application. The application utilizes data stored in files located in the `data\weatherfiles` folder.

## APIs  

### 1. Get the highest, lowest temperature and humidity

-  **Endpoint**: `/api/temperature/highest_lowest_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Highest, Lowest temperature and the humodity in that perticular year and month

  

### 2. Get the highest temperature

-  **Endpoint**: `/api/temperature/highest_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Highest temperature in that perticular year and month

  

### 3. Get the Lowest temperature

-  **Endpoint**: `/api/temperature/lowest_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Lowest temperature in that perticular year and month

  

### 4. Get the Mean temperature

-  **Endpoint**: `/api/temperature/mean_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Mean temperature in that perticular year and month

  

### 5. Get the highest Humidity

-  **Endpoint**: `/api/humidity/highest_humidity?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Highest humidity in that perticular year and month

  

### 6. Get the Lowest Humidity

-  **Endpoint**: `/api/humidity/lowest_humidity?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Lowest humidity in that perticular year and month

  

### 7. Get the Mean Humidity

-  **Endpoint**: `/api/humidity/mean_humidity?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Mean humidity in that perticular year and month

  
  

### 8. Get the Average highest, lowest temperature and humidity

-  **Endpoint**: `/api/temperature_humid/avg_highest_lowest_temperature_humidity?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Average Highest, Lowest temperature and the humodity in that perticular year and month

  

### 9. Get the Average highest temperature

-  **Endpoint**: `/api/temperature/avg_highest_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Highest temperature in that perticular year and month

  

### 10. Get the Average Lowest temperature

-  **Endpoint**: `/api/temperature/avg_lowest_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Average Lowest temperature in that perticular year and month

  

### 11. Get the Average Mean temperature

-  **Endpoint**: `/api/temperature/avg_mean_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Average Mean temperature in that perticular year and month

  

### 12. Get the Average highest Humidity

-  **Endpoint**: `/api/humidity/avg_highest_humidity?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Average Highest humidity in that perticular year and month

  

### 13. Get the Average Lowest Humidity

-  **Endpoint**: `/api/humidity/avg_lowest_humidity?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Average Lowest humidity in that perticular year and month

  

### 14. Get the Average Mean Humidity

-  **Endpoint**: `/api/humidity/avg_mean_humidity?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the Average Mean humidity in that perticular year and month

  
  

### 15. Get the Chart for highest and lowest Temperature in perticular month

-  **Endpoint**: `/api/chart/temperature/chart_highest_lowest_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the chart for the Highest, Lowest temperature in that perticular month of perticular year

  

### 16. Get Chart for highest temperature

-  **Endpoint**: `/api/chart/temperature/chart_highest_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the chart for the Highest temperature in that perticular month of perticular year

  

### 17. Get Chart for Lowest temperature

-  **Endpoint**: `/api/chart/temperature/chart_lowest_temperature?year=2006&month=6

-  **Method**: GET

-  **Description**: This API provides the chart for the Lowest temperature in that perticular month of perticular year


## Conclusion

- The Api's will call a function and that function will return the data in JSON format that will be printed to the console and for the carts that will be displayed to the console as well. These end points will be tested using **Postman**.