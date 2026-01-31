import time
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Crimson Corridor 2D", layout="wide")

st.title("Crimson Corridor 2D: Serbianhero at Nachtarena")
st.caption(
    "Use WASD/Arrow keys to move, E to interact, Space to slap (cartoon), and P to pause."
)

if st.button("Reload game assets"):
    st.rerun()

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")
html_with_buster = html.replace(
    "</head>",
    f"<meta name=\"cache-buster\" content=\"{int(time.time())}\"></head>",
)

components.html(html_with_buster, height=820, scrolling=False)

with st.expander("How to play", expanded=False):
    st.markdown(
        """
        **Controls**
        - Move: **WASD / Arrow keys**
        - Interact: **E**
        - Slap (cartoon): **Space**
        - Pause: **P**

        **Goal**
        - Build respect/viral energy and keep heat low to pass all three door checks.
        """
    )
