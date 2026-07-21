# Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

# Convert to meters and centimeters
meters = feet * 0.3048
centimeters = inches * 2.54

print("Distance in meters =", meters)
print("Distance in centimeters =", centimeters)