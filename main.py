import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading the saved model
loaded_model = pickle.load(open(r'C:\Users\abhil\Downloads\Streamlit\model_pickle1','rb'))

def Churn_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Customer Stayed Back'
    else:
      return 'Customer Churned'


def main():
    
    # giving a title
    st.title('Customer Churn Prediction')
    
    # getting the input data from the user
    
    account_length = st.text_input('Number of Days Since the Customer Joined')
    voice_mail_plan = st.selectbox('Does the Customer have a voicemail plan', ('1','0'))
    customer_service_calls = st.text_input('Calls placed to Customerservice')
    international_plan = st.selectbox('Does the Customer have a International plan', ('1','0'))
    total_charge = st.text_input('Total_charge')
    Total_calls = st.text_input('Total_calls')
    
    # code for Prediction
    Predict = ''
    
    # creating a button for Prediction
    
    if st.button('Submit'):
        Predict = Churn_prediction([account_length, voice_mail_plan, customer_service_calls, international_plan, total_charge, Total_calls])

        
    st.success(Predict)
    
if __name__ == '__main__':
    main()