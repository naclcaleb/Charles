from weather import Weather, Unit
import Driver

class WeatherMap(Driver.Driver):
    device_name = "weathermap"
    def get(self, req):
        weather = Weather(unit=Unit.FAHRENHEIT)

        lookup = weather.lookup(2464467)
        condition = lookup.condition
        if req=="temp":
            return condition.temp
        elif req == "skies":
            return condition.text
        elif req == "all":
            return str(condition.temp) + u'\u00B0' + ", " + condition.text
w = WeatherMap()
print(w.get("all"))
        
