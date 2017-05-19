import netifaces
import json
from mailer import EmailSender

# Create EmailSender instance
sender = EmailSender(

# Let's get ip addresses assigned to each of the interfaces installed in this system

# Let's get the external IP this machine is using on the internet

if __name__ == "__main__":

    args_parser = argparse.ArgumentParser(
                    description='Create one or more MATLAB process(es) to execute multiple cpricer instances.'
                )

	args_parser.add_argument('email_id', type=str)
	args_parser.add_argument('email_password', type=str)
	args_parser.add_argument('smtp_address', type=str)
        args_parser.add_argument('smtp_port_number', type=str)
        args_parser.add_argument('smtp_ssl', action='store_true')

	args = args_parser.parse_args()

	global mc_dll_id_range_start
	mc_dll_id_range_start = args.mc_dll_id_range_start

	global caller_counter
	caller_counter = 0

	if args.vanilla:
		start_matlab(
			args.number_of_processes
			,vanilla_mode_enabled=True
		)
	elif args.custom:
		if len(args.custom) == 0:
			print('ERROR: A prefix needs to be specified after the --custom argument.')
			sys.exit()
		else:
			start_matlab(
				args.number_of_processes
				,custom_list_mode_enabled=True
				,custom_prefix=args.custom
			)
	else:
		start_matlab(
			args.number_of_processes
		)
