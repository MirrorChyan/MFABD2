from pathlib import Path
import shutil
import sys
import json
import re
import os  # 添加 os 模块用于文件遍历

from configure import configure_ocr_model

working_dir = Path(__file__).parent
install_path = working_dir / Path("install")
version = len(sys.argv) > 1 and sys.argv[1] or "v0.0.1"

def install_deps():
    if not (working_dir / "deps" / "bin").exists():
        print("Please download the MaaFramework to \"deps\" first.")
        print("请先下载 MaaFramework 到 \"deps\"。")
        sys.exit(1)

    shutil.copytree(
        working_dir / "deps" / "bin",
        install_path,
        ignore=shutil.ignore_patterns(
            "*MaaDbgControlUnit*",
            "*MaaThriftControlUnit*",
            "*MaaRpc*",
            "*MaaHttp*",
        ),
        dirs_exist_ok=True,
    )
    shutil.copytree(
        working_dir / "deps" / "share" / "MaaAgentBinary",
        install_path / "MaaAgentBinary",
        dirs_exist_ok=True,
    )

def convert_line_endings(file_path):
    """将文件的换行符统一转换为 Windows 格式 (CRLF)"""
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 统一转换为 CRLF
        content = content.replace('\r\n', '\n')  # 先标准化为 LF
        content = content.replace('\n', '\r\n')  # 再转换为 CRLF
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8', newline='\r\n') as f:
            f.write(content)
    except Exception as e:
        print(f"转换换行符失败: {file_path} - {str(e)}")

def install_resource():
    configure_ocr_model()

    # 复制整个 resource 目录
    shutil.copytree(
        working_dir / "assets" / "resource",
        install_path / "resource",
        dirs_exist_ok=True,
    )
    
    # 专门处理公告文件夹中的文件
    announcement_dir = install_path / "resource" / "Announcement"
    if announcement_dir.exists():
        print(f"处理公告文件: {announcement_dir}")
        # 遍历目录中的所有文件
        for root, _, files in os.walk(announcement_dir):
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() == '.md':  # 只处理 Markdown 文件
                    convert_line_endings(file_path)
                    print(f"已转换: {file_path}")

    # 复制并更新 interface.json
    shutil.copy2(
        working_dir / "assets" / "interface.json",
        install_path,
    )

    with open(install_path / "interface.json", "r", encoding="utf-8") as f:
        interface = json.load(f)
    
    # 1. 更新根版本字段
    interface["version"] = version
    
    # 2. 动态更新 custom_title 中的版本号
    if "custom_title" in interface:
        # 匹配 "MFABD2)" 后到 " | 游戏版本" 前的所有内容
        pattern = r"(?<=MFABD2\))(.*?)(?=\s*\|\s*游戏版本：)"
        
        # 确保有v前缀和空格
        display_version = f"v{version.lstrip('v')} "
        
        # 执行替换
        new_title = re.sub(
            pattern, 
            display_version,
            interface["custom_title"]
        )
        interface["custom_title"] = new_title

    with open(install_path / "interface.json", "w", encoding="utf-8") as f:
        json.dump(interface, f, ensure_ascii=False, indent=4)

def install_chores():
    shutil.copy2(working_dir / "README.md", install_path)
    shutil.copy2(working_dir / "LICENSE", install_path)
    shutil.copy2(working_dir / "LICENSE-APACHE", install_path)
    shutil.copy2(working_dir / "LICENSE-MIT", install_path)

def install_agent():
    shutil.copytree(
        working_dir / "agent",
        install_path / "agent",
        dirs_exist_ok=True,
    )

if __name__ == "__main__":
    install_deps()
    install_resource()
    install_chores()
    install_agent()
    print(f"Install to {install_path} successfully.")