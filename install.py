from pathlib import Path
import shutil
import sys
import json
import re  # 必须添加的导入

from configure import configure_ocr_model

working_dir = Path(__file__).parent
install_path = working_dir / Path("install")
version = len(sys.argv) > 1 and sys.argv[1] or "v0.0.1"

def install_deps():
    # ... 保持不变 ...

def install_resource():
    configure_ocr_model()

    shutil.copytree(
        working_dir / "assets" / "resource",
        install_path / "resource",
        dirs_exist_ok=True,
    )
    shutil.copy2(
        working_dir / "assets" / "interface.json",
        install_path,
    )

    with open(install_path / "interface.json", "r", encoding="utf-8") as f:
        interface = json.load(f)
    
    # 1. 更新根版本字段（原有逻辑）
    interface["version"] = version
    
    # 2. 动态更新 custom_title 中的版本号（优化版）
    if "custom_title" in interface:
        # 优化1：更智能的匹配模式
        # 匹配 "MFABD2)" 后到 " | 游戏版本" 前的所有内容
        pattern = r"(?<=MFABD2\))(.*?)(?=\s*\|\s*游戏版本：)"
        
        # 优化2：直接使用传入的版本号（自动处理v前缀）
        # 无需额外判断，直接使用传入的version
        
        # 执行替换：保留前后文本，只替换中间部分
        new_title = re.sub(
            pattern, 
            f"v{version.lstrip('v')} ",  # 确保有v前缀和空格
            interface["custom_title"]
        )
        interface["custom_title"] = new_title

    with open(install_path / "interface.json", "w", encoding="utf-8") as f:
        json.dump(interface, f, ensure_ascii=False, indent=4)

def install_chores():
    shutil.copy2(working_dir / "README.md", install_path)
    shutil.copy2(working_dir / "LICENSE", install_path)
    shutil.copy2(working_dir / "LICENSE-APACHE", install_path)  # 正确
    shutil.copy2(working_dir / "LICENSE-MIT", install_path)     # 正确

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