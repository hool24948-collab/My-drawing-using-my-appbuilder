[app]

# (str) Title of your application
title = App Builder

# (str) Package name
package.name = appbuilder

# (str) Package domain (needed for android packaging)
package.domain = org.appbuilder

# (str) Version of your application
version = 0.1

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 21

# (str) Android SDK Build Tools version
android.sdk_build_tools_version = 33.0.2

# (str) Android NDK version to use (стабильная версия для компиляции расширений)
android.ndk = 25b

# (list) Permissions (нужны для доступа к памяти устройства и выбора файлов)
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 1

# (int) Display warning if buildozer is run as root
warn_on_root = 1
