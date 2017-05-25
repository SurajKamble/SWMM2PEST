# -*- mode: python -*-

block_cipher = None


a = Analysis(['M:\\Script\\Qt1.py', 'M:\\Script\\One.py'],
             pathex=['M:\\Script'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Qt1',
          debug=False,
          strip=False,
          upx=False,
          console=True )
