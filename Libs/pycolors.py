# 1.0
class pycolors:
    HEADER = '\033[95m' # Розовый
    YELLOW = '\033[33m' # Желтый
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'        # End color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Использование: colors.BOLD +
# from Libs.pycolors import pycolors
# colors = pycolors() # Создаем экземпляр класса pycolors
# print(f"Файл успешно очищен: {colors.YELLOW}{self.file_path}{colors.ENDC}")
