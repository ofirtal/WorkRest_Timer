# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/Adi Tal/PycharmProjects/Tkinter_Projects/Timer4/Timer4.py'],
             pathex=['C:\\Users\\Adi Tal\\PycharmProjects\\Tkinter_Projects\\Timer4'],
             binaries=[],
             datas=[('C:/Users/Adi Tal/PycharmProjects/Tkinter_Projects/Timer4/sounds/A-Tone-His_Self-1266414414.wav', '.'), ('C:/Users/Adi Tal/PycharmProjects/Tkinter_Projects/Timer4/sounds/Cuckoo Clock-SoundBible.com-1776874523.wav', '.'), ('C:/Users/Adi Tal/PycharmProjects/Tkinter_Projects/Timer4/sounds/Rooster Crow-SoundBible.com-1802551702.wav', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Timer4',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\Adi Tal\\PycharmProjects\\Tkinter_Projects\\Timer4\\clock_icon.ico')