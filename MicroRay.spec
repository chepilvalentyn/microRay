# -*- mode: python -*-

block_cipher = None


a = Analysis(['MicroRay.py'],
             pathex=['C:\\Users\\Karlheinz\\Desktop\\microRay'],
             binaries=[],
             datas=[('applicationSettings.json', '.'),
                    ('README.md', '.'),
                    ('core/includeFileTemplates', 'core/includeFileTemplates'),
                    ('gui/resources', 'gui/resources'),
                    ('documentation', 'documentation'),
                    ],
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
          exclude_binaries=True,
          name='microRay',
          icon='icon.ico',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='MicroRay')
