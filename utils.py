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

def parse_aggregate(agg_arg):
    if "=" not in agg_arg:
        raise ValueError("Aggregate format must be column=operation")
    column, operation = agg_arg.split("=")
    return column.strip(), operation.strip()

def aggregate(values, operation):
    if operation == "avg":
        return sum(values) / len(values) if values else 0
    elif operation == "min":
        return min(values) if values else None
    elif operation == "max":
        return max(values) if values else None
    else:
        raise ValueError(f"Unsupported aggregate operation: {operation}")
