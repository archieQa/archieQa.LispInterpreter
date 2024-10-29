import logging

# Setup logging configuration
logging.basicConfig(
    filename="interpreter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(message):
    logging.error(message)  # Log an error message

def log_evaluation(expression, result):
    logging.info(f"Evaluated {expression} to {result}")  # Log evaluation result
