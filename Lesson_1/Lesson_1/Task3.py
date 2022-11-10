from datetime import datetime
seconds = int(input("Write count of seconds"))
day = seconds//86400
hour = (seconds%86400)//3600
minute = (seconds%3600)//50
sec = (seconds%60)%60
print(day,"day",hour,"hour",minute,"minutes",sec,"seconds")
