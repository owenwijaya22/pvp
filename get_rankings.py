import json
import requests

def get_border(example):
        length = len(example)
        return '-' * length

def get_inputs():
    cp_cap_example = 'Example: 500, 1500, 2500'
    cup_type_example = 'Example: hisui, little, great, ultra'
    role_example = 'Example: overall, leads, chargers, attackers'    

    cp_cap = input(f'{cp_cap_example}\n{get_border(cp_cap_example)}\nCp cap?: ')

    cup_type = input(f'\n{cup_type_example}\n{get_border(cup_type_example)}\nCup type?: ')

    if cup_type == 'great' or cup_type == 'ultra' or cup_type == 'master':
        cup_type = 'all'

    role = input(f'\n{role_example}\n{get_border(role_example)}\nRole?: ')

    return cp_cap, cup_type, role

class PvpBot:
    def __init__(self, cp_cap, cup_type, role):
        self.cp_cap = cp_cap
        self.cup_type = cup_type
        self.role = role

    def build_url(self):
        search_url = f'https://pvpoke.com/data/rankings/{self.cup_type}/{self.role}/rankings-{self.cp_cap}.json?v=1.29.3.3'
        return search_url
        
    def get_response(self, search_url):
        headers = {'user-agent': 'vscode-restclient'}
        response = requests.get(search_url, headers=headers)
        print(response.status_code)
        return response

    def save_response(self, response):
        with open(f'./data/{self.cp_cap}_{self.cup_type}_{self.role}.json', 'w') as file:
            json.dump(response.json(), file, indent=4)

def main():
    cp_cap, cup_type, role = get_inputs()
    Bot = PvpBot(cp_cap, cup_type, role)
    search_url = Bot.build_url()
    print(search_url)
    response = Bot.get_response(search_url)
    Bot.save_response(response)

if __name__ == "main":
    main()