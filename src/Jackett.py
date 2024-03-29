import requests
import os
from requests.exceptions import Timeout
from utils import get_str_results

def search(query):

    params = (
        ('apikey', os.environ['jackett_api_key']),
        ('Query', query),
        #('Tracker[]',
        # ['eztv', 'idope', 'iptorrents', 'nyaasi', 'rarbg', 'rutracker-ru']),
        ('Category[]', [
            '2000', '2010', '2020', '2030', '2040', '2045', '2050', '2060',
            '2070', '5000', '5010', '5020', '5030', '5040', '5045', '5060',
            '5070', '5080'
        ]),
        #('_', '1587352225849'),
    )

    try:
        response = requests.get(os.environ['jackett_url'], params=params, timeout=(3, 20))
    except Timeout:
        return "Jackett timed out"
    except ConnectionError:
        return "Jackett didn't respond"
    except:
        return "Something went wrong"
    
    if response.ok:
        results = response.json()['Results']
        if len(results) > 0:
            return get_str_results(results)
        else:
            return "No results found"
    else:
        return response.status_code
