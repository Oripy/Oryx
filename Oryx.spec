# -*- mode: python -*-

block_cipher = None


a = Analysis(['Oryx.py'],
             pathex=['C:/Users/CORSON/Downloads/Oryx'],
             binaries=[],
             datas=[('*.ui', '.')],
             hiddenimports=['anglespinbox',
             'dotspinbox',
             'negativezerospinbox'],
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
          name='Oryx',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
app = BUNDLE(exe,
             name='Oryx.app',
             icon=None,
             bundle_identifier=None)
