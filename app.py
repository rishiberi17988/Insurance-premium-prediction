import streamlit as st
from src.pipeline.prediction_pipeline import PredictPipeline, CustomData

# Define the main function to run the Streamlit app
def main():
    st.title("Diamond Price Prediction")

    # Sidebar inputs
    st.sidebar.header("Input Features")
    carat = st.sidebar.number_input("Carat", min_value=0.2, max_value=5.01, step=0.01, value=0.5)
    depth = st.sidebar.number_input("Depth", min_value=43, max_value=79, step=1, value=60)
    table = st.sidebar.number_input("Table", min_value=43, max_value=95, step=1, value=56)
    x = st.sidebar.number_input("X", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    y = st.sidebar.number_input("Y", min_value=0.0, max_value=60.0, step=0.1, value=3.0)
    z = st.sidebar.number_input("Z", min_value=0.0, max_value=32.0, step=0.1, value=2.0)
    cut = st.sidebar.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"], index=4)
    color = st.sidebar.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"], index=3)
    clarity = st.sidebar.selectbox("Clarity", ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"], index=4)

    # Button to trigger prediction
    if st.sidebar.button("Predict"):
        data = CustomData(carat=carat, depth=depth, table=table, x=x, y=y, z=z, cut=cut, color=color, clarity=clarity)
        final_data = data.get_data_as_dataframe()

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)

        result = round(pred[0], 2)

        # Display result
        st.success(f"Predicted Price:${result}")

# Run the app
if __name__ == "__main__":
    main()
