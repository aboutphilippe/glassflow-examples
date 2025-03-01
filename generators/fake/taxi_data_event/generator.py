"""
generate fake events
"""

import random
from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_random_coordinates(self):
        min_lat, max_lat = 45.43344, 45.495083
        min_lon, max_lon = 9.145565, 9.18951
        latitude = round(random.uniform(min_lat, max_lat), 8)
        longitude = round(random.uniform(min_lon, max_lon), 8)
        return latitude, longitude

    def generate_fake_taxi_data(self):
        user = self.fake.uuid4()
        taxi = self.fake.uuid4()
        driver = self.fake.uuid4()

        passenger_current_location = self.generate_random_coordinates()
        passenger_arrival_location = self.generate_random_coordinates()
        drivers_current_location = self.generate_random_coordinates()

        drivers_review = random.uniform(1.0, 5.0)
        booking_timestamp = self.fake.date_time_this_year()
        booking_source = random.choice(["website", "app"])
        n_passengers = random.randint(1, 4)
        estimated_fare = random.uniform(10, 50)
        estimated_arrival_time = random.randint(5, 15)
        vehicle_details = random.choice(["suv", "sedan", "hatchback", "minivan"])
        trip_duration = random.randint(10, 60)
        trip_distance = random.uniform(1, 20)
        trip_rating = random.uniform(1.0, 5.0)
        trip_id = self.fake.uuid4()

        data = {
            "user_id": str(user),
            "taxi_id": str(taxi),
            "driver_id": str(driver),
            "passenger_current_location": passenger_current_location,
            "passenger_arrival_location": passenger_arrival_location,
            "drivers_current_location": drivers_current_location,
            "drivers_review": drivers_review,
            "booking_timestamp": str(booking_timestamp),
            "booking_source": booking_source,
            "n_passengers": n_passengers,
            "estimated_fare": estimated_fare,
            "estimated_arrival_time_in_m": estimated_arrival_time,
            "vehicle_details": vehicle_details,
            "trip_duration": trip_duration,
            "trip_distance": trip_distance,
            "trip_rating": trip_rating,
            "trip_id": str(trip_id),
        }
        return data
