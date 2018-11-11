day = input('Введите день недели в двухбуквенном формате (пн, вт...)')
new_text = ''
with open('input.txt') as f_in:
    text = f_in.readlines()
for i in text:
    f1 = i.find(day)
    print(f1)
    if f1 != -1:
        f2 = i.find(':')
        print(f2)
        name = i[0:f2]
        print(name)
        new_text += ' ' + name + ','
new_text = new_text[0: -1]
with open('output.txt', 'w') as f_out:
    if new_text == '':
        f_out.write('На выбранный день недели ничего не найдено. Попробуйте еще раз.')
    else:
        f_out.write('В выбранный день можно посетить следующие представления:' + new_text)

