def shutdown(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

# Example usage
print(shutdown("yes"))
print(shutdown("no"))
print(shutdown("abc"))