from data import employees, salaries

lupa = employees.get("Лупа")
pupa = employees.get("Пупа")

lupa_salary = salaries.get("Лупа")
pupa_salary = salaries.get("Пупа")

lupa.pay(pupa_salary)
pupa.pay(lupa_salary)
