import pandas as pd
import joblib
import re

def extract_features(address):
    return {
        'Length': len(address),
        'StartsWith1': address.startswith('1'),
        'StartsWith3': address.startswith('3'),
        'StartsWith0x': address.startswith('0x'),
        'StartsWithT': address.startswith('T'),
        'StartsWithL': address.startswith('L'),
        'StartsWithr': address.startswith('r'),
        'NumDigits': sum(c.isdigit() for c in address),
        'NumLetters': sum(c.isalpha() for c in address),
        'NumLowercase': sum(c.islower() for c in address),
        'NumUppercase': sum(c.isupper() for c in address)
    }

def is_valid_address(address):
    # Regular expressions for basic validation of each cryptocurrency address type
    btc_pattern = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
    eth_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
    trx_pattern = re.compile(r'^T[a-zA-Z0-9]{33}$')
    ltc_pattern = re.compile(r'^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$')
    xrp_pattern = re.compile(r'^r[0-9a-zA-Z]{24,34}$')

    return bool(btc_pattern.match(address) or 
                eth_pattern.match(address) or 
                trx_pattern.match(address) or 
                ltc_pattern.match(address) or 
                xrp_pattern.match(address))

if __name__ == "__main__":
    # Load the saved Random Forest model
    model_filename = 'crypto_address_classifier_rf_model.pkl'
    rf_model_loaded = joblib.load(model_filename)

    while True:
        # Get address input from the user
        address = input("Enter the cryptocurrency address (or type 'exit' to quit): ").strip()
        
        # Exit the loop if the user types 'exit'
        if address.lower() == 'exit':
            break
        
        # Check if the address is empty
        if not address:
            print("Error: The address cannot be empty. Please enter a valid cryptocurrency address.")
            continue

        # Validate the address
        if not is_valid_address(address):
            print("Error: The address entered is not valid. Please enter a valid cryptocurrency address.")
            continue

        # Extract features from the address
        features = extract_features(address)
        features_df = pd.DataFrame([features])

        # Predict the blockchain type
        try:
            prediction = rf_model_loaded.predict(features_df)
            print(f'The address belongs to the {prediction[0]} blockchain.')
        except Exception as e:
            print(f"Error: {str(e)}")
