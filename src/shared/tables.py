import prettytable


def create_standings_table(users: list):
    table = "\n"

    if(len(users) >= 1):
        table += "🥇" + users[0].userId + "  " + str(users[0].points) + " POINTS\n"
    if(len(users) >= 2):
        table += "🥈" + users[1].userId + "  " + str(users[1].points) + " POINTS\n"
    if(len(users) >= 3):
        table += "🥉" + users[2].userId + "  " + str(users[2].points) + " POINTS\n"

    if(len(users) >= 4):
        for index, user in enumerate(users[3:]):
            table += index +". " + user.userId + "  " + str(user.points) + " POINTS\n"

    print(table)
    return table


def create_drivers_table(drivers: list):
    table = prettytable.PrettyTable(['Driver', 'Code', 'Number'])
    table.align['Driver'] = 'l'
    table.align['Code'] = 'm'
    table.align['Number'] = 'r'

    for driver in drivers:
        table.add_row([driver.surname, driver.code, driver.number])

    return table
