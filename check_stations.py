import requests
import time

# seznam stanic
stations = [
    11406, 11414, 11423, 11433, 11438, 11450, 11457, 11464, 11487,
    11502, 11509, 11518, 11519, 11520, 11538, 11546, 11567,
    11603, 11609, 11624, 11628, 11636, 11643, 11652, 11659,
    11669, 11679, 11683, 11692, 11693, 11698,
    11710, 11723, 11730, 11747, 11766, 11774, 11782, 11787, 11791
]

base_url = "http://89.221.223.46:8080/weather_api?station="

for st_id in stations:
    try:
        url = f"{base_url}{st_id}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        print(data)

    except Exception as e:
        print(f"Chyba pro stanici {st_id}: {e}")

    # malá pauza, aby se nezahltil server
    time.sleep(0.5)
