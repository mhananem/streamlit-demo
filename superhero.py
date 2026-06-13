import streamlit as st
import pandas as pd

# 1. Title
st.title("Superhero Name Generator")

# 2. Header
st.header("Create Your Superhero Identity")

# 3. Subheader
st.subheader("Fill in the details below")

# 4. Text
st.text("Answer a few questions and we'll build your unique superhero profile.")

# 5. Markdown
st.markdown("Your name is generated from your **favorite animal**")

# 6. Input Widgets
animal = st.text_input("Enter your favorite animal:")
st.write(f"Favorite animal: {animal}")
color = st.text_input("Enter your favorite color:")
st.write(f"Favorite color: {color}" if color else "")


# 10. Selectbox
superpower = st.selectbox(
    "Choose your superpower:",
    ["Flying", "Invisibility", "Time Travel"]
)
st.write(f"You selected: {superpower}")

# 9. Checkbox
show_motto = st.checkbox("Show my superhero motto")
if show_motto:
    mottos = {
        "Flying":            "The sky is not the limit",
        "Invisibility":      "The invisible hand that control us all",
        "Time Travel":       "Today is your next best chance",
    }
    st.write(f"Your motto is: {mottos[superpower]}")


# 8. Button
if st.button("Generate"):
    if animal and color:
        hero_name = animal[:2].upper() + color[-2:].upper()
        st.write(f"Your superhero name is: {hero_name}")
        st.write(f"Your superpower is: {superpower}")