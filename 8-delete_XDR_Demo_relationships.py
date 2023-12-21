'''
    delete all XDR Demo relationships from z_relationships_id_list.txt file which contains judgment ids
    
    z_relationships_id_list.txt is created by 7-get_XDR_Demo_relationships.py
'''
import requests
import json
from crayons import cyan,green,red,yellow

def delete_relationships(access_token):
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    line_content = []
    with open('z_relationships_id_list.txt') as inputfile:
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
    delete_relationships(access_token)

if __name__ == "__main__":
    main()    