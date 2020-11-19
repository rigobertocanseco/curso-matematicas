import ttg

s = '(((p_0 or p_1) => (( p_2 or p_3 ) => ( (not p_4) => p_5)) ) and ( (~(p_4 or p_6)) => p_7)) => (p_0 => (p_2 => p_7))'

#s = '(p_4 or p_5) and (p_4 or p_6)'

#print(ttg.Truths(['p_0','p_1','p_2', 'p_3','p_4', 'p_5', 'p_6','p_7'], [s]).as_tabulate(index=False, table_format='latex'))


#(((p_0 or p_1) => (( p_2 or p_3 )  => ( (not p_4) => p_5)) ) and (not(p_4 or p_6) => p_7)) => (p_0 => (p_2 => p_7))

#(((p_0 or p_1) => (( p_2 or p_3 ) => (not p_4 => p_5)) ) and (not(p_4 or p_6) => p_7)) => (p_0 => (p_2 => p_7))




s= '( (p_0 or p_1) and p_5) and ( not (p_6) and not (p_5))'
s2= '(not(p_0) or not(p_5)) and (not(p_1) or not(p_5)) and (p_6 or p_5)'

s3= 'not( ((p_0 or p_1) and p_5) = ( (not(p6)) => p_5) )'
print(ttg.Truths(['p_0','p_1','p_5', 'p_6'], [s3]))

