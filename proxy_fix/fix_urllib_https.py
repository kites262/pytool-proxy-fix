import os
import sys
import fileinput

def get_urllib_path():
    '''根据当前的 Python 环境获取 urllib 模块路径'''
    python_home = sys.prefix  # 这是 Python 环境的根目录
    urllib_path = os.path.join(python_home, 'Lib', 'urllib')
    
    # 检查 urllib 模块路径是否存在
    if os.path.exists(urllib_path):
        return urllib_path
    else:
        raise FileNotFoundError('Unable to locate the urllib module in the current Python environment.')

def fix_urllib_bug():
    '''修复 urllib.request.py 中的 'https' 改为 'http' 的 bug'''
    try:
        urllib_path = get_urllib_path()
        
        # 要修改的是 `request.py` 文件
        request_file_path = os.path.join(urllib_path, 'request.py')
        
        if not os.path.exists(request_file_path):
            raise FileNotFoundError(f'{request_file_path} does not exist.')
        
        bug_fixed = False
        bug_line_number = 0
        bug_line = ''
        
        # 使用 fileinput 修改文件内容
        with fileinput.FileInput(request_file_path, inplace=True, backup='.bak') as file:
            
            for line in file:
                # 查找并修改目标行
                if "proxies['https'] = 'https://%s' % proxyServer" in line:
                    line = line.replace('https://', 'http://')  # 修改 https 为 http
                    bug_fixed = True
                    bug_line_number = file.filelineno()
                    bug_line = line
                print(line, end='')
            
        if bug_fixed:
            print(f'Bug fix applied successfully in {request_file_path}')
            print(f'Backup file: {request_file_path}.bak')
            print(f'Fixed line#{bug_line_number}: \n---\n{bug_line.strip()}\n---')
        else:
            os.remove(f'{request_file_path}.bak')
            print(f'Bug fix not applied in {request_file_path}')
            print('That means the bug might have been fixed in the current environment.')
    except Exception as e:
        print(f'Error: {e}')

def main():
    '''主函数'''
    fix_urllib_bug()
