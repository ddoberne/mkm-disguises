import streamlit as st
import disguises

st.title('Who dat?')
st.divider()
mana_sources = []
possible_mana_sources = ['rainbow', 'W', 'U', 'B', 'R', 'G', 'colorless']
other_mana_sources = ['W-U', 'W-B', 'W-R', 'W-G', 'U-B', 'U-R', 'U-G', 'B-R', 'B-G', 'R-G']

st.sidebar.subheader('Mana sources:')

msdict = {}
for possible_mana_source in possible_mana_sources:
    msdict[possible_mana_source] = st.sidebar.number_input(label = possible_mana_source, min_value = 0, step = 1)
if st.sidebar.checkbox(label = 'Show surveil lands', value = False):
    for possible_mana_source in other_mana_sources:
        msdict[possible_mana_source] = st.sidebar.number_input(label = possible_mana_source, min_value = 0, step = 1)

for key in msdict.keys():
    for i in range(msdict[key]):
        mana_sources.append(key)

st.write(f'Total available mana: {len(mana_sources)}')

possible_suspects = []
for d in disguises.disguise_list:
    if d.castable(mana_sources):
        possible_suspects.append(d)

for suspect in possible_suspects:
    st.write(f'![{suspect.name'}]({suspect.image})')
