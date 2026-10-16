Ex 10. AI-Based Flood Risk Prediction System

# AI-Based Flood Risk Prediction System
def calculate_risk(rainfall, water_level, soil_moisture,
                   temperature, drainage):

    # Calculate weighted risk score
    risk_score = (
        rainfall * 0.30 +
        water_level * 0.30 +
        soil_moisture * 0.20 +
        temperature * 0.05 +
        drainage * 0.15
    )

    return risk_score


def predict_risk(score):

    if score >= 80:
        return "VERY HIGH RISK"
    elif score >= 60:
        return "HIGH RISK"
    elif score >= 40:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


def safety_message(risk):

    if risk == "VERY HIGH RISK":
        return "Evacuate immediately and move to a safe place."
    elif risk == "HIGH RISK":
        return "Stay alert and follow emergency instructions."
    elif risk == "MEDIUM RISK":
        return "Monitor rainfall and river water level."
    else:
        return "Normal condition. Continue monitoring."


def main():

    print("=" * 60)
    print("AI-BASED FLOOD RISK PREDICTION SYSTEM")
    print("=" * 60)

    print("\nEnter environmental parameters")
    print("(Enter values between 0 and 100)\n")

    rainfall = float(input("Enter Rainfall Level     : "))
    water_level = float(input("Enter River Water Level : "))
    soil_moisture = float(input("Enter Soil Moisture     : "))
    temperature = float(input("Enter Temperature Risk   : "))
    drainage = float(input("Enter Drainage Risk      : "))

    # Check input range
    if (rainfall < 0 or rainfall > 100 or
        water_level < 0 or water_level > 100 or
        soil_moisture < 0 or soil_moisture > 100 or
        temperature < 0 or temperature > 100 or
        drainage < 0 or drainage > 100):

        print("\nError: Enter values only between 0 and 100.")
        return

    # Calculate risk
    score = calculate_risk(
        rainfall,
        water_level,
        soil_moisture,
        temperature,
        drainage
    )

    # Predict risk level
    risk = predict_risk(score)

    # Display result
    print("\n" + "=" * 60)
    print("PREDICTION RESULT")
    print("=" * 60)

    print("Rainfall Level       :", rainfall)
    print("River Water Level    :", water_level)
    print("Soil Moisture        :", soil_moisture)
    print("Temperature Risk     :", temperature)
    print("Drainage Risk        :", drainage)

    print("\nFlood Risk Score     :", round(score, 2))
    print("Flood Risk Level     :", risk)

    print("\nSafety Advice         :", safety_message(risk))

    print("=" * 60
# Main function
if __name__ == "__main__":
    main()

Output
============================================================
        AI-BASED FLOOD RISK PREDICTION SYSTEM
============================================================

Enter environmental parameters
(Enter values between 0 and 100)

Enter Rainfall Level     : 90
Enter River Water Level : 85
Enter Soil Moisture     : 80
Enter Temperature Risk   : 60
Enter Drainage Risk      : 75

============================================================
                 PREDICTION RESULT
============================================================
Rainfall Level       : 90.0
River Water Level    : 85.0
Soil Moisture        : 80.0
Temperature Risk     : 60.0
Drainage Risk        : 75.0

Flood Risk Score     : 82.25
Flood Risk Level     : VERY HIGH RISK

Safety Advice         : Evacuate immediately and move to a safe place.
=================================================
