class Worker:
    def __init__(self, worker_num: int, fname: str, lname: str, 
                 work_experience_company: int, total_years_experience: int, 
                 salary: float, age: int):
        self.Worker_num = worker_num
        self.Fname = fname
        self.Lname = lname
        self.Work_experience_company = work_experience_company
        self.Total_years_experience = total_years_experience
        self.Salary = salary
        self.Age = age

    def worker_information(self):
        return f"num: {self.Worker_num}, fname: {self.Fname}, 
        lname: {self.Lname}, exp in company: {self.Work_experience_company}, 
        total exp: {self.Total_years_experience}, salary: {self.Salary}, age: {self.Age}"
    def salary_bonus(self):
        if self.Work_experience_company < 5:
            return self.Salary * 0.005
        elif self.Work_experience_company > 10:
            return self.Salary * 0.02
        else:
            return self.Salary * 0.015

def search_by_num(wks: list[Worker], num):
    for w in wks:
        if w.Worker_num == num:
            return True
    return False

def search_by_name_experience(wks: list[Worker], name, comp_exp):
    for w in wks:
        if w.Fname == name and w.Work_experience_company == comp_exp:
            print(w.worker_information())

def add_worker(wks: list[Worker], w: Worker):
    wks.append(w)

def remove_worker(wks: list[Worker], num):
    for w in wks:
        if w.Worker_num == num:
            wks.remove(w)
            print("Information deleted!")
    print("Wrong worker_num!")

workers_list = [] 

# command = input()
# if command == "add":
#     num = int(input())
#     fname = input()
#     lname = input()
# elif command == "remove":
# elif command == "search by number":
# elif command == "search by name":