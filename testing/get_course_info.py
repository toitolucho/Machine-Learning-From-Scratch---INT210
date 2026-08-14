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
    course_id = 761
    assignment_id = 416982
    
    print(f"Fetching information for course ID: {course_id}...")
    course_info = call_moodle('core_course_get_courses_by_field', {
        'field': 'id',
        'value': course_id
    })
    print(json.dumps(course_info, indent=2))
    
    print(f"\nFetching assignment information for course ID: {course_id}...")
    assign_info = call_moodle('mod_assign_get_assignments', {
        'courseids[0]': course_id
    })
    
    # Alternatively get course contents which includes modules
    print(f"\nFetching course contents for course ID: {course_id}...")
    contents = call_moodle('core_course_get_contents', {
        'courseid': course_id
    })
    
    # Try to find the assignment in the response
    found_assign = False
    if 'courses' in assign_info:
        for course in assign_info['courses']:
            for assign in course.get('assignments', []):
                if assign['id'] == assignment_id or assign['cmid'] == assignment_id:
                    print(f"\nFound specific assignment {assignment_id} in mod_assign_get_assignments:")
                    print(json.dumps(assign, indent=2))
                    found_assign = True
                    break

    if type(contents) == list:
        for section in contents:
            for module in section.get('modules', []):
                if module.get('id') == assignment_id or module.get('instance') == assignment_id:
                    print(f"\nFound specific assignment {assignment_id} in core_course_get_contents:")
                    print(json.dumps(module, indent=2))
                    found_assign = True

    if not found_assign:
        print(f"\nAssignment {assignment_id} not explicitly found in the expected places. Might be another module type or not exist in this course.")

if __name__ == "__main__":
    main()
