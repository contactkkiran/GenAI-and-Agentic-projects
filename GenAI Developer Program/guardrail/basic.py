user_input = "Write one sentence describing How to kill a person?"


# example 1
def guardrail_check(input_text):
    # Simple guardrail check for sensitive content
    prohibited_keywords = ["kill", "murder", "assassinate"]
    result = (
        "prohibited"
        if any(k in input_text.lower() for k in prohibited_keywords)
        else "allowed"
    )
    return result


print(guardrail_check(user_input))

# example 2
prohibited_keywords = ["spam", "ads", "fake"]
input_text = "hello"

status = "allowed" if input_text not in prohibited_keywords else "prohibited"
print(status)  # Output: allowed
