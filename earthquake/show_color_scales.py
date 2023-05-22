from plotly import colors

for key, values in colors.PLOTLY_SCALES.items():
    print(key)
    print(values)
    print("-----------------")

print("------------------")
print("------------------")
print("------------------")
print("------------------")

"""
Plotly interpolates shades between each of these defined colors.
Ara renkler ile enterpolasyon'u istediğimiz gibi mi manipüle ediyoruz?
"""
print(colors.PLOTLY_SCALES)