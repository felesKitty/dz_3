
def info_about_user(name, surname, year_of_born, city,
                    e_mail, phone_number):
    return f'Name: {name}. Surname: {surname}. ' \
           f'Year of your born: {year_of_born}. City: {city}. ' \
           f'Your mail: {e_mail}. Phone number: {phone_number}.'

print(info_about_user(name='Maria', surname='Pupkina',
                      year_of_born='1978', e_mail='pupkina_smile@mail.ru',
                      phone_number='8999-555-1256', city='Kaliningrad'))