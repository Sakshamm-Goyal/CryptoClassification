# Crypto Address Classifier

This repository contains a Python script to classify cryptocurrency addresses into different blockchains. The script uses a pre-trained Random Forest model to predict the blockchain type based on various address features.

## Features

- Extracts features from a cryptocurrency address.
- Validates if the input address is a valid cryptocurrency address.
- Predicts the blockchain type (e.g., Bitcoin, Ethereum, Tron, Litecoin, Ripple) using a pre-trained Random Forest model.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/crypto-address-classifier.git
    cd crypto-address-classifier
    ```

2. **Create and activate a virtual environment (optional but recommended)**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure you have the pre-trained model file**:
    - Place the `crypto_address_classifier_rf_model.pkl` file in the root directory of the project.

## Usage

To classify a cryptocurrency address, run the script and input the address when prompted:

```bash
python train_and_save_model.py
```

```bash
python classify_address.py
```

### Example

```bash
Enter the cryptocurrency address (or type 'exit' to quit): 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
The address belongs to the Bitcoin blockchain.
```


https://github.com/Sakshamm-Goyal/CryptoClassification/assets/144555727/81787b89-4f1b-4559-a509-288e4e0813b6


## Script Details

### `extract_features(address)`

Extracts features from a given cryptocurrency address.

- `Length`: Length of the address.
- `StartsWith1`: Boolean indicating if the address starts with '1'.
- `StartsWith3`: Boolean indicating if the address starts with '3'.
- `StartsWith0x`: Boolean indicating if the address starts with '0x'.
- `StartsWithT`: Boolean indicating if the address starts with 'T'.
- `StartsWithL`: Boolean indicating if the address starts with 'L'.
- `StartsWithr`: Boolean indicating if the address starts with 'r'.
- `NumDigits`: Number of digits in the address.
- `NumLetters`: Number of letters in the address.
- `NumLowercase`: Number of lowercase letters in the address.
- `NumUppercase`: Number of uppercase letters in the address.

### `is_valid_address(address)`

Validates if the input address is a valid cryptocurrency address using regular expressions.

- `btc_pattern`: Regex for Bitcoin addresses.
- `eth_pattern`: Regex for Ethereum addresses.
- `trx_pattern`: Regex for Tron addresses.
- `ltc_pattern`: Regex for Litecoin addresses.
- `xrp_pattern`: Regex for Ripple addresses.

### Main Script

1. Loads the saved Random Forest model from `crypto_address_classifier_rf_model.pkl`.
2. Prompts the user to input a cryptocurrency address.
3. Validates the input address.
4. Extracts features from the address.
5. Predicts the blockchain type using the loaded model.
6. Prints the prediction result.

