import requests

API_URL = "http://127.0.0.1:8000/hospital/patients/"

def get_patients():
    try:
        response = requests.get(API_URL)
        
        if response.status_code == 200:
            data = response.json() 
            patient_dict = {}

            for patient in data:
                patient_id = patient.get("id")
                patient_dict[patient_id] = {
                    "name": patient.get("name"),
                    "age": patient.get("age"),
                    "gender": patient.get("gender"),
                    "disease": patient.get("disease"),
                    "admission_date": patient.get("admission_date"),
                }

            return patient_dict
        else:
            print(f"Error: Unable to fetch data, Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

patients = get_patients()
if patients:
    print("Patient Data Dictionary:")
    print(patients)
