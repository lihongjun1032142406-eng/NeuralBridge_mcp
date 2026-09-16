from pathlib import Path

root = Path(__file__).resolve().parents[1]

# Chinese edition build transform. Only exact quoted user-visible literals are changed.
# Identifiers, MCP protocol/tool names and log category values remain untouched.
replacements = {
    "Status": "状态", "Setup": "设置", "Logs": "日志",
    "CHECKING STATUS...": "正在检查状态…", "WAITING FOR CONNECTION": "等待连接",
    "Waiting for connection": "等待 MCP 客户端连接", "ENABLE": "启用",
    "Accessibility": "无障碍服务", "MCP Server": "MCP 服务", "Screenshots": "截图",
    "DEVICE INFO": "设备信息", "PERFORMANCE": "性能", "Total": "总计",
    "PERMISSIONS 0/5": "权限 0/5", "CLEAR": "清空", "PAUSE": "暂停",
    "No commands logged yet.\\nExecute MCP commands to see activity here.": "暂无命令日志。\\n执行 MCP 命令后将在此显示活动记录。",
    "Permission Name": "权限名称", "Description": "说明", "GRANT": "授权",
    "DISABLED": "已停用", "ALL SYSTEMS READY": "全部系统就绪", "SETUP INCOMPLETE": "设置未完成",
    "NEURALBRIDGE IS OFF": "NEURALBRIDGE 已关闭", "Toggle to enable": "打开开关以启用",
    "CONNECTED": "已连接", "ACTIVE": "已启用", "RUNNING": "运行中", "OFF": "关闭",
    "FAST": "快速", "SLOW": "慢速", "GRANTED": "已授权", "RESUME": "继续",
    "AccessibilityService": "无障碍服务",
    "Core automation service for UI control and observation": "用于界面控制和观察的核心自动化服务",
    "Notification Listener": "通知读取权限", "Access full notification content": "读取完整通知内容",
    "Post Notifications": "发送通知", "Show foreground service notification": "显示前台服务通知",
    "Battery Optimization": "电池优化", "Prevent Android from killing the service": "防止 Android 终止后台服务",
    "MediaProjection": "屏幕捕获", "Enable fast screenshot capture (60ms)": "启用快速截图捕获（约 60ms）",
    "device-ip": "设备IP", "no wifi": "无 Wi-Fi",
}

files = [
    root / "app/src/main/res/layout/activity_main.xml",
    root / "app/src/main/res/layout/header_gradient.xml",
    root / "app/src/main/res/layout/tab_status.xml",
    root / "app/src/main/res/layout/tab_setup.xml",
    root / "app/src/main/res/layout/tab_logs.xml",
    root / "app/src/main/res/layout/item_permission_card.xml",
    root / "app/src/main/kotlin/com/neuralbridge/companion/MainActivity.kt",
]

for path in files:
    text = path.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(f'"{old}"', f'"{new}"')
    if path.name == "MainActivity.kt":
        text = text.replace('permissionProgressLabel.text = "PERMISSIONS $granted/$total"', 'permissionProgressLabel.text = "权限 $granted/$total"')
        text = text.replace('append("Model: ${Build.MANUFACTURER} ${Build.MODEL}\\n")', 'append("型号: ${Build.MANUFACTURER} ${Build.MODEL}\\n")')
        text = text.replace('append("Screen: ${dm.widthPixels}x${dm.heightPixels} @ ${dm.densityDpi}dpi\\n")', 'append("屏幕: ${dm.widthPixels}x${dm.heightPixels} @ ${dm.densityDpi}dpi\\n")')
        text = text.replace('append("Density: ${dm.density}x")', 'append("密度: ${dm.density}x")')
    path.write_text(text, encoding="utf-8")
    print(f"localized: {path.relative_to(root)}")

print("zh-CN UI transform complete; MCP protocol/tool/category identifiers preserved")
