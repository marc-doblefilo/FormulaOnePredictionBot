import prettytable


def create_standings_table(users: list):
    table = prettytable.PrettyTable(['Username', 'Points'])
    table.align['Username'] = 'l'
    table.align['Points'] = 'r'

    for user in users:
        table.add_row([user.userId, user.points])

    return table
