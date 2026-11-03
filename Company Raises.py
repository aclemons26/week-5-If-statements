data = [1121, "Jackie Grainger", 22.22,
        1122, "Jignesh Thrakkar", 25.25,
        1127, "Dion Green", 28.75, False,
        24.32, 1132, "Jacob Gerber",
        "Sarah Sanderson", 23.45, 1137, True,
        "Brandon Heck", 1138, 25.84, True,
        1152, "David Toma", 22.65,
        23.75, 1157, "Charles King", False,
        "Jackie Grainger", 1121, 22.22, False,
        22.65, 1152, "David Toma"]

# Step 2-3: Programmatically parse into unique database-like dicts (no duplicates)
employees = {}

def try_add(emp_id, name, wage):
    if emp_id is not None and name is not None and wage is not None and emp_id not in employees:
        employees[emp_id] = {
            "employee_id": emp_id,
            "name": name,
            "hourly_wage": round(float(wage), 2)
        }

i = 0
n = len(data)
while i < n:
    if i + 2 < n:
        a, b, c = data[i], data[i+1], data[i+2]
        # id, name, wage
        if isinstance(a, int) and isinstance(b, str) and isinstance(c, float):
            try_add(a, b, c)
            i += 3
            if i < n and isinstance(data[i], bool):
                i += 1
            continue
        # wage, id, name
        if isinstance(a, float) and isinstance(b, int) and isinstance(c, str):
            try_add(b, c, a)
            i += 3
            continue
        # name, wage, id
        if isinstance(a, str) and isinstance(b, float) and isinstance(c, int):
            try_add(c, a, b)
            i += 3
            if i < n and isinstance(data[i], bool):
                i += 1
            continue
    if i + 3 < n:
        a, b, c, d = data[i], data[i+1], data[i+2], data[i+3]
        # name, id, wage, bool
        if isinstance(a, str) and isinstance(b, int) and isinstance(c, float) and isinstance(d, bool):
            try_add(b, a, c)
            i += 4
            continue
        # name, wage, id, bool
        if isinstance(a, str) and isinstance(b, float) and isinstance(c, int) and isinstance(d, bool):
            try_add(c, a, b)
            i += 4
            continue
    i += 1

# Convert to sorted list of dictionaries
employee_list = sorted(employees.values(), key=lambda x: x["employee_id"])

# Step 4: Add total_hourly_rate (hourly_wage * 1.3)
for emp in employee_list:
    emp["total_hourly_rate"] = round(emp["hourly_wage"] * 1.3, 2)

# Step 5: underpaid_salaries (total_hourly_rate between 28.15 and 30.65)
underpaid_salaries = [
    emp for emp in employee_list
    if 28.15 <= emp["total_hourly_rate"] <= 30.65
]

# Step 6: Calculate raises based on hourly_wage (not total)
company_raises = []
for emp in employee_list:
    rate = emp["hourly_wage"]
    if 22 <= rate < 24:
        pct = 0.05
    elif 24 <= rate < 26:
        pct = 0.04
    elif 26 <= rate < 28:
        pct = 0.03
    else:
        pct = 0.02
    raise_amount = round(rate * pct, 2)
    company_raises.append({
        "name": emp["name"],
        "raise": raise_amount
    })

# Step 7: Print all three lists
print("=== Employee List (with total_hourly_rate) ===")
for emp in employee_list:
    print(emp)

print("\n=== Underpaid Salaries ===")
for emp in underpaid_salaries:
    print(emp)

print("\n=== Company Raises ===")
for raise_info in company_raises:
    print(raise_info)
    