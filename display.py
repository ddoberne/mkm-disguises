import streamlit as st
import disguises

st.title('Who dat?')
st.divider()
mana_sources = []
possible_mana_sources = ['W', 'U', 'B', 'R', 'G', 'W-U', 'W-B', 'W-R', 'W-G',
                         'U-B', 'U-R', 'U-G', 'B-R', 'B-G', 'R-G', '*', 'c']

msdict = {}
for possible_mana_source in possible_mana_sources:
    msdict[possible_mana_source] = st.number_input(label = possible_mana_source, min_value = 0, step = 1)

for key in msdict.keys():
    for i in range(msdict[key]):
        mana_sources.append(key)
        
st.sidebar.write(str(mana_sources))
