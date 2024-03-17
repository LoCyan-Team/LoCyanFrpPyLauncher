import platform
import requests
import subprocess
import winreg
import zipfile


# 封装查询系统架构的函数
def get_system_architecture():
    try:
        key_name = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_name) as key:
            arch_value, _ = winreg.QueryValueEx(key, "PROCESSOR_ARCHITECTURE")
        return arch_value.lower()
    except Exception as err:
        print(f"不支持此架构: {err}")
        return None


# 检测系统架构并下载对应文件
def check_system_architecture():
    os_name = platform.system()
    arch_info = get_system_architecture()

    if os_name != "Windows" or arch_info is None:
        print("不支持的操作系统或无法获取处理器架构")
        return

    print(f"检测到系统环境是 {arch_info}，正在下载适用于 {arch_info} 的软件包...")
    requests.get(f"https://mirrors.nyanest.xyz/locyan/{arch_info}_windows.zip", stream=True)

    def unzip_file(zip_path, target_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(target_path)

    unzip_file(f'{arch_info}_windows.zip', './LoCyanPureFrp')


# 调用检查函数
check_system_architecture()
