text = 'съешь ещё этих мягких французских булок'
print(text[0])                              # с
print(text[1])                              # ъ
print(text[len(text)-1])                    # к
print(text[-1])                             # к
print(text[-5])                             # б
print(text[:])                              # съешь ещё этих мягких французских булок
print(text[:2])                             # съ
print(text[len(text)-2:])                   # ок
print(text[2:9])                            # ешь ещё
print(text[6:-18])                          # ещё этих мягких
print(text[0:len(text):6])                  # сеикакал
print(text[::6])                            # сеикакал
text = text[2:9] + text[-5] + text[:2]      # ешь ещебсъ