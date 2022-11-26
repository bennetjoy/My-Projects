import phonenumbers
from phonenumbers import geocoder

phno = input("Enter Phone number:")
phnoc = "+" + phno
print(phnoc)
chno = phonenumbers.parse(phnoc,"CH")
print(geocoder.description_for_number(chno,"en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(phnoc,"RO")
print(carrier.name_for_number(service_nmber, "en"))
