import streamlit as st
import pandas as pd

# Function to save data to CSV file


def save_data_to_csv(data):
    df = pd.DataFrame(
        data, columns=["Note Title", "Note Description", "Google Drive Link"])
    df.to_csv("notes.csv", index=False)

# Main function


def main():
    st.title("Digital Notes Collection")

    # Sidebar for user input
    st.sidebar.header("Submit a Note")
    note_title = st.sidebar.text_input("Note Title")
    note_description = st.sidebar.text_area("Note Description")
    google_drive_link = st.sidebar.text_input("Google Drive Link")

    if st.sidebar.button("Submit"):
        st.sidebar.success("Note submitted successfully!")
        save_data_to_csv([(note_title, note_description, google_drive_link)])

        # Display the submitted notes
        st.header("Submitted Notes")
        df = pd.read_csv("notes.csv")
        st.dataframe(df)

    # Display embedded Google Drive view
        st.header("Embedded Google Drive View")
        if df.shape[0] > 0:
            google_drive_link = df.iloc[-1]["Google Drive Link"]
            st.components.v1.iframe(google_drive_link, height=600)


if __name__ == "__main__":
    main()
