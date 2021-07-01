number_of_snowballs = int(input())
snowball_value = 0
snowball_value_final = 0
snowball_snow_final = 0
snowball_time_final = 0
snowball_quality_final = 0

for n in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow // snowball_time) ** snowball_quality

    if snowball_value > snowball_value_final:
        snowball_value_final = snowball_value
        snowball_snow_final = snowball_snow
        snowball_time_final = snowball_time
        snowball_quality_final = snowball_quality

print(f"{snowball_snow_final} : {snowball_time_final} = {snowball_value_final} ({snowball_quality_final})")