import os

class CalculatorConfig:
    def __init__(self):
        # Load configurations from environment variables with fallback defaults.
        self.base_dir = os.getenv("CALCULATOR_BASE_DIR", ".")  # Default to current directory.
        self.max_history_size = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))
        self.auto_save = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
        self.precision = int(os.getenv("CALCULATOR_PRECISION", 10))
        self.max_input_value = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1e100))
        self.encoding = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
