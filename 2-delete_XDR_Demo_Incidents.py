'''
    delete all incidents from z_incidents_id_list.txt file which contains incidents ids
    
    z_incidents_id_list.txt is created by the 1-get_XDR_Demo_incidents.py
'''
import requests
import json
from crayons import cyan,green,red,yellow

#access_token = 'eyJhbGciO....bPito5n5Q' # Truncated example
def delete_incidents(access_token):
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    line_content = []
    with open('z_incidents_id_list.txt') as inputfile:
    	for line in inputfile:
    		line_content.append(line.strip())
    for url in line_content:
        print (green(url,bold=True))
        response = requests.delete(url, headers=headers)
        print()
        print (yellow(response,bold=True))  

def main():
    fa = open("ctr_token.txt", "r")
    access_token = fa.readline()
    fa.close()   
    delete_incidents(access_token)

if __name__ == "__main__":
    main()    