name_list = ["Peter", "John", "James"]
salary_list = [40000, 50000, 70000]
bonus_percent = ["10.25%", "8%", "12.3%"]

bonus_data = dict(zip(name_list,
             [salary * coeff / 100 for (salary, coeff) in
              dict(zip(salary_list, list(map(lambda s: float(s.replace("%", "")), bonus_percent)))).items()]))

print(bonus_data)