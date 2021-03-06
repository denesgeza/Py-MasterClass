import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print(f'The current time in {country} is {local_time}.')
print(f"UTC is {datetime.datetime.utcnow()}")

for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names)

for x in sorted(pytz.country_names):
    print(f'{x}: {pytz.country_names[x]}, {pytz.country_timezones.get(x)}')