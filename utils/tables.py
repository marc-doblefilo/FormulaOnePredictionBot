import prettytable


def create_standings_table(users: list):
    table = "\n"

    for index, user in enumerate(users):
        if index == 0:
            if user.isAdmin:
                table += "🥇" + user.userId + " (A)" + "\n" + str(user.points) + " POINTS\n\n"
                continue
            table += "🥇" + user.userId + "\n" + str(user.points) + " POINTS\n\n"
            continue
        if index == 1:
            if user.isAdmin:
                table += "🥈" + user.userId + " (A)" + "\n" + str(user.points) + " POINTS\n\n"
                continue
            table += "🥈" + user.userId + "\n" + str(user.points) + " POINTS\n\n"
            continue
        if index == 2:
            if user.isAdmin:
                table += "🥉" + user.userId + " (A)" + "\n" + str(user.points) + " POINTS\n\n"
                continue
            table += "🥉" + user.userId + "\n" + str(user.points) + " POINTS\n\n"
            continue
        
        if user.isAdmin:
            table += str(index+1) + ". " + user.userId + " (A)" + "\n" + str(user.points) + " POINTS\n\n"
            continue
        table += str(index+1) + ". " + user.userId + "\n" + str(user.points) + " POINTS\n\n"

    return table


def create_drivers_table(drivers: list):
    table = prettytable.PrettyTable(['Driver', 'Code', 'Number'])
    table.align['Driver'] = 'l'
    table.align['Code'] = 'm'
    table.align['Number'] = 'r'

    for driver in drivers:
        table.add_row([driver.surname, driver.code, driver.number])

    return table
