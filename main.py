import pygeocoder

# Load the image
image = Image.open("Users/wgierer26/Desktop/IMG-8611.JPG")

# Extract the EXIF data from the image
exif_data = image._getexif()

# Get the GPS information from the EXIF data
gps_info = exif_data[34853]

# Extract the latitude and longitude from the GPS information
latitude = gps_info[2][0][0] / gps_info[2][0][1]
longitude = gps_info[4][0][0] / gps_info[4][0][1]

# Use PyGeoCoder to reverse geocode the coordinates and get the location
location = pygeocoder.Geocoder.reverse_geocode(latitude, longitude)

# Print the location
print(location)
