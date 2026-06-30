import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Faker object for Indian names and cities
fake = Faker("en_IN")

# Reproducible random data
random.seed(42)

# Number of users
NUM_USERS = 500

# Empty list to store user records
users_data = []

for user_id in range(1, NUM_USERS + 1):

    users_data.append({
        "user_id": user_id,
        "full_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 60),
        "city": fake.city(),
        "height_cm": random.randint(150, 190),
        "weight_kg": round(random.uniform(50, 100), 1),
        "fitness_goal": random.choice([
            "Weight Loss",
            "Muscle Gain",
            "Maintain Fitness"
        ]),
        "join_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    })

# Create DataFrame
users_df = pd.DataFrame(users_data)

# Save CSV
users_df.to_csv(
    "datasets/raw/users.csv",
    index=False
)

print("users.csv generated successfully")
print(users_df.head())



# -----------------------------
# Daily Steps Configuration
# -----------------------------

NUM_DAYS = 90

steps_data = []

step_id = 1

for user_id in range(1, NUM_USERS + 1):

    for day in range(NUM_DAYS):

        activity_date = datetime.today() - timedelta(days=day)

        # 85% chance user is active on a given day
        if random.random() < 0.85:

            steps = random.randint(1000, 20000)

            distance_km = round(steps * 0.0008, 2)

            calories_burned = round(steps * 0.04, 2)

            steps_data.append({
                "step_id": step_id,
                "user_id": user_id,
                "activity_date": activity_date.strftime("%Y-%m-%d"),
                "steps": steps,
                "distance_km": distance_km,
                "calories_burned": calories_burned
            })

            step_id += 1

steps_df = pd.DataFrame(steps_data)

steps_df.to_csv(
    "datasets/raw/daily_steps.csv",
    index=False
)

print("daily_steps.csv generated successfully")
print(steps_df.head())


# ------------------------------------
# Workout Dataset
# ------------------------------------

workout_data = []

workout_id = 1

workout_types = [
    "Running",
    "Walking",
    "Cycling",
    "Gym",
    "Yoga",
    "HIIT"
]

for user_id in range(1, NUM_USERS + 1):

    for day in range(NUM_DAYS):

        # Only 40% chance that user performs workout
        if random.random() < 0.40:

            workout_date = datetime.today() - timedelta(days=day)

            workout = random.choice(workout_types)

            duration = random.randint(20, 90)

            calories = duration * random.randint(6, 12)

            workout_data.append({

                "workout_id": workout_id,

                "user_id": user_id,

                "workout_date": workout_date.strftime("%Y-%m-%d"),

                "workout_type": workout,

                "duration_minutes": duration,

                "calories_burned": calories

            })

            workout_id += 1

workout_df = pd.DataFrame(workout_data)

workout_df.to_csv(
    "datasets/raw/workouts.csv",
    index=False
)

print("workouts.csv generated successfully")
print(workout_df.head())



# ------------------------------------
# Heart Rate Dataset
# ------------------------------------

heart_rate_data = []
heart_rate_id = 1

for user_id in range(1, NUM_USERS + 1):

    for day in range(NUM_DAYS):

        if random.random() < 0.90:

            record_date = (datetime.today() - timedelta(days=day)).strftime("%Y-%m-%d")

            avg_hr = random.randint(65, 100)
            max_hr = avg_hr + random.randint(20, 60)
            resting_hr = random.randint(55, 80)

            # Intentional dirty data
            if random.random() < 0.01:
                avg_hr = -20

            if random.random() < 0.01:
                avg_hr = None

            heart_rate_data.append({
                "heart_rate_id": heart_rate_id,
                "user_id": user_id,
                "record_date": record_date,
                "avg_heart_rate": avg_hr,
                "max_heart_rate": max_hr,
                "resting_heart_rate": resting_hr
            })

            heart_rate_id += 1


heart_rate_df = pd.DataFrame(heart_rate_data)

heart_rate_df.to_csv(
    "datasets/raw/heart_rate.csv",
    index=False
)

print("heart_rate.csv generated successfully")
print(heart_rate_df.head())




# ------------------------------------
# Diet Dataset
# ------------------------------------

diet_data = []
diet_id = 1

meal_types = [
    "Breakfast",
    "Lunch",
    "Dinner",
    "Snack"
]

for user_id in range(1, NUM_USERS + 1):

    for day in range(NUM_DAYS):

        if random.random() < 0.95:

            meal_date = (datetime.today() - timedelta(days=day)).strftime("%Y-%m-%d")

            meal = random.choice(meal_types)

            calories = random.randint(250, 900)

            protein = random.randint(10, 60)

            carbs = random.randint(20, 120)

            fat = random.randint(5, 35)

            if random.random() < 0.01:
                calories = None

            diet_data.append({

                "diet_id": diet_id,

                "user_id": user_id,

                "meal_date": meal_date,

                "meal_type": meal,

                "calories_intake": calories,

                "protein_g": protein,

                "carbs_g": carbs,

                "fat_g": fat

            })

            diet_id += 1


diet_df = pd.DataFrame(diet_data)

diet_df.to_csv(
    "datasets/raw/diet_logs.csv",
    index=False
)

print("diet_logs.csv generated successfully")
print(diet_df.head())



# ------------------------------------
# Sleep Dataset
# ------------------------------------

sleep_data = []
sleep_id = 1

for user_id in range(1, NUM_USERS + 1):

    for day in range(NUM_DAYS):

        if random.random() < 0.95:

            sleep_date = (datetime.today() - timedelta(days=day)).strftime("%Y-%m-%d")

            sleep_hours = round(random.uniform(4.5, 9.5), 1)

            if sleep_hours < 6:
                quality = "Poor"
            elif sleep_hours < 7:
                quality = "Average"
            elif sleep_hours < 8:
                quality = "Good"
            else:
                quality = "Excellent"

            sleep_data.append({

                "sleep_id": sleep_id,

                "user_id": user_id,

                "sleep_date": sleep_date,

                "sleep_hours": sleep_hours,

                "sleep_quality": quality

            })

            sleep_id += 1

sleep_df = pd.DataFrame(sleep_data)

sleep_df.to_csv(
    "datasets/raw/sleep_logs.csv",
    index=False
)

print("sleep_logs.csv generated successfully")
print(sleep_df.head())

