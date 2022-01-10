import weather_forecast as wf
import time
import datetime
from datetime import datetime
from datetime import date

now = datetime.now()
place=input("Enter location of where you want the forecast for - ")
t=input("For when do you want the weather forecast? - ")
da=input("Which Date's weather forecast do you want? - ")
current_time = now.strftime("%H:%M:%S")
today=date.today()
wf=wf.forecast(place,t,da,forecast="daily")
print("This is the Requested Forecast")
