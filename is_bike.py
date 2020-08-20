from bike_stations import BikeStations
import http.client
import xlsxwriter
import json

# Ibb GET Request
conn = http.client.HTTPSConnection("api.ibb.gov.tr")
payload = ''
headers = {'Cookie': 'cookiesession1=678A3E0FPQRSTVWXYZABCDEFGHIJA4C8'}
conn.request("GET", "/ispark-bike/GetAllStationStatus", payload, headers)
response = conn.getresponse().read()
parsed_as_data_list = json.loads(response)["dataList"]
BikeStations.create(parsed_as_data_list)

# Excel sheet writer
bike_locations = xlsxwriter.Workbook("BikeLocations.xlsx")
worksheet = bike_locations.add_worksheet("İstanbul")
# Page format section
cell_format = bike_locations.add_format({'bold': True, 'font_color': 'black'})
cell_format.set_align("center")
cell_format.set_bg_color("yellow")
worksheet.set_column("B:D", 30)
# Header section
worksheet.write("A1", "#", cell_format)
worksheet.write("B1", "Name", cell_format)
worksheet.write("C1", "Latitude", cell_format)
worksheet.write("D1", "Longitude", cell_format)
# Data section
for i in range(len(BikeStations.bike_array)):
    worksheet.write("A{}".format(i + 2), i+1)
    worksheet.write("B{}".format(i + 2), BikeStations.bike_array[i].name)
    worksheet.write("C{}".format(i + 2), BikeStations.bike_array[i].lat)
    worksheet.write("D{}".format(i + 2), BikeStations.bike_array[i].lon)

# Don't forget to close the Excel sheet
bike_locations.close()
