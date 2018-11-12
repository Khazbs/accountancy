from data import employees, salaries

lupa = employees.get("Лупа")
pupa = employees.get("Пупа")

lupa_salary = salaries.get("Лупа")
pupa_salary = salaries.get("Пупа")

lupa.pay(lupa_salary)
pupa.pay(pupa_salary)
