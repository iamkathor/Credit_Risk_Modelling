import streamlit as st
import pandas as pd
import pickle
import joblib
import numpy as np

st.title("Credit Risk Prediction App")
st.write("Enter Applicant Details to Predict Credit Risk")

# Load the model
try:
    model = joblib.load("extra_trees_model.pkl")
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Define all categories and their mappings
categories = {
    "Sex": ["female", "male"],
    "Housing": ["own", "rent", "free"],
    "Saving accounts": ["little", "moderate", "rich", "quite rich"],
    "Checking account": ["little", "moderate", "rich"]
}

# Manual mappings for all categorical variables
mappings = {
    "Sex": {"female": 0, "male": 1},
    "Housing": {"own": 0, "rent": 1, "free": 2},
    "Saving accounts": {"little": 0, "moderate": 1, "rich": 2, "quite rich": 3},
    "Checking account": {"little": 0, "moderate": 1, "rich": 2}
}

# Display available categories
with st.expander("📋 Available Categories"):
    st.write(f"**Sex**: {categories['Sex']} (0=female, 1=male)")
    st.write(f"**Housing**: {categories['Housing']} (0=own, 1=rent, 2=free)")
    st.write(f"**Saving accounts**: {categories['Saving accounts']} (0=little, 1=moderate, 2=rich, 3=quite rich)")
    st.write(f"**Checking account**: {categories['Checking account']} (0=little, 1=moderate, 2=rich)")

# User inputs
age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex", categories["Sex"])
job = st.selectbox("Job (0-3)", options=range(0, 4), index=1)
housing = st.selectbox("Housing", categories["Housing"])
saving_accounts = st.selectbox("Saving Accounts", categories["Saving accounts"])
checking_account = st.selectbox("Checking Account", categories["Checking account"])

credit_amount = st.number_input("Credit Amount", min_value=0, value=1000, step=100)
duration = st.number_input("Duration (in months)", min_value=1, value=12, step=1)

# Prepare data for prediction using manual mappings
try:
    # Convert to strings and strip whitespace
    sex_val = str(sex).strip()
    housing_val = str(housing).strip()
    saving_val = str(saving_accounts).strip()
    checking_val = str(checking_account).strip()
    
    # Encode all categorical variables using manual mappings
    sex_encoded = mappings["Sex"][sex_val]
    housing_encoded = mappings["Housing"][housing_val]
    saving_encoded = mappings["Saving accounts"][saving_val]
    checking_encoded = mappings["Checking account"][checking_val]
    
    # Debug information
    st.write("### Debug: Encoding Values")
    st.write(f"Sex: '{sex_val}' → {sex_encoded}")
    st.write(f"Housing: '{housing_val}' → {housing_encoded}")
    st.write(f"Saving accounts: '{saving_val}' → {saving_encoded}")
    st.write(f"Checking account: '{checking_val}' → {checking_encoded}")
    
    input_df = pd.DataFrame({
        "Age": [age],
        "Sex": [sex_encoded],
        "Job": [job],
        "Housing": [housing_encoded],
        "Saving accounts": [saving_encoded],
        "Checking account": [checking_encoded],
        "Credit amount": [credit_amount],
        "Duration": [duration]
    })
    
    st.success("✅ Data prepared successfully!")
    
except KeyError as e:
    st.error(f"Error: Value not found in mapping - {e}")
    st.write("### Debug Information:")
    st.write(f"Sex value: '{sex}' (type: {type(sex)})")
    st.write(f"Housing value: '{housing}' (type: {type(housing)})")
    st.write(f"Saving accounts value: '{saving_accounts}' (type: {type(saving_accounts)})")
    st.write(f"Checking account value: '{checking_account}' (type: {type(checking_account)})")
    st.write(f"Available mappings: {mappings}")
    st.stop()
    
except Exception as e:
    st.error(f"Error encoding inputs: {e}")
    st.write("### Debug Information:")
    st.write(f"Sex value: '{sex}' (type: {type(sex)})")
    st.write(f"Housing value: '{housing}' (type: {type(housing)})")
    st.write(f"Saving accounts value: '{saving_accounts}' (type: {type(saving_accounts)})")
    st.write(f"Checking account value: '{checking_account}' (type: {type(checking_account)})")
    st.stop()

# Prediction button
if st.button("Predict Risk"):
    try:
        pred = model.predict(input_df)[0]
        
        if pred == 1:
            st.success("✅ The predicted credit risk is: **GOOD**")
            st.balloons()
        else:
            st.error("❌ The predicted credit risk is: **BAD**")
            
    except Exception as e:
        st.error(f"Prediction error: {e}")