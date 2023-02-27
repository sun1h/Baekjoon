croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
st=input()
for c in croatia:
    st=st.replace(c,'c')    
print(len(st))