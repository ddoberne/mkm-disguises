import streamlit as st
import disguises

st.title('Who dat?')
st.divider()
mana_sources = []
possible_mana_sources = ['none', 'W', 'U', 'B', 'R', 'G', 'W-U', 'W-B', 'W-R', 'W-G',
                         'U-B', 'U-R', 'U-G', 'B-R', 'B-G', 'R-G', '*', 'c']
current = st.sidebar.selectbox('Add mana source:', options = possible_mana_sources, index = 0)
while (current != 'none'):
    mana_sources.append(current)
    current = st.sidebar.selectbox('Add mana source:', options = possible_mana_sources, index = 0)


st.sidebar.write(str(mana_sources))
