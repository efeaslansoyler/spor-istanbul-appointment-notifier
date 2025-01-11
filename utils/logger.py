from datetime import datetime

def log_with_timestamp(message: str) -> None:
    """
    Prints a message with current timestamp
    
    Args:
        message: The message to be logged
    """
    print(f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] {message}")