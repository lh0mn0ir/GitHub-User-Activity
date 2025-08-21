import argparse
from controllers import get_user


parser = argparse.ArgumentParser(description="display GitHub user activity.")

# Subcommand for user events
parser.add_argument("--username", help="Get user events")

args = parser.parse_args()

user_events = get_user(args.username)
if user_events:
	print(f"\nEvents data:")
	print(
		f"- {user_events['type']} at {user_events['created_at']}\nuser: {user_events['login']}"
	)
	print(f"Total public repos: {user_events['public_repos']}")
else:
	parser.print_help()

