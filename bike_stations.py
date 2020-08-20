class BikeStations:
    bike_array = []

    def __init__(self, guid, station_no, name, is_active, available, not_available, lat, lon, last_connection):
        self.guid = guid
        self.station_no = station_no
        self.name = name
        self.is_active = is_active
        self.available = available
        self.not_available = not_available
        self.lat = lat
        self.lon = lon
        self.last_connection = last_connection

    @classmethod
    def create(cls, data_list):
        for i in range(len(data_list)):
            cls.guid = data_list[i]["guid"]
            cls.station_no = data_list[i]["istasyon_no"]
            cls.name = data_list[i]["adi"]
            cls.is_active = data_list[i]["aktif"]
            cls.available = data_list[i]["bos"]
            cls.not_available = data_list[i]["dolu"]
            cls.lat = data_list[i]["lat"]
            cls.lon = data_list[i]["lon"]
            cls.last_connection = data_list[i]["sonBaglanti"]
            bike_stations = BikeStations(cls.guid, cls.station_no, cls.name, cls.is_active, cls.available,
                                         cls.not_available, cls.lat, cls.lon, cls.last_connection)
            cls.bike_array.append(bike_stations)
