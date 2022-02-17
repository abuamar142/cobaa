import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = phonenumbers.parse(input("Masukkan nomor: (example : +62....) -> "))

# this will print the country name
print(f"Negara : {geocoder.description_for_number(phone_number, 'en')}")

# this will print the service provider
print(f"Provider : {carrier.name_for_number(phone_number, 'en')}")

# this will print the timezone
print(f"Lokasi : {timezone.time_zones_for_geographical_number(phone_number)}") 