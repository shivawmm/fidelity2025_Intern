# Name: Shivam Singh
# Email: shivamsingh181002@outlook.com
# Phone: 6307008497



# solution 2
import re
def extract_valid_emails(text):
    pattern = r"\b[a-zA-Z][a-zA-Z0-9]*@[a-zA-Z]+\.(com|in|net|uk)\b"
    emails = [match.group() for match in re.finditer(pattern, text)]
    return emails

txt = "I know a set of email addresses that we can extract using expression1: abc.df@somecompany.co.uk, abc@gmail.com, xyz.ab@tpa.com, dfg.gh@dp.cp.net . But what about 11.234.abc.ghy@tp.edu, let's check."
valid_emails = extract_valid_emails(txt)
print("Valid emails are: ",valid_emails)




# solution 3
import os
class TextFileFinder:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    def find_text_files(self):
        if not os.path.isdir(self.folder_path):
            raise ValueError(f"Invalid folder path: {self.folder_path}")
        
        text_files = [f for f in os.listdir(self.folder_path) if f.endswith('.txt')]
        return text_files
    
finder = TextFileFinder("C:/Users/Shivam Singh/OneDrive/Desktop/Fidelity/Shivam_Assessment_week1")
print(finder.find_text_files())




# solution 5
# django folder is present in the folder




# solution 7
class Employee:
    def __init__(self, name, emp_id, dept):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept

class Department(Employee):
    def __init__(self, name, emp_id, dept, deptname, departid):
        super().__init__(name, emp_id, dept)
        self.deptname = deptname
        self.departid = departid

    def dsp(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Department Name: {self.deptname}")

dept = Department("Shivam", 123, "Engineering", "Software Development", 456)
dept.dsp()





# solution 11
def read_trans(file_path):
    successful_trans = []
    pending_trans = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            if len(parts) == 3:
                trans_date = parts[0]
                trans_id = parts[1]
                trans_status = parts[2]

                if trans_status == 'S':
                    successful_trans.append((trans_date, trans_id))
                elif trans_status == 'P':
                    pending_trans.append((trans_date, trans_id))
    return successful_trans, pending_trans

file_path = "C:/Users/Shivam Singh/OneDrive/Desktop/Fidelity/Shivam_Assessment_week1/data1.txt"
successful_trans, pending_trans = read_trans(file_path)
print("\nSuccessful Transactions:")
for date, trans_id in successful_trans:
    print(f"Date: {date}, ID: {trans_id}")
print("\nPending Transactions:")
for date, trans_id in pending_trans:
    print(f"Date: {date}, ID: {trans_id}\n")

