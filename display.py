import streamlit as st
import disguises

st.title('Who dat?')
st.divider()
mana_sources = []
possible_mana_sources = ['none', 'W', 'U', 'B', 'R', 'G', 'W-U', 'W-B', 'W-R', 'W-G',
                         'U-B', 'U-R', 'U-G', 'B-R', 'B-G', 'R-G', '*', 'c']
i = 0
current = st.sidebar.selectbox('Add mana source:', options = possible_mana_sources, index = 0, key = i)
while (current != 'none'):
    mana_sources.append(current)
    i += 1
    current = st.sidebar.selectbox('Add mana source:', options = possible_mana_sources, index = 0, key = i)


st.sidebar.write(str(mana_sources))
