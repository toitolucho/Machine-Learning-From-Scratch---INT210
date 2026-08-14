import requests
import json

TOKEN = 'f0ca8d48a205bb9b8df847c979f99e49' 
MOODLE_DOMAIN = 'https://ecampus.usfx.bo'
ENDPOINT = f'{MOODLE_DOMAIN}/webservice/rest/server.php'

def call_moodle(function, params={}):
    params.update({
        'wstoken': TOKEN,
        'wsfunction': function,
        'moodlewsrestformat': 'json'
    })
    response = requests.post(ENDPOINT, data=params)
    return response.json()

def main():
    print("Fetching site info to check available functions...")
    info = call_moodle('core_webservice_get_site_info')
    
    if 'functions' in info:
        funcs = info['functions']
        print(f"Total functions available: {len(funcs)}")
        
        # Look for creation functions
        create_funcs = [f['name'] for f in funcs if 'create' in f['name'] or 'add' in f['name']]
        
        print("\nFunctions related to creation/adding:")
        for f in sorted(create_funcs):
            print(f" - {f}")
            
        print("\nAll other interesting functions (course/module/assign related):")
        other_funcs = [f['name'] for f in funcs if any(x in f['name'] for x in ['course', 'module', 'assign'])]
        for f in sorted(other_funcs):
            if f not in create_funcs:
                print(f" - {f}")
    else:
        print("No 'functions' list returned in site_info.")
        print("Keys returned:", info.keys())

if __name__ == "__main__":
    main()
