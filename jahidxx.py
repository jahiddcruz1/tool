import os
import random
import string
import uuid
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests
import json
import sys
import os
import platform
import re





filefolder = "C:/Users/Public/NguyenTheQuyet"
try: 
    os.mkdir(filefolder) 
except OSError as error: 
    pass  
filepath = filefolder+'/Keytool.txt'
try:
    f = open(filepath)
    print("Licence Key: "+f.read()+'|JTXFBTOOL')
except IOError:
    key = ''
    chunk = ''
    check_digit_count = 0
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    while len(key) < 25:
        char = random.choice(alphabet)
        key += char
        chunk += char
        if len(chunk) == 4:
            key += '-'
            chunk = ''
    key = key[:-1]
    with open(filepath, 'w') as f:
        f.write(key)

keymay = open(filepath).read()+'|JTXFBTOOL'
k = requests.get('https://docs.google.com/spreadsheets/d/18V2R6lU4YEWBlyQgRyxXt-Qh6Zlw40vy890KuOGLqk4/edit?usp=sharing').text
if keymay in k:
        print("")

else:
    print('''
             -------------------------------------------------------------

                        OWNER : JAHID D'CRUZ
                        FACEBOOK : https://facebook.com/jahid.tech
                        TELEGRAM : @jtsmmpanel_admin

            -------------------------------------------------------------
          
          Your licence is not active / expired, please contact owner to purchase
          

          
          ''')
    input()
    quit()




darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
def Video_Extractid(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'
    video_pattern = r'videos/(\d+)/'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)
    video_match = re.search(video_pattern, url)

    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    elif video_match:
        video_id = video_match.group(1)
        return video_id
    else:
        return None 
def extract_ids(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)

    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    else:
        return None 
    







    
def jovan():
    adrkz = "\033[34m "
    violet_chu = "\033[1;35m"
    print(f"""
    {violet_chu} 
                
        
 
       _________  __ __________  __    __    ____ _       __
      / /_  __/ |/ // ____/ __ \/ /   / /   / __ \ |     / /
 __  / / / /  |   // /_  / / / / /   / /   / / / / | /| / / 
/ /_/ / / /  /   |/ __/ / /_/ / /___/ /___/ /_/ /| |/ |/ /  
\____/ /_/  /_/|_/_/    \____/_____/_____/\____/ |__/|__/   
                                                            


                                                                                             
                                                                                             
                                                                  
                🎀 {white} https://jtsmmpanel.com  🎀
     {adrkz}───────────────────────────────────────────────────────────────\033[0m
     {violet_chu}OWNER    {yellow}: {green}Jahid D'cruz
     {violet_chu}DESC:    {yellow}: {green}THIS IS A FACEBOOK AUTOMATION TOOL                                                               
     {violet_chu}TOOL     {yellow}: {green}JAHID X FOLLOWS
     {adrkz}───────────────────────────────────────────────────────────────\033[0m""")  
    

def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([
        True,
        False])
    if is_win64:
        if not 'WOW64;':
            user_agent = f'''Mozilla/5.0 (Windows NT {windows_version}.{''}Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'''
            return user_agent
import os
import uuid
import random
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import string  

import os

def createfile():
    folder_name = "/sdcard/boostphere"
    file_names = ["FRAACCOUNT.txt", "FRAPAGES.txt", "RPWACCOUNT.txt", "RPWPAGES.txt"]


# Check if the folder exists, if not, create it
    if not os.path.exists(folder_name):


        try:
          os.makedirs(folder_name)
        except Exception:
              pass
              # Fail silently if unable to create the folder

# Check and create each file in the list if it doesn't exist
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)

        if not os.path.exists(file_path):

            try:

                with open(file_path, 'w') as file:

                    pass  # Create an empty file if it doesn't exist
            except Exception:

                pass  # Fail silently if unable to create the file


def count_tokens(accounts_file, pages_file):
    """Count the number of accounts and pages stored in the respective files."""
    total_accounts = 0
    total_pages = 0

    try:
        with open(accounts_file, 'r') as af:
            total_accounts = sum(1 for line in af if line.strip())  
    except FileNotFoundError:
        print(f"Account file not found: {accounts_file}")

    try:
        with open(pages_file, 'r') as pf:
            total_pages = sum(1 for line in pf if line.strip())  
    except FileNotFoundError:
        print(f"Page file not found: {pages_file}")

    return total_accounts, total_pages

def get_ua():
    """Generate a random user agent for a Samsung device."""
    return f'''Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S{random.randrange(100, 9999)}/{random.randrange(100, 9999)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randrange(1, 9)}; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/{random.randrange(1, 9)}.{random.randrange(1, 9)} Mobile WVGA SMM-MMS/1.2.0 OPN-B'''

def get_token(email, password, user_agent, success_count, fail_count):
    """Get access token for a given email and password."""
    url = 'https://b-api.facebook.com/method/auth.login'
    form = {
        'adid': str(uuid.uuid4()),
        'email': email,
        'password': password,
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'cpl': 'true',
        'family_device_id': str(uuid.uuid4()),
        'locale': 'en_US',
        'client_country_code': 'US',
        'credentials_type': 'device_based_login_password',
        'generate_session_cookies': '1',
        'generate_analytics_claim': '1',
        'generate_machine_id': '1',
        'currently_logged_in_userid': '0',
        'irisSeqID': 1,
        'try_num': '1',
        'enroll_misauth': 'false',
        'meta_inf_fbmeta': 'NO_FILE',
        'source': 'login',
        'machine_id': 'KBz5fEj0GAvVAhtufg3nMDYG',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '882a8490361da98702bf97a021ddc14d',
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
    }

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-friendly-name': 'fb_api_req_friendly_name',
        'x-fb-http-engine': 'Liger',
        "accept-language": "fil-PH,fil;q=0.9,en-US;q=0.8,en;q=0.7",
        'user-agent': get_ua()  # Pass the user_agent parameter
    }

    try:
        response = requests.post(url, data=form, headers=headers)
        response_data = response.json()

        if 'access_token' in response_data:
            access_token = response_data['access_token']
            success_count.append({"email": email, "access_token": access_token})
            print("     \033[1;37m───────────────────────────────────────────────────────────────\033")
            print(f"     \033[1;32m[SUCCESS]\033[0m \033[1;33mSUCCESSFULLY EXTRACTED\033[0m ──────> \033[1;37m{email}\033[0m\n")
            print("      \033[1;37m───────────────────────────────────────────────────────────────\033")
        else:
            fail_count.append(email)
            print("      \033[1;37m───────────────────────────────────────────────────────────────\033")
            print(f"     \033[1;31m[FAILED]\033[0m \033[1;33mFAILED TO EXTRACT\033[0m ──────> \033[1;37m{email}\033[0m\n")
            print("      \033[1;37m───────────────────────────────────────────────────────────────\033")
    except requests.RequestException as e:
        fail_count.append(email)
        print(f"Error processing {email}: {e}")
        time.sleep(1)

def payl(file_path):
    """Process the file and extract uid-password pairs."""
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return None, []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        print("File is empty.")
        return None, []

    # No longer using a password line, instead we handle uid|password format
    uid_password_pairs = [line.strip().split('|') for line in lines if '|' in line.strip()]
    
    if not uid_password_pairs:
        print("Invalid file format.")
        return None, []

    # Unpack uids and passwords from the pairs
    uids, passwords = zip(*uid_password_pairs)
    return uids, passwords

def mainmany():
    
    clear_screen()
    jovan()

    """Main function to execute the process."""
    print(f"     {yellow}[1] {green}Save in FRAACCOUNT.txt & FRAPAGES.txt")
    print(f"     {yellow}[2] {green}Save in RPWACCOUNT.txt & RPWPAGES.txt")
    save_choice = input(f"     {yellow}CHOICE: ").strip()

    folder_path = "/sdcard/boostphere"  # Folder path

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        page_file = os.path.join(folder_path, "FRAPAGES.txt")
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        page_file = os.path.join(folder_path, "RPWPAGES.txt")
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"    {green}THE FORMAT SHOULD BE {red}uid|pass")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     {green}PATH: ").strip()

    uids, passwords = payl(file_path)

    if not uids or not passwords:
        print("Invalid file format or missing data.")
        return

    success_count = []
    fail_count = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for uid, password in zip(uids, passwords):
            user_agent = get_ua()  # Get a random user agent
            futures.append(executor.submit(get_token, uid, password, user_agent, success_count, fail_count))

        for future in as_completed(futures):
            future.result()  
    
    if success_count:
        
        existing_tokens = set()
        if os.path.exists(account_file):
            with open(account_file, 'r') as f:
                existing_tokens = set(f.read().splitlines())

        with open(account_file, 'a') as f:  
            for account in success_count:
                token_entry = f"{account['email']}|{account['access_token']}"
                if token_entry not in existing_tokens:
                    f.write(token_entry + "\n")

    print("\033[1;37m───────────────────────────────────────────────────────────────\033")
    print(f"\033[1;34m[SUCCESS]\033[0m: {len(success_count)} accounts successfully extracted.")
    print(f"\033[1;31m[FAILED]\033[0m: {len(fail_count)} accounts failed to extract.")
    print("\033[1;37m───────────────────────────────────────────────────────────────\033")   
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction_vid(token, uid_url, reaction_type, reactions_count):
    """Send a reaction using the provided access token."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    
    try:
        response = requests.post(auto_react)
        return access_token, response.status_code, response.text  # Return the results for further processing
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)  # Handle request exceptions
def clear_text_files():
    """Clear the contents of specified text files."""
    file_paths = [
        "/sdcard/boostphere/FRAACCOUNT.txt",
        "/sdcard/boostphere/FRAPAGES.txt",
        "/sdcard/boostphere/RPWACCOUNT.txt",
        "/sdcard/boostphere/RPWPAGES.txt"
    ]

    for file_path in file_paths:
        try:
            with open(file_path, 'w') as file:
                file.truncate(0)  # Clear the file content
            print(f"Successfully cleared: {file_path}")
        except Exception as e:
            print(f"Error clearing {file_path}: {str(e)}")

# You can call the function like this:
# clear_text_files()

def perform_reaction_fast_vid():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  
    
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/videos/539673715119122/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = Video_Extractid(z)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id  

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        
        return

    # Step 5: Check if the requested number of reactions exceeds the available tokens
    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT exceeding {len(tokens)}")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        return

    # Step 6: Perform reactions using multithreading
    reactions_count = 0
    max_workers = 20  # Set maximum number of threads
    results = []  

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit reactions for each token
        future_to_token = {executor.submit(perform_reaction_vid, token, uid_url, reaction_type, reactions_count): token for token in tokens[:num_reactions]}

        for future in as_completed(future_to_token):
            token = future_to_token[future]
            try:
                access_token, status_code, response_text = future.result()
                if status_code == 200:
                    reactions_count += 1
                    print(f"   \033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY REACTED\033[1;32m {blue}───────> {yellow}{uid_url}")
                else:
                    print(f"   \033[1;31m[FAILED]\033[1;31m FAILED TO REACT {blue}───────> {yellow}{uid_url}")
            except Exception as e:
                print(f"Error processing token {token}: {e}")
    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL: {reactions_count}")





import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type, reactions_count):
    """Send a reaction using the provided access token."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()  # Use the randomly selected user agent
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text  # Return the results for further processing
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)  # Handle request exceptions

def perform_reaction_fast():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  
    
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/541319968479439/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = extract_ids(z)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id  

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        
        return

    
    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT exceeding {len(tokens)}")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        return

    
    reactions_count = 0
    max_workers = 20  
    results = []  

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        
        future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type, reactions_count): token for token in tokens[:num_reactions]}

        for future in as_completed(future_to_token):
            token = future_to_token[future]
            try:
                access_token, status_code, response_text = future.result()
                if status_code == 200:
                    reactions_count += 1
                    print(f"   \033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY REACTED\033[1;32m {blue}───────> {yellow}{uid_url}")
                else:
                    print(f"   \033[1;31m[FAILED]\033[1;31m FAILED TO REACT {blue}───────> {yellow}{uid_url}")
            except Exception as e:
                print(f"Error processing token {token}: {e}")
    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL: {reactions_count}")




import re

def extract_reel_id(link):
    """
    Extract the reel ID from the provided Facebook reel link.
    Example: https://www.facebook.com/reel/1020864812286112?mibextid=rS40aB7S9Ucbxw6v
    should return '1020864812286112'
    """
    # Define the regular expression pattern to match the reel ID
    pattern = r'/reel/(\d+)'  # Looks for '/reel/' followed by digits
    
    # Search for the pattern in the link
    match = re.search(pattern, link)
    
    if match:
        # If the pattern matches, return the reel ID (the digits after '/reel/')
        return match.group(1)
    else:
        # Return None if no match found
        return None

# Example usage:
def react_comment(token, uid_url, reaction_type, reactions_count):
    """Send a reaction using the provided access token."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()  # Use the randomly selected user agent
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text  # Return the results for further processing
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)  # Handle request exceptions

def comment_react():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  
    
    # Step 4: Get post ID and comment ID
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/541319968479439/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    post_id = input(f"   {green}POST ID: ")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    comment_id = input(f"   {green}COMMENT ID: ")

    uid_url = f"{post_id}_{comment_id}"  # Format post ID and comment ID

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return

    # Step 5: Check if the requested number of reactions exceeds the available tokens
    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT exceeding {len(tokens)}")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        return

    # Step 6: Perform reactions using multithreading
    reactions_count = 0
    max_workers = 20  # Set maximum number of threads
    results = []  

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        
        future_to_token = {executor.submit(react_comment, token, uid_url, reaction_type, reactions_count): token for token in tokens[:num_reactions]}

        for future in as_completed(future_to_token):
            token = future_to_token[future]
            try:
                access_token, status_code, response_text = future.result()
                if status_code == 200:
                    reactions_count += 1
                    print(f"   \033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY REACTED\033[1;32m {blue}───────> {yellow}{uid_url}")
                else:
                    print(f"   \033[1;31m[FAILED]\033[1;31m FAILED TO REACT {blue}───────> {yellow}{uid_url}")
            except Exception as e:
                print(f"Error processing token {token}: {e}")
    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL: {reactions_count}")


#REACT TO REELS
import os
import random
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# Load user agents from a file
def load_user_agents(ua_file):
    """Load user agents from a file."""
    if not os.path.isfile(ua_file):
        print("User agents file not found.")
        return []
    
    with open(ua_file, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Select a random user agent

# Send a reaction using the provided access token for reels
def react_to_reels(token, reels_link, reaction_type):
    """Send a reaction using the provided access token for reels."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    reels_react_url = f'https://graph.facebook.com/v20.0/{reels_link}/reactions?type={reaction_type}&access_token={access_token}'

    headers_ = {
        'User-Agent': W_ueragnt()  # Use the randomly selected user agent
    }

    try:
        response = requests.post(reels_react_url, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

# Main function to perform reactions
def perform_reaction_reels():
    """Perform reactions based on user input for file choice, reels link, reaction type, and number of reactions."""
    
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""    {white}CHOOSE TYPE OF REACTORS: 
    {blue}[1] {green}FRA ACCOUNT 
    {blue}[2] {green}FRA PAGES
    {blue}[3] {green}RPW ACCOUNT
    {blue}[4] {green}RPW PAGES
    {blue}[0] {green}EXIT
    {blue}───────────────────────────────────────────────────────────────""")
    
    try:
        file_choice = int(input("     Choose: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────")
        if file_choice == 0:
            return  # Exit
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the selected line

    
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/reel/638981218192398?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    a = input(f"     {green}Enter the reels link: ")
    reels_link = extract_reel_id(a)
    print(f"    {blue}───────────────────────────────────────────────────────────────")
    print(f"""    {white}Choose the reaction type:
    {yellow}[1] {green}LIKE
    {yellow}[2] {green}LOVE
    {yellow}[3] {green}WOW
    {yellow}[4] {green}SAD
    {yellow}[5] {green}ANGRY
    {yellow}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────""")
    
    try:
        reaction_choice = int(input(f"    {blue}Choose: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────")
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None: 
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 5: Ask for the number of reactions
    try:
        num_reactions = int(input(f"    {green}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────")
    except ValueError:
        print("Please enter a valid number for reactions.")
        return

    # Step 6: Check if the requested number of reactions exceeds the available tokens
    if num_reactions > len(tokens):
        print(f"ENTER AGAIN NOT exceeding {len(tokens)}")
        return

    # Step 7: Perform reactions using multithreading
    reactions_count = 0
    max_workers = 20  # Set maximum number of threads
    total_successful_reactions = 0
    reactions_lock = Lock()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {executor.submit(react_to_reels, token, reels_link, reaction_type): token for token in tokens[:num_reactions]}

        for future in as_completed(future_to_token):
            token = future_to_token[future]
            try:
                access_token, status_code, response_text = future.result()
                if status_code == 200:
                    with reactions_lock:
                        total_successful_reactions += 1
                    print(f"   \033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY REACTED TO REELS\033[1;32m {blue}───────> {yellow}{reels_link}")
                else:
                    print(f"   \033[1;31m[FAILED]\033[1;31m FAILED TO REACTED TO REELS {blue}───────> {yellow}{reels_link}")
            except Exception as e:
                print(f"Error processing token {token}: {e}")
    print(f"    {blue}───────────────────────────────────────────────────────────────")
    print(f"TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")

# Example call
# perform_reaction_fast()


import re

def extract_user_id_prof(url):
    """Extract user ID from a Facebook profile URL."""
    pattern = r'id=(\d+)|profile\.php\?id=(\d+)'
    match = re.search(pattern, url)
    
    if match:
        return match.group(1) or match.group(2)  # Return the captured group
    return None  # Return None if no match is found

# Example usage


def follow_account(page_access_token, account_id):
    """Follow an account using a specific page access token."""
    headers_ = {
        'User-Agent': W_ueragnt()  # Use the randomly selected user agent
    }
    headers = {
        'Authorization': f'Bearer {page_access_token}',
        **headers_  # Merging both headers
    }

    try:
        response = requests.post(
            f'https://graph.facebook.com/v18.0/{account_id}/subscribers',
            headers=headers
        )
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False
def auto_follow_fast():
    """Automatically follow a target account using tokens and pages."""
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF FOLLOWERS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return

    if len(tokens) == 0:
        print("No tokens found in the selected file.")
        return

    # Ask for starting line
    start_line = int(input(f"    {green}Enter the starting line {red}(1 to {len(tokens)}): "))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    tokens = tokens[start_line - 1:]  # Adjust token list based on the starting line

    a = input(f'    {green}Enter the target account ID: ')
    account_id = extract_user_id_prof(a)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    follow_limit = int(input(f'    {green}Enter the maximum number of follows: '))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
 
    follow_count = 0
    tasks = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        for token in tokens:
            if follow_count >= follow_limit:
                break

            page_access_token = token.split('|')[1]  # Assuming tokens are in email|token format
            tasks.append(executor.submit(follow_account, page_access_token, account_id))

        for future in as_completed(tasks):
            success = future.result()
            if success:
                follow_count += 1
                print(f"\033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY FOLLOWED\033[1;32m")
                if follow_count >= follow_limit:
                    break

    print(f'{red}Total follows performed: {follow_count}')


import re

def extract_fbid_dp(url):
    """Extract Facebook ID from a Facebook photo URL."""
    pattern = r'fbid=(\d+)'
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)  # Return the captured group
    return None  # Return None if no match is found


import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type, reactions_count):
    """Send a reaction using the provided access token."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    
    try:
        response = requests.post(auto_react)
        return access_token, response.status_code, response.text  # Return the results for further processing
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)  # Handle request exceptions

def perform_reaction_fast_dp():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  
    
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/photo.php?fbid=541361691808600")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = extract_fbid_dp(z)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id  

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        
        return

    # Step 5: Check if the requested number of reactions exceeds the available tokens
    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT exceeding {len(tokens)}")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        return

    # Step 6: Perform reactions using multithreading
    reactions_count = 0
    max_workers = 20  # Set maximum number of threads
    results = []  

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit reactions for each token
        future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type, reactions_count): token for token in tokens[:num_reactions]}

        for future in as_completed(future_to_token):
            token = future_to_token[future]
            try:
                access_token, status_code, response_text = future.result()
                if status_code == 200:
                    reactions_count += 1
                    print(f"   \033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY REACTED\033[1;32m {blue}───────> {yellow}{uid_url}")
                else:
                    print(f"   \033[1;31m[FAILED]\033[1;31m FAILED TO REACT {blue}───────> {yellow}{uid_url}")
            except Exception as e:
                print(f"Error processing token {token}: {e}")
    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL: {reactions_count}")

import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def rep(post_id, comment, access_token):
    """Comment on a Facebook post using the provided access token."""
    
    # Split the token in case it includes 'uid|access_token' format
    if '|' in access_token:
        _, access_token = access_token.split('|', 1)
    
    # Now check if the token starts with 'EA' or 'EAA'
    if not access_token.startswith(("EA", "EAA")):
        return f"Invalid token: {access_token}"
    
    try:
        converted_link = post_id
        auto_comment_url = f'https://graph.facebook.com/v13.0/{converted_link}/comments'
        params = {
            'message': comment,
            'access_token': access_token
        }
        time.sleep(1)  # Sleep for 1 second between comments
        headers = {
            'user-agent': W_ueragnt()  # Use the random user agent
        }
        response = requests.post(auto_comment_url, params=params, headers=headers)
        
        # Print status code and response for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if response.status_code == 200:
            return f"\033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY COMMENTED: {green}{comment}\033[1;32m"
        else:
            return f"\033[1;31m[FAILED]\033[1;31m FAILED TO COMMENT: {green}{comment} "

    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"


def reply():
    """Perform comments based on user input for file choice, starting line, post link, and number of comments."""
    
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {yellow}[1] {green}FRA ACCOUNT 
     {yellow}[2] {green}FRA PAGES
     {yellow}[3] {green}RPW ACCOUNT
     {yellow}[4] {green}RPW PAGES
     {red}[0] {red}EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        file_choice = int(input(f"     {green}Choose: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the given line
    
    # Step 4: Ask for the post ID
    a = input(f"    {green}Enter the post ID: ")
    b = input(f"    {green}Enter the comment ID: ")
    result = f"{a}_{b}"

    post_id = result
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    # Step 5: Ask how many comments and get the list of comments
    try:
        num_comments = int(input(f"    {red}Enter the number of comments: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if num_comments <= 0:
            print("Number of comments must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    comments_list = []
    for i in range(num_comments):
        comment = input(f"    {green}Enter comment {i + 1}: ")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        comments_list.append(comment)

    # Step 6: Ask how many accounts to use for commenting
    try:
        num_accounts = int(input(f"   {green}Enter the number of accounts to use for commenting (1 to {len(tokens)}): "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"Please enter a valid number between 1 and {len(tokens)}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 7: Perform comments using multithreading
    results = []
    comments_count = 0
    max_workers = 15  # Set the maximum number of threads
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        for i, token in enumerate(tokens[:num_accounts]):
            comment = random.choice(comments_list)  # Randomly pick a comment
            future = executor.submit(rep, post_id, comment, token)
            future_to_token[future] = token

        for future in as_completed(future_to_token):
            try:
                result = future.result()
                print(result)  # Print the result of the comment attempt
                if "SUCCESSFULLY" in result:
                    comments_count += 1
            except Exception as e:
                print(f"Error processing token: {e}")

    print(f"Total comments made: {comments_count}")

def comment_with_token(post_id, comment, access_token):
    """Comment on a Facebook post using the provided access token."""
    
    # Split the token in case it includes 'uid|access_token' format
    if '|' in access_token:
        _, access_token = access_token.split('|', 1)
    
    # Now check if the token starts with 'EA' or 'EAA'
    if not access_token.startswith(("EA", "EAA")):
        return f"Invalid token: {access_token}"
    
    try:
        converted_link = post_id
        auto_comment_url = f'https://graph.facebook.com/v13.0/{converted_link}/comments'
        params = {
            'message': comment,
            'access_token': access_token
        }
        time.sleep(1)  # Sleep for 1 second between comments
        headers = {
            'user-agent': W_ueragnt()  # Use the random user agent
        }
        response = requests.post(auto_comment_url, params=params, headers=headers)
        
        # Print status code and response for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if response.status_code == 200:
            return f"\033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY COMMENTED: {green}{comment}\033[1;32m"
        else:
            return f"\033[1;31m[FAILED]\033[1;31m FAILED TO COMMENT: {green}{comment} "

    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"


def perform_comment_fast():
    """Perform comments based on user input for file choice, starting line, post link, and number of comments."""
    
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {yellow}[1] {green}FRA ACCOUNT 
     {yellow}[2] {green}FRA PAGES
     {yellow}[3] {green}RPW ACCOUNT
     {yellow}[4] {green}RPW PAGES
     {red}[0] {red}EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        file_choice = int(input(f"     {green}Choose: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the given line
    
    # Step 4: Ask for the post ID
    a = input(f"    {green}Enter the post ID: ")
    post_id = extract_ids(a)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    # Step 5: Ask how many comments and get the list of comments
    try:
        num_comments = int(input(f"    {red}Enter the number of comments: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if num_comments <= 0:
            print("Number of comments must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    comments_list = []
    for i in range(num_comments):
        comment = input(f"    {green}Enter comment {i + 1}: ")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        comments_list.append(comment)

    # Step 6: Ask how many accounts to use for commenting
    try:
        num_accounts = int(input(f"   {green}Enter the number of accounts to use for commenting (1 to {len(tokens)}): "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"Please enter a valid number between 1 and {len(tokens)}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 7: Perform comments using multithreading
    results = []
    comments_count = 0
    max_workers = 15  # Set the maximum number of threads
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        for i, token in enumerate(tokens[:num_accounts]):
            comment = random.choice(comments_list)  # Randomly pick a comment
            future = executor.submit(comment_with_token, post_id, comment, token)
            future_to_token[future] = token

        for future in as_completed(future_to_token):
            try:
                result = future.result()
                print(result)  # Print the result of the comment attempt
                if "SUCCESSFULLY" in result:
                    comments_count += 1
            except Exception as e:
                print(f"Error processing token: {e}")

    print(f"Total comments made: {comments_count}")

# Execute the function


# Execute the function

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed



def load_tokens(file_path):
    """Load tokens from the specified file."""
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
        return tokens
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return []

def follow_and_like_facebook_page(uid, access_token):
    """Follow and like a Facebook page/profile using the given UID and access token."""
    follow_url = f"https://graph.facebook.com/v20.0/{uid}/subscribers"
    headers = {'Authorization': f'Bearer {access_token}'}
    
    # Perform the follow action
    follow_response = make_http_request('POST', follow_url, headers=headers)
    if follow_response and 'error' in follow_response:
        print(f"Error following page with UID {uid}: {follow_response['error']['message']}")
    elif follow_response:
        print(f"\033[1;32m[SUCCESSFULLY] FOLLOWED the page/profile with UID {uid}\033[0m")

    # Perform the like action
    like_url = f"https://graph.facebook.com/v20.0/{uid}/likes"
    like_response = make_http_request('POST', like_url, headers=headers)
    if like_response and 'error' in like_response:
        print(f"Error liking page with UID {uid}: {like_response['error']['message']}")
    else:
        print(f"\033[1;32m[SUCCESSFULLY] LIKED the page/profile with UID {uid}\033[0m")

def make_http_request(method, url, headers=None, data=None):
    """Make an HTTP request."""
    try:
        if method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data)
        elif method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        else:
            print(f"Unsupported HTTP method: {method}")
            return None

        if response.status_code == 200:
            return response.json()
        else:
            print(f"HTTP request failed with status code: {response.status_code}")
            return response.json()
    except Exception as e:
        print(f"An error occurred during the HTTP request: {str(e)}")
        return None

def perform_actions_from_file():
    """Main function to manage the follow and like actions based on user input."""
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    
    clear_screen()
    jovan()
    
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 1: Load tokens and display the total
    tokens = load_tokens(file_path)
    total_tokens = len(tokens)
    
    if total_tokens == 0:
        print("No tokens available from the selected file.")
        return

    

    # Step 2: Ask for the starting line
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {total_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > total_tokens:
            print(f"Please enter a valid line number between 1 and {total_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Adjust the tokens based on the starting line
    tokens = tokens[start_line - 1:]

    # Step 3: Get the page ID
    uid = input(f"    {green}Enter the Page/Profile UID: ").strip()
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    if not uid.isdigit():
        print("Invalid UID. Please ensure you entered a correct numeric UID.")
        return

    # Step 4: Get the number of actions
    try:
        num_actions = int(input(f"    {green}LIMIT {red}(not exceeding {total_tokens}): ").strip())
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if num_actions > total_tokens:
            print(f"It exceeds the limit of {total_tokens}.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for the actions.")
        return

    # Step 5: Perform actions using multithreading
    action_count = 0
    tasks = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        for token in tokens[:num_actions]:  # Limit the tokens to the number of actions requested
            future = executor.submit(follow_and_like_facebook_page, uid, token.split('|')[1])  # Assuming token format is email|access_token
            tasks.append(future)
            action_count += 1

        # Wait for all tasks to complete
        for task in as_completed(tasks):
            try:
                task.result()  # To raise any exceptions if occurred during execution
            except Exception as e:
                print(f"An error occurred during execution: {str(e)}")

    print(f"{green}\nSUCCESSFULLY FOLLOWED AND LIKED | ID:", uid)
    print(f"Completed {action_count} requested actions.")

# Call the method to execute the functionality
import requests
import sys
import time
from concurrent.futures import ThreadPoolExecutor

gome_token = []

def tokz(input_cookies):
    for cookie in input_cookies:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass

def shar():
    clear_screen()
    jovan()
    input_cookies = input(f"     {green}Enter Cookie:  \x1b[38;2;233;233;233m").split(',')
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    id_share = input(f"     {green}Enter Post ID: \x1b[38;2;233;233;233m")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    total_share = int(input(f"    {green}How Many Share: \x1b[38;2;233;233;233m"))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    delay = int(input(f"    {green} Delay Share: \x1b[38;2;233;233;233m"))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print('\x1b[38;2;173;255;47m[*] \x1b[38;2;233;233;233mwaiting...', end='\r')
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    all = tokz(input_cookies)
    total_live = len(all)
    print(f'\x1b[38;2;173;255;47mLive: \x1b[38;2;233;233;233m{total_live} \x1b[38;2;173;255;47mCookies')
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    if total_live == 0:
        sys.exit()

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    stt = 0

    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = []
        while True:
            for tach in all:
                if stt >= total_share:
                    break
                futures.append(executor.submit(share, tach, id_share))
                stt += 1
                print(f'\x1b[38;2;173;255;47mShare: + \x1b[38;2;233;233;233m{stt}', end='\r')
                time.sleep(delay)
            if stt >= total_share:
                break

    gome_token.clear()
    input('\x1b[38;2;173;255;47m[*] \x1b[38;2;233;233;233mEnter^^\033[0m')

import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan

import os
import random
import uuid

R = "\033[31m"  # Red
G = "\033[32m"  # Green
Y = "\033[33m"  # Yellow
B = "\033[34m"  # Blue
M = "\033[35m"  # Magenta
P = "\033[36m"  # Cyan
C = "\033[37m"  # White

def randc():
    return random.choice([R, G, Y, B, M, P, C])

def logo():
    rp(pan(f"""{randc()}
 ██████╗ ██████╗ 
██╔════╝██╔════╝ 
██║     ██║  ███╗
██║     ██║   ██║
╚██████╗╚██████╔╝
 ╚═════╝ ╚═════╝ 
                  """,
           title=f"{Y}COOKIE GETTER", subtitle=f"{R}DEVELOP BY JOVAN", border_style="bold purple"))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_file_path():
    clear_screen()
    jovan()
    return input(f"{C}(Enter path to file with email and password):~ ")
print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

def get_cookie_storage_path():
    return input(f"{C}(Enter path to store cookies):~ ")
print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

def read_credentials(file_path):
    credentials = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if '|' in line:
                uid, password = line.split('|')
                uid = uid.strip()
                password = password.strip()
                credentials.append((uid, password))
            else:
                print(f"Warning: Invalid format in line '{line}'. Skipping.")
    except FileNotFoundError as e:
        print(f"Error: File not found {file_path}: {str(e)}")
    
    print(f"Read {len(credentials)} credentials.")
    return credentials


def cuser(user, passw):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'cpl': 'true',
        'family_device_id': str(uuid.uuid4()),
        'credentials_type': 'device_based_login_password',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'method': 'auth.login',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
    }
    response = pt("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False)
    return response.json()

def runing():
    clear_screen()
    jovan()
    file_path = get_file_path()
    storage_path = get_cookie_storage_path()  # Get path for storing cookies
    credentials = read_credentials(file_path)

    if not credentials:
        print(f"{R}No credentials found in the file.")
        return

    print(f"{Y}Processing {len(credentials)} credentials...")

    for user, passw in credentials:
        response = cuser(user, passw)

        if "session_key" in response:
            clear()
            cookie_str = '; '.join(f'{i["name"]}={i["value"]}' for i in response.get('session_cookies', []))
            print(f"{G}USER ID/EMAIL: {C}{user}\n{G}PASSWORD: {C}{passw}\n{G}COOKIE: {C}{cookie_str}\n{G}ACCESS_TOKEN: {C}{response.get('access_token', 'Not available')}")
            
            with open(storage_path, 'a') as f:  # Use the user-defined path for storing cookies
                f.write(cookie_str + '\n')
        else:
            print(f"{R}INVALID/CHECKPOINT for USER ID: {C}{user}")

    print(f"{G}Processing complete. All credentials have been processed.")
import random
import requests
from colorama import init, Fore, Style
import os

# Initialize colorama
init()

class RegPro5:
    def __init__(self, cookies) -> None:
        self.cookies = cookies
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }
        
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text

        # Initialize fb_dtsg to None
        self.fb_dtsg = None
        
        # Try to find fb_dtsg using multiple patterns
        patterns = [
            '{"name":"fb_dtsg","value":"',  # Primary pattern
            ',"f":"',                      # Secondary pattern
            # Add more patterns if necessary
        ]

        for pattern in patterns:
            try:
                self.fb_dtsg = profile.split(pattern)[1].split('"},')[0]
                break  # Break if the pattern is found
            except IndexError:
                continue  # Try the next pattern

        if not self.fb_dtsg:
            kolor("Error: fb_dtsg not found in profile data.", 'red')

    def reg(self, name):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"' + name + '","page_referrer":"launch_point","actor_id":"' + self.id_acc + '","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)

        try:
            result = response.json()
            if 'id' in result:
                page_id = result['id']
                self.set_profile_picture(page_id)
            return result
        except:
            return response.text

    def set_profile_picture(self, page_id):
        picture_path = "/home/spade/Desktop/load data/Profile.jpeg"  # Replace with your actual path to the profile picture
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': f'https://www.facebook.com/{page_id}',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'ProfilePicUpload',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        files = {
            'source': (os.path.basename(picture_path), open(picture_path, 'rb'), 'image/jpeg')
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            'profile_id': page_id,
            'fb_dtsg': self.fb_dtsg,
            'photo_source': '4',
            'composer_entry_time': '0',
            'composer_session_id': 'abc',
            'ref': 'timeline',
            'upload_id': 'profile_pic',
            'upload_type': 'profile',
        }

        response = requests.post('https://www.facebook.com/photos/upload', headers=headers, files=files, data=data)

        try:
            return response.json()
        except:
            return response.text

# Function to print colored text
def kolor(text, color):
    if color == 'green':
        print(Fore.GREEN + text + Style.RESET_ALL)
    elif color == 'red':
        print(Fore.RED + text + Style.RESET_ALL)
    else:
        print(text)

def get_cookies_file_path():
    clear_screen()
    jovan()
    return input("Enter the path to the cookies.txt file: ")

def hackezr():
    
    cookies_file = get_cookies_file_path()

    try:
        with open(cookies_file, 'r') as f:
            cookies_list = f.readlines()
    except FileNotFoundError:
        kolor("Error: File not found. Please check the path.", 'red')
        return

    for cookie_line in cookies_list:
        cookie_line = cookie_line.strip()  # Remove leading/trailing whitespace

        # For your provided format, no need to split further; just use the entire line as cookies
        cookies = cookie_line

        vietnamese_names = [
            "Kim Tricia",
"Jerald Deocampo",
"Vincentius Hollister",
"Althea Mae Quarteros",
"Anthony Quarteros",
"Mary Ann Limpajan",
"Daisy Anito",
"Felisa Bolilawa Quarteros",
"Rossel Olaguer",
"Yohanne Quarteros",
"Alman Manlaunan",
"Ranilo Bolilawa",
"JB Guitar Clinic",
"Rome Espeon",
"Ibcp Pag Asa Kapalong",
"Freyah Beatrice B. Gambito",
"Sam Ting Wong",
"Bolilawa Nars",
"Cedenio Ampalid",
"Romel Bermejo",
"Lanie Puralan Bolilawa",
"Ja Ryd",
"Cristine May Limpajan",
"Charice Minor",
"Dohna Alejan Dalura",
"Tatum Abejuela",
"Loriene Myko Batuigas Matao",
"Grace Caparos Pablo",
"Noemie Ann Bacalso",
"Agua Collec Tions",
"Tetzkie ArteCraft",
"Honey Castelo Camporedondo",
"Ailene Bacus Bacalso",
"Mcjayz Bulz",
"Kathryn Bolilawa",
"PJ Balisalisa",
"Love LY",
"Lanie Malinao Magtubo",
"Jezzel Aiko Escote Palma",
"Maria Maffi Khalifa",
"Jonnel Bulilawa Jayagan",
"Arch Jean",
"Lea Gail Benaning",
"November Neriza Ang",
"Ethel Jane Rosillo",
"Ka Rhyn Bautista",
"Yocalub Enehpesoj",
"Christina Cosina Procurato",
"Majara Khouri Marzonia",
"Cj Andrews",
"Sa Ra",
"Meryam Misoles Balt",
"N�v� J��n P�Li�s",
"Christine Maeh",
"Christie Jean Villanueva Ganiera",
"Jessa Mendoza Salac",
"Rhoda Valenzuela",
"Michelle Baguio-Tanio Baldueza",
"Jay-ar Vistas Bolilawa",
"Estanislao Pasion III",
"Lynzkie Sabac Prudente Rmt",
"Mary Rose Masiga",
"Dawn Quarteros",
"Tristan Tejada Torralba",
"Jemma Palabrica Deadio",
"Honeybee Fortuna Villafuerte-Hidalgo",
"Charlene Joy Alcarez Bitangga",
"Jessi Jess",
"Jerah Mae Boquila",
"Ghia Tics",
"Jesryl R. Layson",
"Nellie Waro",
"Toni Basio",
"Mekaii Sh�ne",
"Angelix Vinoya",
"Jesza Amainah Pamplona",
"Rodelyn Joy Caverte - Cabale",
"Arlez Alicia Hojilla",
"Robert Uy",
"Doriza Mae Royo Dubb",
"Christine Socorin Boquila",
"Jash Jamalul",
"Janet Monares",
"Chaii Xiarah",
"Joy Len Ellan",
"Rowena Bolilawa Dumanayos",
"Leahlyn Chua",
"Jill Palma",
"Rosas Sa Palasyo",
"Dave Tupino Padrones",
"Ayiesha Monica D. HidaLgo",
"Queen Ann Alternado",
"Janeth Ordaneza-Rotersos Tenido",
"Charlene Jean Taduran",
"Hennessy De Guzman",
"Vievien Serenio",
"Marlyn Jean Banguiz Talon",
"C Glenn Bajade",
"Rejen P. Dacles",
"Em Em Garcia Grabato",
"Grace Samar",
"Jus Tine XD",
"Trixie Lectawa",
"Lanie Leyte",
"Cai",
"Mary Jane Baquino Ranque",
"Christine Karen D Quilario",
"Sarang Claveria Kim",
"Belljoe Aguinaldo",
"Vanessa Rose",
"Downa Downa",
"Hannah Aguspina Abrasaldo",
"Klydel Salanga",
"Yerffoj Ralliv Otibla",
"Jaysamae Lagulos Dianon",
"Thalia May Rojas Brock",
"Fritzie Dela Pena",
"Gimelle Bano Latoreno",
"Jeners Rabino",
"Mae Sabuero Quilla",
"Jedel Ordaneza Genotivo",
"Pau Ganiera",
"Jobert Rubio Abarico",
"Eugene Daga-ang",
"Myrelle Alex Estrada - Cubero",
"Aqshol Gilbus",
"Aprilyn Mae T. Taganahan",
"Rr R. Suela",
"Carla Iayns Gentiles",
"Jho Mansujeto",
"Jeffrey Dumanayos",
"Camela Tan",
"Ching Solis",
"Timmy Genyoung",
"Chari Mae Lacaba",
"Yhun Ri Joy",
"Liziel Quimzo",
"Nicandro Dujali",
"Deniece Anne Ramos Babiera",
"Christine Moralla",
"Michelle Sugaste",
"Myka Angela Bautista Dasas",
"Regine Litob Cerbolles",
"Caryl Iyns",
"Young Sil Demeray Capoy",
"Jamie Angelica Gutierrez Saraum",
"LadyGay Brei",
"Gemgil Oani",
"Marson Estabillo Muegna",
"Joy Cee",
"Deveyvon Lupos Espinosa",
"Kath O. Nebran Cabulao",
"MaRose Rebote",
"Mimi Arrocena",
"Gay Ann Jomarie Duque",
"Cha Chang Ley",
"Sheila Mae Niniel",
"Michael John Claro",
"Cristy Mifa",
"Vanessa Madrigal",
"Mary Blaze",
"Pasion Sara Lee",
"Junnell U Selim",
"Mae Rabe",
"Renren Manaran",
"Jason Mark C Yee",
"Nesciel Braza Olden",
"Inatay Dinna",
"Cj Mirafuentes",
"Jowelyn Obedo Robilla-Bulahan",
"Zhel Dahunog Jaictin - Caramol",
"Julie-Ann Ca�ete Tingson",
"Haydee Amar Guiret",
"Shy-aRa Alonzo-Garcia Caballes",
"Ivy Ditomal Aringoy",
"Che Dee",
"Domactol JaSon Bolilawa",
"Everly Duran",
"Mickie Jimenez Balinggao",
"Regine",
"Norly Norie Kim",
"Jovie Jane Lomocso Villalino",
"Roxan Hinay",
"Ar Yinkai Consencino",
"Patrice Nicole",
"Jyrah Cams",
"Fel Jun Talili",
"Erlyn Flores Maestre",
"Yhumme Villaflor Soberano",
"Furio Vincent Mark",
"Rebecca Bastasa Econar",
"Cha Avila Kita",
"Hermelyn Bastasa-Salang Lpt",
"Joycie Maniwang Bentulan",
"Riva Jean Tesoro Taganait",
"Jimmy Madulara Sonajo",
"Gonzaga Abella Cris",
"Queen Tejada Nabong",
"Dee Nette",
"Marjorie Jane Apatan Cerna",
"Jovy Ann Alicame",
"Revie Galapon",
"Cheryl Ann Felio",
"Alona Jane Mollanida Pidraroja-Leorna",
"Twff Nezyl",
"Angelica Briones Candido",
"Haniff Royo",
"Kazel Limpag",
"John Dave B Permangil",
"Rona Joy Alegado Egalan",
"Johanna Kasandra Galano",
"Anastacio Jr Esperada",
"Enanaj Guangco Patanao",
"Kenneth Joy Surdilla",
"Chloe Jane Claro",
"Mai Ya",
"Joseph Rabe Bumaat",
"Karla Justine Letada",
"Babe-Lorie Roy Ampit",
"AJ Murillo",
"Esguerra Julius Ceazar Abelilla",
"Jcamelia Gocela",
"Whenday Fermiza Galgo",
"Ily Morales",
"Hj Dela Rosa",
"Kit Vendiola Pasuquin",
"Ruby Carlos",
"Carelle Angela Letada",
"ACuh CXi Dianne",
"Mitzie Figuracion",
"Juvy Jane Paalisbo",
"Shaira Alegre",
"Klin Calo",
"Hannah Mendoza",
"Jaycel Orogo",
"Gel Eroy",
"Jane Bilbao",
"Charlene Jean Pangomlayen Kalaw",
"Steve Carl",
"ROy Pueblas",
"Velly Grace Pacoma",
"Rojilyn Legaspi Persigas",
"Lawrence Oliver Gambong Rabino",
"Miya Ugay",
"Anaflor Quarteros",
"Eloisa Jane Laurente",
"Anne Cuento",
"Lovely Joy Dongiapon",
"Grace Cabanig",
"Donald James Cordero",
"Jaan E Adaa",
"Aireen Jean Ramos",
"Raiz Maps",
"Therese Litob",
"Arar Auceran Rapal",
"Anbu Hanzo New",
"Nerahk Ramos",
"Mary Glaine Saguing Bravo",
"Ryan Palitoc",
"Irene Mae Romero-Godmaling Haberle-Villaram",
"Ayen Sta Maria Celestino",
"Harren Rose Talotalo Rosas",
"Je Miel Sala-um",
"Jorleen Lopez Salvador",
"Sarah Mae Enriquez Porquiado",
"Ramjoy Conlas Dominguez",
"Jeil Marie Romay",
"Jeany Parcon Biason",
"Ritchell Manlang Dequinto",
"Ge Ne Va",
"Razel Manuales De Leon",
"Joemarie Rendon",
"Sarjane Brigole Pana",
"Ranji Jimlani Taclob Ramos",
"Joan Manlang",
"Cheenee Mae Rabuya Abella",
"Juhla Mae E. Fernandez",
"Merz Valenton",
"Charlene Dorothy Dela Cruz",
"Karen Cabasag Jamorol",
"Ghiz Awing Almedora",
"Kathleen Kathie",
"Janny Batallones",
"Donalyn Balisa Recona",
"Alvin Roda",
"Maria Emalyn Morandante Redoble",
"Perly V. Cutamora",
"Jonah S. Tibagong",
"Crlyn Dljr Lao",
"Hazel Trimidal Arcala",
"Mary Cris Acquiatan",
"Bhebepril Magbanua Diano",
"Mitch Manos",
"Maria Jeanneth Panos",
"Carla Legaspi-Falco",
"Kyle Redaniel",
"Avatat Avatat",
"Louie Neth Grace Belo-Peralta",
"John Reyann Cunahap Compuesto",
"Lythelle Almonicar-Ramos",
"Anna Robles Peralta",
"Richelle Cast",
"Charmaine Jane Sagot",
"Ian Ceneza",
"Villapana Shaina",
"Joey Bolilawa",
"Joy Suan",
"Cherry Ching Vinculado Agosto",
"Rhea Mea Awalilob Manlang",
"Jayson Baldos",
"Shina Mansueto - Brasile�o",
"Rail Radz",
"HOoa Iix Iia",
"Jennevive Suarez Manlawe Lpt",
"Kap Romel Beldua",
"Judy Ramos",
"Khryz Thia Milgar",
"Jeth Mark",
"RJ Wenceslao Gesulga Castardo",
"Aicrag Enaj",
"Zandra Cunahap",
"Regine Lumacang Generalao",
"Ricky Suson",
"Kin Saligumba",
"Tiffany Xu",
"Remedios Ruguian Ubaldo",
"Honey Grace S. Bacalso",
"Emmalyn Sisneros Menorias",
"Amor Pillo",
"Maria Jemina Andersen",
"Bridgette Eve Selim Tamparong",
"Gretchen Balaga",
"Zane Baliog",
"Hammiel Onia Agustin",
"Jangskie Awalilob",
"Alex",
"Den Khrexiah Jzianly",
"Debby Espina Diansay",
"Eva Mae Ingar",
"Shiarah Zernia Gaile",
"Charise Supnet",
"Genevieve Ni�eza Jitotowani",
"Dowend Quilla",
"Jodelle John",
"Lakatuv Gutnuv",
"Meme D. Babao",
"Jhey Bolilawa",
"Erwin Ea",
"Jay Son",
"Novie Puralan Bolilawa",
"Charlene Jean Gwapa Montoya",
"Razel Luarez",
"Domactol MJ",
"Jairah Rafael Landanganon",
"Johnrey Bulilawa",
"Analezele Jaycel Culintas",
"Jason Salcedo",
"Jinalyn Bolilawa",
"Marjorie Orocio Abella",
"Maria Elena Cosido Supot",
"Elealeh Suan",
"Glaiza Mae Panes Latoza",
"Joy Garciano Bolilawa",
"Naizhel Faith",
"Dacel Love Loreto Hinayon",
"KhEm PT Broke",
"Kazekage Fendi Emblem",
"Lencejoy Amba",
"Fritz Frances Abe Bolilawa",
"Jesel Smith",
"Maryell Madulara Aleria",
"Asatsab Nylanej",
"Rick Tor",
"Maelyn L. Briones",
"Julie Rose Gamo",
"Ako Si Gee",
"Eednac Zerimar Loromaj",
"Peng Kay",
"Julie Ann Abella Dinolan",
"Joar Tatoy Bulacoy",
"Michael James Paul Latoza-Casas",
"Aileen Ansaldo",
"Maria Leah Parallag Estanda",
"Chessa Estilloso",
"Dovey Lovey Beejoy"
        ]

        random_name = random.choice(vietnamese_names)

        reg_instance = RegPro5(cookies)
        result = reg_instance.reg(random_name)

        if 'error' not in result:
            kolor("[SUCCESS] Created Page", 'green')
        else:
            kolor("[UNSUCCESSFUL] Created Page", 'red')
           


import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan

import os
import random
import uuid

R = "\033[31m"  # Red
G = "\033[32m"  # Green
Y = "\033[33m"  # Yellow
B = "\033[34m"  # Blue
M = "\033[35m"  # Magenta
P = "\033[36m"  # Cyan
C = "\033[37m"  # White

def randc():
    return random.choice([R, G, Y, B, M, P, C])

def logo():
    rp(pan(f"""{randc()}
 ██████╗ ██████╗ 
██╔════╝██╔════╝ 
██║     ██║  ███╗
██║     ██║   ██║
╚██████╗╚██████╔╝
 ╚═════╝ ╚═════╝ 
                  """,
           title=f"{Y}COOKIE GETTER", subtitle=f"{R}DEVELOP BY JOVAN", border_style="bold purple"))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_file_path():
    clear_screen()
    jovan()
    return input(f"     {green}{C}(Enter path to file with email and password):~ ")
print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

def get_cookie_storage_path():
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    return input(f"     {yellow}{C}(Enter path to store cookies):~ ")
print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

def read_credentials(file_path):
    credentials = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        password = None
        for line in lines:
            line = line.strip()
            if line.startswith('password:'):
                password = line.split(':')[1].strip()
            elif line:
                if password:
                    credentials.append((line, password))
                else:
                    print("Warning: Found user ID before any password.")
    except FileNotFoundError as e:
        print(f"Error: File not found {file_path}: {str(e)}")
    
    print(f"Read {len(credentials)} credentials.")
    return credentials

def cuser(user, passw):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'cpl': 'true',
        'family_device_id': str(uuid.uuid4()),
        'credentials_type': 'device_based_login_password',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'method': 'auth.login',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
    }
    response = pt("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False)
    return response.json()

def runing():
    clear_screen()
    jovan()
    file_path = get_file_path()
    storage_path = get_cookie_storage_path()  # Get path for storing cookies
    credentials = read_credentials(file_path)

    if not credentials:
        print(f"{R}No credentials found in the file.")
        return
     
    print(f"{Y}Processing {len(credentials)} credentials...")

    for user, passw in credentials:
        response = cuser(user, passw)

        if "session_key" in response:
            clear()
            cookie_str = '; '.join(f'{i["name"]}={i["value"]}' for i in response.get('session_cookies', []))
            print(f"{G}USER ID/EMAIL: {C}{user}\n{G}PASSWORD: {C}{passw}\n{G}COOKIE: {C}{cookie_str}\n{G}ACCESS_TOKEN: {C}{response.get('access_token', 'Not available')}")
            
            with open(storage_path, 'a') as f:  # Use the user-defined path for storing cookies
                f.write(cookie_str + '\n')
        else:
            print(f"{R}INVALID/CHECKPOINT for USER ID: {C}{user}")

    print(f"{G}Processing complete. All credentials have been processed.")

# Run main() only when script is executed directly
def bitz():
    clear_screen()
    jovan()
    print(f"     {yellow}[1] {green}Add cookie")
    print(f"     {yellow}[2] {green}Auto create page")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    num_reactions = int(input(f'     {red}Enter Option: '))

    if num_reactions == 1:
        runing()
    elif num_reactions == 2:
        hackezr() # Placeholder for further implementation
    else:
        print(f"{R}Invalid option selected.")


import requests
import os
import random
import time

BASE_URL = 'https://graph.facebook.com/v18.0'
DIRECTORY = 'Picture'

def pigzs(access_token):
    url = f'{BASE_URL}/me/accounts'
    params = {
        'access_token': access_token
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error getting pages for token {access_token}: {str(e)}")
        return []

def pec(page_id):
    url = f'{BASE_URL}/{page_id}?fields=picture'
    try:
        response = requests.get(url)
        response.raise_for_status()
        picture_data = response.json().get('picture', {})
        return 'data' in picture_data and 'url' in picture_data['data']
    except requests.exceptions.RequestException as e:
        print(f"Error checking profile picture for page {page_id}: {str(e)}")
        return False

def plod(page_id, page_access_token, file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {
                'source': file
            }
            data = {
                'access_token': page_access_token
            }
            url = f'{BASE_URL}/{page_id}/picture'
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error uploading profile picture to page {page_id}: {str(e)}")
        return {'error': str(e)}
    except FileNotFoundError as e:
        print(f"Error: File not found {file_path}: {str(e)}")
        return {'error': str(e)}

def rad(file_path):
    tokens = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "Access Token:" in line:
                    token = line.split('Access Token:')[1].strip()
                    tokens.append(token)
    except FileNotFoundError as e:
        print(f"Error: Tokens file not found {file_path}: {str(e)}")
    return tokens
import requests
import json
import sys
import os
import platform
import re

class Color:
    END = '\033[0m'
    BOLD = '\033[1m'



def pzl(username, passwords):
    url_base = "https://b-api.facebook.com/method/auth.login"
    device_id = "0ksqyflb-tnnh-aaag-j5si-gqof920ps1lo"
    sim_serials = '["89014103210593510720"]'
    locale = "en_US"
    client_country_code = "US"

    for password in passwords:
        url = f"{url_base}?format=json&device_id={device_id}&email={username}&password={password}&cpl=true&family_device_id={device_id}&sim_serials={sim_serials}&credentials_type=password&error_detail_type=button_with_disabled&locale={locale}&client_country_code={client_country_code}&method=auth.login&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            responses = response.json()
            if 'access_token' in responses:
                return responses['access_token'], True
            else:
                error_msg = responses.get('error_msg', 'Unknown error')
                print(f"Error for {username}: {error_msg}")
        except requests.exceptions.RequestException as e:
            print(f"Error for {username}: {str(e)}")
    
    return None, False

def lodza(token_file_path):
    """Load data from the specified token file."""
    try:
        with open(token_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"access_tokens": []}
    return data

def sav(data, token_file_path):
    """Save data to the specified token file."""
    with open(token_file_path, 'w') as file:
        json.dump(data, file, indent=4)

def prz(file_path, tokens_array):
    """Process the file and extract tokens for uid|pass format."""
    if not os.path.isfile(file_path):
        print(f"{Color.BOLD}File {file_path} does not exist.{Color.END}")
        return

    print(f"{Color.BOLD}Processing file: {file_path}{Color.END}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        print(f"{Color.BOLD}File {file_path} is empty.{Color.END}")
        return

    # Read uid|pass format lines
    account_pairs = [line.strip() for line in lines if '|' in line]

    if not account_pairs:
        print(f"{Color.BOLD}No valid uid|pass pairs found in {file_path}.{Color.END}")
        return

    for account in account_pairs:
        uid, password = account.split('|')
        print(f"{Color.BOLD}[✦] Attempting to log in with {uid}{Color.END}")
        token, success = pzl(uid, [password])  # Using the password as a single element list
        if success:
            tokens_array.append({"email": uid, "access_token": token})
        else:
            print(f"{Color.BOLD}Failed to get token for {uid}.{Color.END}")

# The rest of the code remains unchanged


def kitok(tokens_array, token_file_path):
    """Function to add access tokens.""" 
    data = lodza(token_file_path)
    access_tokens = data.get("access_tokens", [])

    for token_info in tokens_array:
        email = token_info["email"]
        access_token = token_info["access_token"]
        
        # Check if the token already exists
        if any(token.get("access_token") == access_token for token in access_tokens):
            print(f"Token already exists for email: {email}")
            continue
        
        try:
            # Verify the token
            response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
            if response.status_code == 200:
                is_valid_token = True
                
                # Fetch associated pages
                pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
                if pages_response.status_code == 200:
                    pages_data = pages_response.json().get("data", [])
                   
                    # Prepare token data
                    account_data = {"email": email, "access_token": access_token}
                    account_pages = [page for page in pages_data]
                    account_data["pages"] = account_pages
                    access_tokens.append(account_data)
                    data["access_tokens"] = access_tokens
                    
                    print("\033[91mSuccessfully added Account\033[0m")  # Successfully added message in red
            else:
                is_valid_token = False
        except requests.exceptions.RequestException:
            is_valid_token = False

        if not is_valid_token:
            print(f"Invalid token for email: {email}")

    sav(data, token_file_path)

def maz():
    """Display the main menu and handle user choices.""" 
    clear_screen()
    jovan()
    file_path = input(f"{yellow}Enter the path of the text file with accounts and passwords: ").strip()
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    token_file_path = input(f"{yellow}Enter the path of the file where tokens should be stored: ").strip()
    

    tokens_array = []

    prz(file_path, tokens_array)

    if tokens_array:
        print(f"{Color.BOLD}Collected Tokens:{Color.END}")
        for token_info in tokens_array:
            print(f"Email: {token_info['email']}, Access Token: {token_info['access_token']}")
        
        # Call add_token with the collected tokens and specified token file path
        kitok(tokens_array, token_file_path)
    else:
        print(f"{Color.BOLD}No tokens collected.{Color.END}")

    print("Exiting the program...")

def start():
    clear_screen()
    jovan()
    token_file_path = input("Enter the path to the file containing the tokens: ").strip()
    
    tokens = rad(token_file_path)
    if not tokens:
        print("No tokens found. Exiting.")
        return

    if not os.path.exists(DIRECTORY):
        print(f"Error: Directory '{DIRECTORY}' does not exist.")
        return

    files_in_directory = os.listdir(DIRECTORY)
    if not files_in_directory:
        print(f"Error: No files found in directory '{DIRECTORY}'.")
        return

    for user_token in tokens:
        pages = pigzs(user_token)
        if not pages:
            print(f"No pages found for token {user_token}. Skipping.")
            continue

        for page in pages:
            print(f"Page Name: {page['name']} - Page ID: {page['id']}")
            page_id = page['id']
            page_access_token = page.get('access_token')

            if not page_access_token:
                print(f"No access token found for page {page_id}. Skipping.")
                continue

            # Check if the page already has a profile picture
            if pec(page_id):
                print(f"Page {page['name']} already has a profile picture. Skipping upload.")
                continue

            # Randomly select a file from the directory
            file_name = random.choice(files_in_directory)
            file_path = os.path.join(DIRECTORY, file_name)

            result = plod(page_id, page_access_token, file_path)
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            print(f"    {green}SUCCESSFULLY UPLOADED PROFILE PICTURE {page['name']}")
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            # Add a delay between requests to avoid hitting rate limits
            time.sleep(2)  # Adjust delay as needed

def mainzsa():
    clear_screen()
    jovan()
    print("[1] GET TOKEN")
    print()
    print("[2] SET PFP")
    print("\033[1;37m───────────────────────────────────────────────────────────────\033")
    choice = input("Enter: ")
    if choice == '1':
        maz()
    if choice == '2':
        start()
    else: 
        print("invalid po")
        clear_screen()

import requests
import random
import string
import os

CODE_FILE = '/sdcard/boostphere/generated_code.txt'  # File to store the generated code

def generate_code():
    """Generate a unique code in the format JAHIDXFOLLOWS-XXX-XXXXX."""
    prefix = "JAHIDXFOLLOWS"
    number_part = ''.join(random.choices(string.digits, k=3))  # 3 random digits
    letters_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  # 5 alphanumeric characters
    code = f"{prefix}-{number_part}-{letters_part}"
    return code

def save_code(code):
    """Save the generated code to a file."""
    with open(CODE_FILE, 'w') as file:
        file.write(code)

def load_code():
    """Load the code from the file, if it exists."""
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE, 'r') as file:
            return file.read().strip()
    return None

def is_code_approved(code):
    """Check if the generated code is approved by fetching the approval list."""
    try:
        response = requests.get("https://raw.githubusercontent.com/testerz559/Approval/refs/heads/main/Approval")
        response.raise_for_status()  # Raise an error for bad responses
        approved_codes = response.text.splitlines()  # Split the response into lines
        
        # Remove comments and strip whitespace, then check for the code
        approved_codes = [line.split('#')[0].strip() for line in approved_codes if line]
        return code in approved_codes  
    except requests.RequestException as e:
        print(f"Error fetching the approval list: {e}")
        return False

def main():
    
    print("Main function is running...")

def generate_and_check_code():
    """Generate a code if not existing, check if it's approved, then run main()."""
    code = load_code()
    
    if code is None:
        code = generate_code()
        save_code(code)
        print(f"{green}Generated Code: {code}")
    else:
        print(f"{green}Loaded Code: {code}")

    if is_code_approved(code):
        
        main()
    else:
        print(f"{red}CODE IS NOT APPROVE PLS SEND IT TO {yellow}https://www.facebook.com/profile.php?id=100078043222260")
def main():
    fraaccounts_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    frapages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpwaccounts = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpwpages = '/sdcard/boostphere/RPWPAGES.txt'
    total_accounts, total_pages = count_tokens(fraaccounts_file, frapages_file)
    total_account_rpw, total_pages_rpw = count_tokens(rpwaccounts,rpwpages)
    jovan()
    print(f"""                 {lightblue}OVERVIEW OF STORED ACCOUNT & PAGES💫
          
                            {blue}FRA ACCOUNT{yellow} : {green}{total_accounts}
                            {blue}FRA PAGES  {yellow} : {green}{total_pages}
                            {blue}RPW ACCOUNT{yellow} : {green}{ total_account_rpw}
                            {blue}RPW PAGES  {yellow} : {green}{total_pages_rpw}
      {blue}───────────────────────────────────────────────────────────────\033[0m""")
    print(f"                          {green} Services We Offer✨                               ")
    print(f"      {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"           {red}[01]  {red}ADD ACCOUNTS")
    print(f"           {yellow}[02]  {blue}REACT TO POST             {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[03]  {blue}REACT TO REELS            {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[04]  {blue}REACT TO GROUP POST       {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[05]  {blue}REACT TO POST[VID & PHOTO]{yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[06]  {blue}AUTO FOLLOW               {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[07]  {blue}AUTO REACT TO DP & POST   {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[08]  {blue}AUTO COMMENT              {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[09]  {blue}AUTO LIKE & FOLLOW PAGE   {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[10]  {blue}AUTO SHARE [VIA COOKIE]   {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[11]  {blue}AUTO REACT COMMENT        {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {yellow}[12]  {blue}AUTO REPLY COMMENT        {yellow}- {green}[PAGE & ACCOUNT]")
    print(f"           {red}[13] {red}RESET")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"                         {red}EXTRA TOOLS 🔥                                 ")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"           {yellow}[14] {blue}AUTO CREATE PAGE          {yellow}- {green}[PHB NAMES]")
    print(f"           {yellow}[15] {blue}AUTO SET PFP              {yellow}- {green}[RANDOM]")
    print(f"           {yellow}[16] {blue}CREATE FILE               {yellow}- {green}[RANDOM]")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {green}CHOICE: ").strip()         

    if choice == '1':
        mainmany()
    if choice == '2':
        perform_reaction_fast()
    if choice == '3':
        perform_reaction_reels()
    if choice == '4':
        perform_reaction_fast()
    if choice == '5':
        perform_reaction_fast_vid()
    if choice == '6':
        auto_follow_fast()
    if choice == '7':
        perform_reaction_fast_dp()
    if choice == '8':
        perform_comment_fast()
    if choice == '9':
        perform_actions_from_file()
    if choice == '10':
        shar()
    if choice == '11': 
        comment_react()
    if choice == '12': 
        reply()
    if choice == '13':
        clear_text_files()
    if choice == '14':
        bitz()
    if choice == '15':
        mainzsa()
    if choice == '16':
        createfile()
    else:
        print("Invalid choice, exiting.")
if __name__ == "__main__":
    main()
    
    
