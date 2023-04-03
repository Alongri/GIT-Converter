"""
***********************************
     Author: Alon Gritsovsky
     Welcome to GIT Converter
***********************************
"""
import xml.etree.ElementTree as ET
import os
import shutil
import glob


"""
inputs of: the project name and campaign to replace
"""
print("******************************************")
print("****** Welcome to GIT Converter  *********")
print("******************************************")
project_name = input("Enter the project name: ")
campaign_path = input("Enter the campaign path: ")

"""
Copy the campaign and all tests and procedures
"""
campaign = "C:\\QA\\autotester_tools\\AutoTester_Campaigns\\"+project_name
tests = "C:\\QA\\autotester_tools\\AutoTester_TestCases\\"+project_name
procedures = "C:\\QA\\autotester_tools\\AutoTester_Procedures\\"+project_name



# Create the new folder
os.mkdir(campaign)
os.mkdir(tests)
os.mkdir(procedures)


# Create a list of all tests
list_of_tests = []
tree = ET.parse(campaign_path)
root = tree.getroot()
titles = root.findall('testCases/testCase')
for title in titles:
  file_attribute = title.get('file')
  list_of_tests.append(file_attribute)


#Check duplicates of tests
filenames = [os.path.basename(test) for test in  list_of_tests]
filename_to_path = {filename: test for filename, test in zip(filenames,  list_of_tests)}
unique_filenames = list(set(filenames))
updated_list_of_tests = [filename_to_path[filename] for filename in unique_filenames]


# Copy the test files
for test in updated_list_of_tests:
  shutil.copy(test, tests)
  print(f'{test} copied to {tests}')

def copy_deeper_procedures(x):
    tree = ET.parse(x)
    root = tree.getroot()
    procedure_elements = tree.findall('.//procedure')
    if len(procedure_elements) > 0:
        for include_elem in procedure_elements:
            include_path = include_elem.get('path')
            list_of_procedures.append(include_path)
            copy_deeper_procedures(include_path)

# Create a list of all procedures
list_of_procedures = []
for test in updated_list_of_tests:
    tree = ET.parse(test)
    root = tree.getroot()
    for proc in tree.findall('.//procedure'):
        path_attribute = proc.get('path')
        list_of_procedures.append(path_attribute)
        copy_deeper_procedures(path_attribute)


# Copy procedures that located in campaign file
tree = ET.parse(campaign_path)
root = tree.getroot()
for proc in tree.findall('.//procedure'):
    path_attribute = proc.get('path')
    list_of_procedures.append(path_attribute)
    copy_deeper_procedures(path_attribute)


#Check duplicates of procedures
filenames = [os.path.basename(procedure) for procedure in  list_of_procedures]
filename_to_path = {filename: procedure for filename, procedure in zip(filenames,  list_of_procedures)}
unique_filenames = list(set(filenames))
updated_list_of_procedures = [filename_to_path[filename] for filename in unique_filenames]


# Copy the procedure files
for procedure in updated_list_of_procedures:
  shutil.copy(procedure, procedures)
  print(f'{procedure} copied to {procedures}')

# Copy the campaign file
shutil.copy(campaign_path,campaign)
print(f'{campaign_path} copied to {campaign}')



"""
replacing all the tests,procedures in this Campaign
"""

#replacement of the location of the tests in the campaign file
campaign_filename = os.path.basename(campaign_path)
new_campaign_path = campaign +"\\"+ campaign_filename
tree = ET.parse(new_campaign_path)
root = tree.getroot()
titles = root.findall('testCases/testCase')
for title in titles:
  file_attribute = title.get('file')
  index =  file_attribute.rfind("\\")
  tests_location_before =  file_attribute[:index]
  replacer = file_attribute.replace(tests_location_before,tests)
  title.set('file', replacer)
tree.write(new_campaign_path, encoding='utf-8', xml_declaration=True)


#replacement of the location of the procedures in tests files
tests_path = glob.glob(os.path.join(tests, '*.attc'))
for file_name in tests_path:
    tree = ET.parse(file_name)
    root = tree.getroot()
    procedure_elements = tree.findall('.//procedure')
    for proc in procedure_elements:
        path_attribute = proc.get('path')
        index = path_attribute.rfind("\\")
        procedure_location_before = path_attribute[:index]
        replacer = path_attribute.replace(procedure_location_before, procedures)
        proc.set('path', replacer)
    tree.write(file_name, encoding='utf-8', xml_declaration=True)


#replacement of the location of the procedures in procedures files
procedure_path = glob.glob(os.path.join(procedures, '*.atap'))
for file_name in procedure_path:
    tree = ET.parse(file_name)
    root = tree.getroot()
    procedure_elements = tree.findall('.//procedure')
    if len(procedure_elements) > 0:
        for proc in procedure_elements:
            path_attribute = proc.get('path')
            index = path_attribute.rfind("\\")
            procedure_location_before = path_attribute[:index]
            replacer = path_attribute.replace(procedure_location_before, procedures)
            proc.set('path', replacer)
        tree.write(file_name, encoding='utf-8', xml_declaration=True)
    path_attribute = root.get("path")
    index = path_attribute.rfind("\\")
    procedure_location_before = path_attribute[:index]
    replacer = path_attribute.replace(procedure_location_before, procedures)
    root.set("path", replacer)
    tree.write(file_name, encoding='utf-8', xml_declaration=True)


#replace all procedures in the campaign
tree = ET.parse(new_campaign_path)
root = tree.getroot()
procedure_elements = tree.findall('.//procedure')
if len(procedure_elements) > 0:
    for proc in procedure_elements:
        path_attribute = proc.get('path')
        index = path_attribute.rfind("\\")
        procedure_location_before = path_attribute[:index]
        replacer = path_attribute.replace(procedure_location_before, procedures)
        proc.set('path', replacer)
    tree.write(new_campaign_path, encoding='utf-8', xml_declaration=True)
else:
    print('The campaign file does not contain any procedure elements.')



print("*****************************************************************")
print("***** The file transfer process was completed successfully ******")
print("*****************************************************************")

























