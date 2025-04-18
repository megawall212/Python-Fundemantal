#Set up the price for child and adult before 2 pm
adult_before = 11.17
child_before = 8.00
#Set up the price for child and adult after 2 pm
adult_after = 12.45
child_after = 9.68

#function used to display the available movie:
def type():
    #input the movie choice,showtime, and number of adult/child tickets
    choice = input('Movie choice:\t')
    choice = choice.upper()

    if (choice != 'A') and (choice != 'B') and (choice != 'C'):
        print('Invalid option; please restart app...')
    else:
        showtime = int(input('Showtime:\t'))
        showtime = abs(showtime)
        if (choice == 'A') and (showtime>4):
            print('Invalid option; please restart app...')
        elif(choice =='B') and (showtime>2):
            print('Invalid option; please restart app...')
        elif (choice == 'C') and (showtime > 4):
            print('Invalid option; please restart app...')


        else:

            adult_ticket = int(input('Adult tickets:\t'))
            adult_ticket = abs(adult_ticket)
            child_ticket = int(input('Kid tickets:\t'))
            child_ticket = abs(child_ticket)
            if adult_ticket + child_ticket >=30:
                print('Invalid option; please restart app...')
            else:
                calculate(choice,showtime,adult_ticket,child_ticket)
def display():
    print('Available movies today:')
    print('A)12 Strong:	1)2:30  2)4:40  3)7:50  4)10:50')
    print('B)Coco:		1)12:40 2)3:45')
    print('C)The Post:	1)12:45 2)3:35  3)7:05  4)9:55')
    type()



def calculate(choice,showtime,adult_ticket,child_ticket):


    if ((choice == 'B') and (showtime == 1)) or ((choice == 'C') and (showtime == 1)):
        total = 11.17 * adult_ticket + 8 * child_ticket
    else:
        total = 12.45 * adult_ticket + 9.68 * child_ticket
    print(f"Total cost:\t${total:.2f}")




if __name__ == '__main__':
    display()
