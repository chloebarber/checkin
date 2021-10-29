from flask.cli import AppGroup
from .users import seed_users, undo_users
from .sites import seed_sites
from .zones import seed_zones
from .people import seed_people
from .logs import seed_logs

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_sites()
    seed_zones()
    seed_people()
    seed_logs()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # Add other undo functions here
