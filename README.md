# imalive
`imalive` is a simple Python script that checks ip addresses assigned to every network interfaces installed in the machine the script is running, and sends those addresses to email recipients. imalive uses [`netifaces`](https://alastairs-place.net/projects/netifaces/) package.

It also checks the public IP the machine is using on the internet and reports that as well. For now, it directly sends the output from 'netifaces.ifaddresses()' and the public IP query on https://api.ipify.org. I just needed this to check the private IP address assigned to one of the machines I use, so nothing really fancy in this script.

I use this in conjunction with `crontab` on a Linux machine. Remember to put `.imalive_config.json` in the home directory of the user account the script will run on.

Works on whatever platform `netifaces` and CPython supports. (*nix / Windows)

# License

`imalive` is licensed under BSD-new license. Please check `LICENSE`.
