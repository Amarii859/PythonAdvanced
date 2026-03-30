import streamlit as st

from module7.trduy import message


def main():
    st.title("Hello World")

    st.button("Click Me")


if __name__ == "__main__":
    main()

if st.button("Click me"):
    st.write("Button cliked")

st.checkbox("Check me")

if st.checkbox("check to show some text"):
    st.write("some text")

user_input = st.text_input("enter text " , "sample text")

st.write("You entered:" , user_input)

age = st.number_input("Enter age :", min_value=0 ,  max_value=100)

st.write(f"your age is:{age}")

message = st.text_area("enter a message")

st.write(f"your message {message}")

choice = st.radio("pick one" , ["1","2" , "3"])

st.write(f"your choice is : {choice}")

if st.button("success"):
    st.success("operation wa sucsessful")

try:
    1 / 0
except Exception as e:
    st.exception(e)


