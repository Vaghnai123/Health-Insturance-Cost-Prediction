import streamlit as st
import joblib
import pandas as pd

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="Health Insurance Predictor", page_icon="🏥", layout="centered"
)


def main():
    # 2. Modernized Header
    st.markdown(
        """
        <div style="background-color:#0e1117; padding:20px; border-radius:10px; margin-bottom:25px;">
            <h1 style="color:#00ff99; text-align:center; margin:0;">🏥 Health Insurance Cost Predictor</h1>
            <p style="color:#fafafa; text-align:center; margin-top:5px; font-size:16px;">
                Enter your details below to get an estimated insurance premium.
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Load the model (use st.cache_resource to prevent reloading on every interaction)
    @st.cache_resource
    def load_model():
        return joblib.load("model_joblib_gr")

    try:
        model = load_model()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    # 3. Grouping inputs into structured sections using Columns
    st.subheader("👤 Personal Information")
    col1, col2, col3 = st.columns(3)

    with col1:
        p1 = st.number_input("Age", min_value=18, max_value=100, value=25, step=1)
    with col2:
        s1 = st.selectbox("Sex", ("Male", "Female"))
        p2 = 1 if s1 == "Male" else 0
    with col3:
        p3 = st.number_input(
            "BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1
        )

    st.markdown("---")  # Divider for visual separation

    st.subheader("📊 Demographics & Lifestyle")
    col4, col5, col6 = st.columns(3)

    with col4:
        p4 = st.number_input(
            "Children/Dependents", min_value=0, max_value=10, value=0, step=1
        )
    with col5:
        s2 = st.selectbox("Smoker", ("Yes", "No"))
        p5 = 1 if s2 == "Yes" else 0
    with col6:
        # Improved UX: Using descriptive names instead of just numbers 1-4
        region_map = {
            "Southwest (1)": 1,
            "Southeast (2)": 2,
            "Northwest (3)": 3,
            "Northeast (4)": 4,
        }
        region_choice = st.selectbox("Region", list(region_map.keys()))
        p6 = region_map[region_choice]

    st.markdown(
        "<br>", unsafe_allow_html=True
    )  # Add a little spacing before the button

    # 4. Centered and stylized Predict Button
    _, center_col, _ = st.columns([1, 1, 1])

    with center_col:
        predict_button = st.button(
            "Calculate Premium ➔", use_container_width=True, type="primary"
        )

    if predict_button:
        # Create DataFrame with feature names
        input_data = pd.DataFrame(
            [[p1, p2, p3, p4, p5, p6]],
            columns=["age", "sex", "bmi", "children", "smoker", "region"],
        )

        # Make prediction
        prediction = model.predict(input_data)

        st.balloons()

        # 5. Professional Result Display using st.metric
        st.markdown("---")
        st.subheader("💰 Estimated Premium")
        st.metric(label="Annual Insurance Amount", value=f"₹ {prediction[0]:,.2f}")
        st.caption("Note : This is an AI-generated estimate based on historical data.")


if __name__ == "__main__":
    main()
