import prettytable

from src.user.domain.user import User


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

def create_predictions_table(predictions: list):
    table = "\n"

    for index, prediction in enumerate(predictions):
        if User.is_admin(prediction.user_id, prediction.league_id):
            table += f"{prediction.user_id} (A)\n 🥇{prediction.p1}  🥈{prediction.p2}  🥉{prediction.p3}\n\n"
            continue
        table += f"{prediction.user_id}\n 🥇{prediction.p1}  🥈{prediction.p2}  🥉{prediction.p3}\n\n"

    return table

def create_drivers_table(drivers: list):
    table = prettytable.PrettyTable(['Driver', 'Code', 'Number'])
    table.align['Driver'] = 'l'
    table.align['Code'] = 'm'
    table.align['Number'] = 'r'

    for driver in drivers:
        table.add_row([driver.surname, driver.code, driver.number])

    return table
