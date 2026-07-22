import string

def check_password_strength(password):
    # 1. Evaluate conditions
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    # Check for symbols using Python's built-in punctuation list
    symbols = string.punctuation
    has_symbol = any(char in symbols for char in password)
    
    # 2. Count how many criteria are met
    criteria = [length_ok, has_upper, has_digit, has_symbol]
    score = sum(criteria)
    
    # 3. Determine strength result
    # Short passwords (less than 8 characters) are automatically weak
    if not length_ok or score <= 2:
        strength = "Weak"
        advice = "Make it at least 8 characters long and mix in numbers, symbols, and capitals."
    elif score == 3:
        strength = "Medium"
        advice = "Good start! Add more variety (like symbols or uppercase) to make it stronger."
    else:  # score == 4
        strength = "Strong"
        advice = "Great job! Your password meets all security criteria."

    return strength, advice

# --- Simple Interactive CLI ---
if __name__ == "__main__":
    user_password = input("Enter a password to test: ")
    result, tip = check_password_strength(user_password)
    
    print(f"\nPassword Strength: {result}")
    print(f"Feedback: {tip}")