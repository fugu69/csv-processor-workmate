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
    if not values:
        raise ValueError("Cannot aggregate empty list.")

    if operation == "avg":
        return sum(values) / len(values)
    elif operation == "min":
        return min(values)
    elif operation == "max":
        return max(values)
    else:
        raise ValueError(f"Unsupported aggregation operation: {operation}")


def parse_order_by(order_by_arg):
    if "=" not in order_by_arg:
        raise ValueError("Order-by format must be column=asc|desc")
    column, direction = order_by_arg.split("=")
    direction = direction.lower()
    if direction not in ("asc", "desc"):
        raise ValueError("Order direction must be 'asc' or 'desc'")
    return column.strip(), direction
