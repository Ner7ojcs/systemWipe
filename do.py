from main import Main
main_instance = Main()
os_result = main_instance.scan()
os_drive = main_instance.scan_os_drives(os_result)
if os_drive:
    success = main_instance.format_drive(os_drive)
    
    