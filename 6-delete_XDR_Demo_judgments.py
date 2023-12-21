'''
    delete all XDR Demo judgements from z_judgements_id_list.txt file which contains judgment ids
    
    z_judgements_id_list.txt is created by 5-get_XDR_Demo_judgments.py
'''
import requests
import json
from crayons import cyan,green,red,yellow

def delete_judgements(access_token):
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    line_content = []
    with open('z_judgements_id_list.txt') as inputfile:
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
    delete_judgements(access_token)

if __name__ == "__main__":
    main()    