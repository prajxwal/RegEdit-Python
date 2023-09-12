import winreg

ID = "ClientID"

def set_value(name, value):
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, ID)
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(e)
        return False

def get_value(name):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, ID, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(key, name)
        winreg.CloseKey(key)
        return value
    except Exception as e:
        print(e)
        return None

def delete_value(name):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, ID, 0, winreg.KEY_WRITE)
        winreg.DeleteValue(key, name)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(e)
        return False

def delete_subkey():
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, ID)
        return True
    except Exception as e:
        print(e)
        return False

def main():
    # Add new settings
    set_value("startup", "1")
    input()

    # Read it
    value = get_value("startup")
    print(value)
    input()

    # Delete it
    delete_value("startup")
    input()

    # Delete the whole key
    delete_subkey()
    input()

if __name__ == "__main__":
    main()
