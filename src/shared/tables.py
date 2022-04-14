import prettytable


def create_standings_table(users: list):
    table = prettytable.PrettyTable(['Username', 'Points'])
    table.align['Username'] = 'l'
    table.align['Points'] = 'r'

    for user in users:
        if user.isAdmin:
            table.add_row([f'{user.userId}(ADMIN)', user.points])
            continue
        table.add_row([user.userId, user.points])

    return table


def create_drivers_table(drivers: list):
    table = prettytable.PrettyTable(['Driver', 'Code', 'Number'])
    table.align['Driver'] = 'l'
    table.align['Code'] = 'm'
    table.align['Number'] = 'r'

    for driver in drivers:
        table.add_row([driver.surname, driver.code, driver.number])

    return table
