"""
For modifying and reclassifying temperature data.

Help for temp_functions operations:
    fahr_to_celsisus converts temperature data from Fahrenheit into Celsius
    temp_classifier categorizes temperature in Celsius into established integer classes
"""


def fahr_to_celsius(temp_fahrenheit):
    """
    Function for converting temperature in degrees Fahrenheit to degrees Celsius.

    Parameters
    ----------
    temp_fahrenheit: <numerical>
        Temperature in Fahrenheit (°F)
    converted_temp: <str>
        Temperature in Celsius (°C)
    
    Returns
    -------
    <float>
        Converted temperature in Celsius (°C)
    """
    
    #convert the Fahrenheit value (input) using assigned variable with temperature conversion equation 
    converted_temp = (temp_fahrenheit-32)/1.8
    #return the result
    return converted_temp


def temp_classifier(temp_celsius):
    """
    Function for reclassifying temperature in degrees Celsius 
        into integer values based on set classification criteria. 
    
    Parameters
    ----------
    temp_celsius: <numerical>
        Temperature in Celsius (°C)
    class_x: <int>
        Integer values based on set criteria, where x is from 0 to 4
    
    Returns
    -------
    <int>
        Integer return values from 0 to 4 based on classsification criteria.
    """
    
    class_0 = 0 #class for temperature below 600°C
    class_1 = 1 #class for temperature between 600°C to 800°C
    class_2 = 2 #class for temperature between 800°C to 1000°C
    class_3 = 3 #class for temperature between 1000°C to 1200°C
    class_4 = 4 #class for temperature greater than 1200°C
    
    #if temperature condition is satisfied, return result as appropriate class
    if (temp_celsius < 600):
        return class_0
    elif (temp_celsius >= 600) and (temp_celsius < 800):
        return class_1
    elif (temp_celsius >= 800) and (temp_celsius < 1000):
        return class_2
    elif (temp_celsius >= 1000) and (temp_celsius < 1200):
        return class_3
    elif (temp_celsius >= 1200):
        return class_4