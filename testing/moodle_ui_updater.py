import os
import json
import time
import getpass
from playwright.sync_api import sync_playwright

MOODLE_DOMAIN = 'https://ecampus.usfx.bo'
LOGIN_URL = f'{MOODLE_DOMAIN}/login/index.php'

def get_credentials():
    username = os.environ.get('MOODLE_USERNAME')
    password = os.environ.get('MOODLE_PASSWORD')
    
    if not username:
        username = input("Enter your Moodle Username: ")
    if not password:
        password = getpass.getpass("Enter your Moodle Password: ")
        
    return username, password

def run_automation():
    # Load configuration
    try:
        with open('assignments.json', 'r', encoding='utf-8') as f:
            assignments = json.load(f)
    except FileNotFoundError:
        print("Error: assignments.json not found!")
        return

    username, password = get_credentials()

    with sync_playwright() as p:
        # Launch browser in non-headless mode so we can see what's happening
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        print(f"Logging in to {LOGIN_URL}...")
        page.goto(LOGIN_URL)
        
        # Fill in login credentials
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        
        # Click login if we haven't been redirected yet
        if "login/index.php" in page.url:
            submit_btn = page.locator('button[type="submit"]')
            if submit_btn.is_visible():
                submit_btn.first.click()

        # Check if login was successful
        page.wait_for_load_state('networkidle')
        if "login/index.php" in page.url:
             print("Login failed. Please check your credentials.")
             browser.close()
             return
             
        print("Login successful!")

        for item in assignments:
            item_id = item['moodle_item_id']
            edit_url = f"{MOODLE_DOMAIN}/course/modedit.php?update={item_id}"
            
            print(f"\nProcessing Assignment: {item['title']} (ID: {item_id})")
            print(f"Navigating to {edit_url}")
            page.goto(edit_url)
            page.wait_for_load_state('networkidle')
            
            # 1. Set the Description
            print("Updating description...")
            # Moodle often uses the Atto editor which is a contenteditable div
            editor_locator = page.locator('.editor_atto_content')
            if editor_locator.is_visible():
                # Clear existing and fill new
                editor_locator.fill("")
                # Use evaluate to set HTML content safely
                editor_locator.evaluate(f"el => el.innerHTML = '{item['description']}'")
            else:
                # Fallback if plain text editor or another editor is used
                print("Atto editor not found, looking for standard textarea...")
                page.fill('textarea[name="introeditor[text]"]', item['description'])

            # 2. Upload the File Attachment
            if item.get('attachment_path') and os.path.exists(item['attachment_path']):
                print(f"Uploading file: {item['attachment_path']}")
                
                # Click the "Add..." button in the file manager
                add_button = page.locator('a[title="Agregar..."]')
                if not add_button.is_visible():
                    # Fallback selector for the add file button
                    add_button = page.locator('.fp-btn-add').first
                
                add_button.click()
                
                # Wait for the file picker modal to appear
                print("Waiting for file picker dialog...")
                page.wait_for_selector('.moodle-dialogue-base', state='visible', timeout=10000)
                
                # Click the "Upload a file" tab on the left
                print("Selecting upload tab...")
                upload_tab = page.locator('.fp-repo:has-text("Subir un archivo")')
                if not upload_tab.is_visible():
                     upload_tab = page.locator('.fp-repo:has-text("Upload a file")')
                if not upload_tab.is_visible():
                     upload_tab = page.locator('.fp-repo-upload') # fallback to original class
                
                upload_tab.first.click()
                
                # Wait for the file input to appear and set the file
                print("Setting file...")
                file_input = page.locator('input[type="file"]')
                file_input.wait_for(state='attached', timeout=5000)
                file_input.first.set_input_files(item['attachment_path'])
                
                # Click the "Upload this file" button
                print("Clicking upload button...")
                upload_btn = page.locator('button.fp-upload-btn')
                upload_btn.first.click()
                
                # Wait for upload to complete (modal disappears)
                print("Waiting for upload to complete...")
                page.wait_for_selector('.moodle-dialogue-base', state='hidden', timeout=30000)
                print("File uploaded successfully!")
            elif item.get('attachment_path'):
                print(f"WARNING: File not found at {item['attachment_path']}. Skipping upload.")

            # 3. Save and return to course
            print("Saving changes...")
            page.click('#id_submitbutton2') # "Save and return to course" button
            
            page.wait_for_load_state('networkidle')
            print(f"Successfully updated assignment: {item_id}")

        print("\nAll tasks complete! Closing browser in 5 seconds...")
        time.sleep(5)
        browser.close()

if __name__ == "__main__":
    run_automation()
