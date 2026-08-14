import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# ================= CONFIGURATION =================
# 1. Paste your key from "Claves de seguridad" here
# TOKEN = '179539aa8205ed0a428a0977cf6ea032' --usfx

TOKEN = os.environ.get('MOODLE_TOKEN')

#TOKEN = '7a2e06de3d20b346658ba9e75a919e34'  # postgrado

# 2. Configuration based on your links
MOODLE_DOMAIN = os.environ.get('MOODLE_DOMAIN', 'https://ecampus.usfx.bo')
#MOODLE_DOMAIN = 'https://aulasvirtuales.usfx.bo/tecnologia'
COURSE_ID = 1413          # From your course link
CM_ID_FROM_URL = 410653   # From your assignment link (view.php?id=XXXX)

# ================= THE SCRIPT =================
ENDPOINT = f'{MOODLE_DOMAIN}/webservice/rest/server.php'

def call_moodle(function, params={}):
    """Helper to send requests to Moodle"""
    params.update({
        'wstoken': TOKEN,
        'wsfunction': function,
        'moodlewsrestformat': 'json'
    })
    try:
        response = requests.post(ENDPOINT, data=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return None

def main():
    print("--- 🕵️‍♂️ MOODLE API DIAGNOSTIC ---")

    # STEP 1: Test the Token
    print(f"\n1. Testing Token on {MOODLE_DOMAIN}...")
    user_info = call_moodle('core_webservice_get_site_info')
    
    if not user_info or 'exception' in user_info:
        print("❌ Failed. The token might be invalid or lacks permissions.")
        if user_info: print(f"   Moodle says: {user_info.get('message')}")
        return

    print(f"✅ Success! Logged in as: {user_info.get('fullname')} (User ID: {user_info.get('userid')})")

    # STEP 2: Find the Real Assignment ID
    # The ID in the URL (401975) is the "Course Module ID". 
    # The API needs the "Instance ID". We have to find it.
    print(f"\n2. Searching for Assignment details in Course {COURSE_ID}...")
    course_content = call_moodle('core_course_get_contents', {'courseid': COURSE_ID})
    
    real_assign_id = None
    assign_name = None

    if course_content and 'exception' not in course_content:
        # Loop through all sections and modules to find our assignment
        for section in course_content:
            for module in section.get('modules', []):
                if module.get('id') == CM_ID_FROM_URL:
                    real_assign_id = module.get('instance')
                    assign_name = module.get('name')
                    print(f"✅ Found it! Module '{assign_name}'")
                    print(f"   - URL ID (CMID): {CM_ID_FROM_URL}")
                    print(f"   - Real DB ID (Instance): {real_assign_id} <--- We need this one")
                    break
            if real_assign_id: break
    
    if not real_assign_id:
        print("❌ Could not find the assignment in the course content. Check the IDs.")
        if course_content and 'exception' in course_content:
            print(f"   Error: {course_content.get('message')}")
        return

    # STEP 3: Try to Fetch Submissions
    print(f"\n3. Testing permission to read submissions for '{assign_name}'...")
    submissions_data = call_moodle('mod_assign_get_submissions', {'assignmentids[0]': real_assign_id})

    if submissions_data and 'assignments' in submissions_data:
        submissions = submissions_data['assignments'][0]['submissions']
        count = len(submissions)
        print(f"✅ SUCCESS! Access granted.")
        print(f"   Found {count} submissions for this assignment.")
        
        if count > 0:
            print("   First student submission found:", submissions[0].get('status'))
            # This proves we can download the files later!
    else:
        print("❌ Failed to fetch submissions.")
        if submissions_data: print(f"   Moodle says: {submissions_data.get('message')}")
        print("   (This usually means the Token exists but doesn't have 'Teacher' rights or the specific capability)")

if __name__ == "__main__":
    main()