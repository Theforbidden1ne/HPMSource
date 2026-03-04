import os
import shutil
print('Building installer')
os.system('python3 -m PyInstaller py\pki.py --onefile --noconsole --name install')

print('frameworking default package')
shutil.copy('dist/install.exe', 'DefaultPackage/install.exe')

print('building backend')
os.system('python3 -m PyInstaller --onefile --noconsole py/packageManager.py ')

print('building frontend mobile')

os.system('python3 -m PyInstaller --onefile --noconsole py/packageFrontendMobile.py')

print('building frontend desktop')

os.system('python3 -m PyInstaller --onefile --noconsole py/packageFrontendDesktop.py')