import streamlit as st
import requests

st.title("🚀 NASA Image Explorer")
st.write("Search NASA's image database using open API")

query = st.text_input("Enter a keyword (e.g., moon, galaxy, earth):", "moon")

if st.button("Search") and query.strip():
    url = f"https://images-api.nasa.gov/search?q={query}&media_type=image"
    res = requests.get(url).json()

    items = res.get("collection", {}).get("items", [])[:5]

    if not items:
        st.warning("No results found.")
    else:
        for item in items:
            data = item["data"][0]
            title = data.get("title", "Untitled")
            desc = data.get("description", "No description.")
            img = item["links"][0]["href"]
            st.subheader(title)
            st.image(img, use_column_width=True)
            st.caption(desc[:200] + "...")
