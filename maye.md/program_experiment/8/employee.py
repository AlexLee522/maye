class employee:
    def __init__(self, time, salary):
        self.time = time
        self.salary = salary
    @staticmethod
    def total_salary(time, salary):
        return time*salary
    def get_time(new_time):
        time = new_time
        return time
    def get_salary(new_salary):
        salary = new_salary
        return salary


emp_num = int(input('how many employees?'))
i = 0
s = 0
t = []
while i < emp_num:
    time = int(raw_input('NO.'+str(i)+' employee\'s work time:'))
    salary = int(raw_input('NO.'+str(i)+' employee\'s salary:'))
    a = employee.total_salary(time, salary)
    print 'NO.'+str(i)+' employee\'s total salary is %d ' % a
    s += a
    i += 1
    t.append(int(a))
for i in range(emp_num):
    if t[i] > s/emp_num:
        print 'NO.'+str(i)+' employee is excellent'
    
    
    
