import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
dataset_path = 'large_crypto_addresses_dataset.csv'  # Ensure the correct path
df_large = pd.read_csv(dataset_path)

# Extract features
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

features_large = df_large['Address'].apply(extract_features)
features_large_df = pd.DataFrame(features_large.tolist())
df_large = pd.concat([df_large, features_large_df], axis=1)

X_large = df_large.drop(columns=['Address', 'Blockchain'])
y_large = df_large['Blockchain']

X_train_large, X_test_large, y_train_large, y_test_large = train_test_split(X_large, y_large, test_size=0.2, random_state=42)

# Train the Random Forest model
rf_model_large = RandomForestClassifier()
rf_model_large.fit(X_train_large, y_train_large)

# Save the model
model_filename = 'crypto_address_classifier_rf_model.pkl'
joblib.dump(rf_model_large, model_filename)

print(f'Model saved as {model_filename}')
