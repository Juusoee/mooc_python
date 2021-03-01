farenheit = int(input("Anna lämpötila (F): "))
 
celcius = (farenheit - 32)/1.8000
 
if celcius >= 0:
    print(f"{farenheit} fahrenheit-astetta on {celcius} celsius-astetta")
if celcius < 0:
    print(f"{farenheit} fahrenheit-astetta on {celcius} celsius-astetta")
    print("Paleltaa!")