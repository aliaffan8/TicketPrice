
tickets_input = input('Please enter the tickets for every type in the specified format (1 Economy,2 Premium,0 Adult,3 Toddler) \
and no space after commas: ')
ticket_input = tickets_input.split(',')
tickets = []
ticket_type = []

for i in ticket_input:
    temp = i.split(' ')
    tickets.append(int(temp[0].strip()))
    ticket_type.append(temp[1])

is_Fazaa = input('Do you have Fazaa card? ')
is_Fazaa = True if is_Fazaa.title() == 'Yes' else False


is_Teacher = input('Are you a teacher? ')
is_Teacher = True if is_Teacher.title() == 'Yes' else False

"""Number of Tickets check to ensure that the numbered ordered is not negative"""
ticket_no_invalid = False
for i in tickets:
    if i < 0:
        print(f"{i} not a valid ticket number order")
        ticket_no_invalid = True
        break

"""Ticket type check"""
ticket_type_invalid = False
for i in ticket_type:
    if i.title() not in ('Economy', 'Toddler', 'Premium', 'Adult'):
        print(f"{i} not a valid ticket option")
        ticket_type_invalid = True
        break

for i in range(2):
    print()

"""Code for calculating ticket prices"""

if ticket_type_invalid == False and ticket_no_invalid == False:
    print('Tickets order', tickets_input)
    print("Fazaa card available: ", is_Fazaa)
    print("Teacher: ", is_Teacher)

    ticket_type_index = 0
    ticket_price = 0

    for i in tickets:
        price_type = ticket_type[ticket_type_index].title()
        if price_type == 'Economy':
            price = 185
        elif price_type == 'Premium':
            price = 255 
        elif price_type == 'Adult':
            price = 75 
        elif price_type == 'Toddler':
            price = 105
        ticket_type_index +=1

        ticket_price = ticket_price + (i * price)

    print("Ticket pricing applicable without a discount: ", ticket_price) 

    """Incorporating discounts in ticket pricing"""

    discount = 0.5 * ticket_price
    if is_Fazaa == True or is_Teacher == True:
        print("Discount applicable: ", discount)
        total_ticket_price = ticket_price - discount
        print('Total ticket pricing applicable after a discount: ', total_ticket_price)