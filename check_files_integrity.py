import sys
import os
import hashlib


HASH_ALGOS = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256
}


class InputFileNotFound(Exception):
    "Файл с входящими данными не найден" 
    pass

class ArgumentNotProvided(Exception):
    "Пользователь не предоставил необходимые stdin аргументы"
    pass


class Status:
    "Содержит возможные статусы проверки содержимого файла"
    OK: str = "OK"
    FAIL: str = "FAIL"
    NOT_FOUND: str = "NOT FOUND"
        
        
def get_parsed_list_of_files(path_to_list: str) -> list[list[str]]:
    """Читает из файла список значений имени файла, 
    алгоритма хэширования и хэш-суммы"""
    with open(path_to_list, 'r') as f:
        lines = f.readlines()
        
    return [line.strip().split() for line in lines]


def get_file_hash(full_path: str, algo_type: str) -> str:
    """Возвращает хэш-сумму содержимого файла"""
    with open(full_path, 'rb') as f:
        byte_content = f.read()
    
    return HASH_ALGOS.get(algo_type)(byte_content).hexdigest()


def output_msg(file_name: str, status: str) -> None:
    """Управляет сообщением stdout"""
    print(f"{file_name} {status}")


def main():
    if len(sys.argv) != 3:
        raise ArgumentNotProvided("\n\nProgram usage:\n<this script name>.py \
        <path to the input file> \
        <path to the directory containing the files to check>")
        
    _, path_to_input_file, path_to_files = sys.argv
    
    if not os.path.isfile(path_to_input_file):
        raise InputFileNotFound("Файл с хеш-суммами не найден")
    
    for file_info in get_parsed_list_of_files(path_to_input_file):
        
        file_name, algo_type, hash_sum = file_info
        path_to_file = os.path.join(path_to_files, file_name)
        
        if not os.path.isfile(path_to_file):
            output_msg(file_name, Status.NOT_FOUND)        
        elif hash_sum == get_file_hash(path_to_file, algo_type):
            output_msg(file_name, Status.OK)
        else:
            output_msg(file_name, Status.FAIL)
            
            
if __name__ == "__main__":
    main()