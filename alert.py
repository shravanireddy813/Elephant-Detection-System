from datetime import datetime

def generate_alert(confidence):

    print("="*50)
    print(" ALERT ")
    print("Elephant Detected")
    print(f"Confidence : {confidence:.2f}")
    print(f"Time : {datetime.now()}")
    print("="*50)

    # Future Improvements
    # Send Email
    # Send SMS
    # Activate Buzzer
    # Turn ON LED
