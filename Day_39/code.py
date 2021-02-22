import requests
import datetime as dt

APP_ID = "8-"
API_KEY = "a8-"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_params = {
     "query": input("Tell me which exercise you did: "),
     "gender": "male",
     "weight_kg": 77.0,
     "height_cm": 170.8,
     "age": 24
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
# print(response.text)
data = response.json()
print(data)

now = dt.datetime.now()

date = now.strftime("%d/%m/%G")
time = now.strftime("%X")
exercise = data['exercises'][0]['name']
duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']

sheety_endpoint = "https://api.sheety.co/aa-/workoutTracking/workouts"

sheety_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories,
    }
}

headers = {
    "Authorization": "Bearer Thisistokenforsheetyworkoutproject;)",
    "Content-Type": "application/json"
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers)
print(sheety_response.text)

