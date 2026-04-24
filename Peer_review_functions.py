## ------------ IMPORT PACKAGES --------------##
from canvasapi import Canvas
from datetime import datetime
import random

## ------------ INITIALIZE CANVAS OBJECTS ----------- ##
# Canvas API URL
API_URL = "https://ubc.test.instructure.com"
# Canvas API key
API_KEY = "11224~HkHHQmz4v2PCy6AXKauna42zfzFAEYwPWZxVCZzRE9YMQMPCWmwhKmv3rz7ewFXA"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

def intra_group_peer_review(course_id, assignment_id, group_name):

    ## ------------- INITIALIZE OBJECTS --------------- ##
    course = canvas.get_course(course_id)
    assignment = course.get_assignment(assignment_id)
    all_groups = course.get_group_categories()

    for group_cat in all_groups:
        if group_cat.name == f"{group_name}":
            groups = group_cat.get_groups()

            for group in groups:

                # List of users in a group
                # Nested in For loop, so this list is only 1 group at a time
                users = list(group.get_users())

                # skip small groups
                if len(users) < 2:
                    continue
                
                # assign each student the next student in the group
                for i in range(len(users)):
                    reviewer = users[i]
                    # Modulo operator
                    # Since lists are 0 indexed, index i + 1 <= len(users)
                    # Circles through the list so everyone has someone they are peer reviewing 
                    reviewee = users[(i + 1) % len(users)] 

                    submission = assignment.get_submission(reviewee.id)
                    submission.create_submission_peer_review(reviewer.id)

# NOTE: 
# - This is also a good way to assign peer reviews before students have any submissions
#
# - "This is a group assignment" setting must be enabled
# - "Require Peer Reviews" setting must be enabled
# - Only assigns 1 peer review per person
# - Overrides the peer review settings (assigning 0 people/person, manual or automatic, all does not matter with this script)
# - Because groups are pre-made, the assumption is that everyone is already in the same section, or else groups between sections would not exist


# intra_group_peer_review(160156, 2426687, "Bryan Test Group")



# If the course has multiple sections (For example, lab sections), and a large section for all students, we want to assign peer reviews only within each 
# NOTE: TOGGLE THE CANVAS SETTING 
def intra_section_peer_review(course_id, assignment_id):

    ## ------------- INITIALIZE OBJECTS --------------- ##
    course = canvas.get_course(course_id)
    assignment = course.get_assignment(assignment_id)
    sections = list(course.get_sections())

    # Number of students in the course
    enrollments = list(course.get_enrollments(type=["StudentEnrollment"]))

    num_students = len(enrollments)

    for section in sections:
        # List of users in a section

        users = []
        
        for enrollment in enrollments:
            if enrollment.course_section_id == section.id:
                users.append(course.get_user(enrollment.user_id))

        # Excludes the "main" section that includes all students, which is usually the case in most courses
        if len(users) == num_students:
            continue
                
        # skip small sections (realistically this never happens)
        if len(users) < 2:
            continue
                
        # assign each student the next student in the list
        for i in range(len(users)):
            reviewer = users[i]
            # Modulo operator
            # Since lists are 0 indexed, index i + 1 <= len(users)
            # Circles through the list so everyone has someone they are peer reviewing 
            reviewee = users[(i + 1) % len(users)] 

            submission = assignment.get_submission(reviewee.id)
            submission.create_submission_peer_review(reviewer.id)

# intra_section_peer_review(160156, 2426687)