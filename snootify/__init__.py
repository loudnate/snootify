import argparse
import sys

from .monitor import Monitor
from .monitor import SessionStatus


def run(argv=None, monitor: Monitor = Monitor()):
    parser = argparse.ArgumentParser(description="Snootify CLI")
    parser.add_argument(
        'command', default='status', choices=['status', 'debug', 'send']
    )
    parser.add_argument(
        "-l",
        "--level",
        default=SessionStatus.SOOTHING,
        type=SessionStatus.from_str,
        help="Lowest level to trigger a notification",
        choices=[SessionStatus[status] for status in SessionStatus._member_names_]
    )
    args = parser.parse_args(argv or sys.argv[1:])

    monitor.update_session()

    if args.command == 'status':
        print(monitor)
    elif args.command == 'debug':
        print(repr(monitor))
    elif args.command == 'send':
        message = monitor.notify(level=args.level)
        if message is not None:
            print(f"Sent: {message}")
        else:
            print("No message to send")


if __name__ == "__main__":
    run()
