def caese(text,num):
    zugi = ''
    hi_zugi = ''

    for i ,j in enumerate(text):
        if j % num == 0:
            zugi += i
        else:
            hi_zugi += i


    new_text = zugi + hi_zugi
    return new_text