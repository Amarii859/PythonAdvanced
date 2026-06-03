import streamlit as st

st.set_page_config(page_title="Library App", page_icon="📚")

st.title("📚 Library App - Advanced")

# ---------------- SESSION ----------------
if "books" not in st.session_state:
    st.session_state.books = []

# ---------------- SIDEBAR ----------------
st.sidebar.header("📊 Statistika")

total = len(st.session_state.books)
st.sidebar.write(f"Total libra: {total}")

# ---------------- SHTO LIBËR ----------------
st.subheader("➕ Shto libër")

title = st.text_input("Titulli")
author = st.text_input("Autori")

if st.button("Shto"):
    if title and author:
        st.session_state.books.append({
            "title": title,
            "author": author
        })
        st.success("Libri u shtua!")
    else:
        st.error("Shkruaj të gjitha fushat!")

# ---------------- SEARCH ----------------
st.subheader("🔍 Kërko libër")

search = st.text_input("Shkruaj titullin ose autorin")

filtered_books = [
    b for b in st.session_state.books
    if search.lower() in b["title"].lower() or search.lower() in b["author"].lower()
] if search else st.session_state.books

# ---------------- SHFAQ LIBRAT ----------------
st.subheader("📖 Librat")

if filtered_books:
    for i, book in enumerate(filtered_books):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(f"{book['title']} - {book['author']}")

        with col2:
            if st.button("🗑️ Fshi", key=i):
                st.session_state.books.remove(book)
                st.rerun()
else:
    st.info("Nuk ka libra.")

# ---------------- FSHI TË GJITHA ----------------
if st.button("❌ Fshi të gjithë librat"):
    st.session_state.books = []
    st.warning("Të gjithë librat u fshinë!")
    st.rerun()