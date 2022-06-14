import sys

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


def update_password(username, password):
    changed = False

    user = User.objects.get(username=username)
    if not user:
        raise RuntimeError("User not found")

    matches = user.check_password(password)
    if not matches:
        user.set_password(password)
        user.save()
        changed = True

    return changed


class Command(BaseCommand):
    help = 'Updates a password non-interactively'

    def add_arguments(self, parser):
        parser.add_argument('username',
                            help='Username to change the password for')
        parser.add_argument('--password',
                            help='New password for user')
        parser.add_argument('--stdin',
                            action='store_true',
                            default=False,
                            help='Get new password from stdin')

    def handle(self, *args, **options):
        if not options['username']:
            raise CommandError('Username required')

        if options['password'] and options['stdin']:
            raise CommandError('Only one of [--password, --stdin] possible')

        got_password = False
        if not options['password'] and options['stdin']:
            lines = sys.stdin.readlines()
            if len(lines) > 0:
                password = lines[-1].rstrip('\n')
                if len(password) > 0:
                    options['password'] = password
                    got_password = True

        if not got_password:
            raise CommandError('Password required')

        changed = update_password(options['username'], options['password'])
        if changed:
            return "Password updated"
        return "Password not updated"
