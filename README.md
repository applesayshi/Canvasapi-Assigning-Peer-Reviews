# Assigning Peer Review Scripts

## Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Additional Notes](#additional-notes)
- [Limitations](#limitations)
- [Acknowledgements](#acknowledgements)

## Overview 

This Python script has two functions. 


---

## Requirements

1. **General Repository Requirements**  
   Ensure you have completed all Setup Requirements as documented on our [Knowledge Base](https://isit.air.arts.ubc.ca/?p=16867)

2. **Required Python Packages:**
    - canvasapi
    - datetime
    - re
    - collections

---

## Usage

1. **Information Needed** 
    To run this script, only the Course code, and the quiz code are needed. 

2. **Run the script** 
    Run the function by inputting the course code and quiz code: `make_printable_quiz(course_code, quiz_code)`. The script will print messages to the console indicating the file has been generated.

3. **Review the Output**  
    The Output file will be saved in the **downloads** folder. The file will be named `printable_quiz.html`.

4. **Open the file in a Browser**
    Open the file in a browser (Chrome, Edge, Firefox, etc) and print the page with ctrl + p

5. **Printing Settings**
    In the printing pop-up window, open up the Advance settings/More settings drop down, and *Deselect* the "Headers and Footers" option. This option will be enabled by default.

## Additional Notes

- The script only works on **Classic Quizzes**. New Quizzes has its own built in quiz printing method in Canvas. 

## Limitations

- The script is unable to display images from Kaltura due to access issues

### Best Practices 


- **Testing:** It's recommended to test the script if its your first time using it either on Canvas Beta or using a SB.

---

## Acknowledgements 

This script was developed for use in Arts ISIT by Bryan Sun

 