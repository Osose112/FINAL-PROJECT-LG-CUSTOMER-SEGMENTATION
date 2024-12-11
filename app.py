import pandas as pd
import gradio as gr

# Load the data file
try:
    data = pd.read_csv("data/lg_customer_data.csv")
except FileNotFoundError:
    raise RuntimeError("The file 'data/lg_customer_data.csv' was not found in the 'data' directory.")
except Exception as e:
    raise RuntimeError(f"An error occurred while loading the file: {str(e)}")

# Function to process input and return customer segment
def predict_segment(age, annual_income, total_purchases, loyalty_duration):
    # Simulate processing and returning a result
    try:
        # Example logic: Find the closest match based on some criteria
        filtered_data = data[
            (data["age"] <= age + 5) &
            (data["age"] >= age - 5) &
            (data["annual_income"] <= annual_income + 5000) &
            (data["annual_income"] >= annual_income - 5000)
        ]

        if not filtered_data.empty:
            segment = filtered_data.iloc[0]["segment_id"]
            profile = filtered_data.iloc[0]["segment_profile"]
            return f"Segment ID: {segment}", f"Profile: {profile}"
        else:
            return "No matching segment found.", ""

    except Exception as e:
        return f"An error occurred: {str(e)}", ""

# Define the Gradio interface
inputs = [
    gr.Number(label="Age"),
    gr.Number(label="Annual Income"),
    gr.Number(label="Total Purchases"),
    gr.Number(label="Loyalty Duration (in years)"),
]
outputs = [
    gr.Textbox(label="Predicted Segment"),
    gr.Textbox(label="Segment Profile"),
]

interface = gr.Interface(
    fn=predict_segment,
    inputs=inputs,
    outputs=outputs,
    title="Customer Segmentation Predictor",
    description="Predict customer segments based on input features.",
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
