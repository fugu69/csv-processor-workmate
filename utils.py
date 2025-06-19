def parse_condition(condition):
    for op in [">=", "<=", ">", "<", "="]:
        if op in condition:
            column, value = condition.split(op)
            return column.strip(), op, value.strip()
    raise ValueError("Invalid condition format. Use column>value etc.")

def compare(a, b, operator):
    if operator == ">":
        return a > b
    elif operator == "<":
        return a < b
    elif operator == "=":
        return a == b
    elif operator == ">=":
        return a >= b
    elif operator == "<=":
        return a <= b
    else:
        raise ValueError("Unsupported operator")
