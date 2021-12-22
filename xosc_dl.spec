# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['xosc_dl.py'],
             binaries=[],
             datas=[('assets/gui/windowicon.png', './assets/gui/'),
                    ('assets/gui/icons/announcement-banner.png', './assets/gui/icons/'),
                    ('assets/gui/icons/clear-log.png', './assets/gui/icons/'),
                    ('assets/gui/icons/close-shop.png', './assets/gui/icons/'),
                    ('assets/gui/icons/enable-log.png', './assets/gui/icons/'),
                    ('assets/gui/icons/experimental.png', './assets/gui/icons/'),
                    ('assets/gui/icons/about-open-version.png', './assets/gui/icons/'),
                    ('assets/gui/icons/announcement-banner-reload.png', './assets/gui/icons/'),
                    ('assets/gui/icons/hbb-icon.png', './assets/gui/icons/'),
                    ('assets/gui/icons/download.png', './assets/gui/icons/'),
                    ('assets/gui/icons/oscdl-icon.png', './assets/gui/icons/'),
                    ('assets/gui/icons/iconsprovider.png', './assets/gui/icons/'),
                    ('assets/gui/icons/copy-link.png', './assets/gui/icons/'),
                    ('assets/gui/icons/check-for-updates.png', './assets/gui/icons/'),
                    ('assets/gui/icons/work-in-progress.png', './assets/gui/icons/'),
                    ('assets/gui/icons/refresh.png', './assets/gui/icons/'),
                    ('assets/gui/icons/theme.png', './assets/gui/icons/'),
                    ('assets/gui/icons/profile.png', './assets/gui/icons/'),
                    ('assets/gui/icons/controllers/1WiiRemote.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/controllers/2WiiRemote.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/controllers/3WiiRemote.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/controllers/4WiiRemote.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/controllers/ClassicController.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/controllers/GamecubeController.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/controllers/nunchuk.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/controllers/SDHC.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/controllers/USBKeyboard.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/controllers/WiiZapper.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/category/demo.png', './assets/gui/icons/category/'),
                    ('assets/gui/icons/category/emulator.png', './assets/gui/icons/category/'),
                    ('assets/gui/icons/category/game.png', './assets/gui/icons/category/'),
                    ('assets/gui/icons/category/media.png', './assets/gui/icons/category/'),
                    ('assets/gui/icons/category/utility.png', './assets/gui/icons/category/'),
                    ('assets/gui/icons/bricks.png', './assets/gui/icons/'),
                    ('assets/gui/splash.png', './assets/gui/'),
                    ('assets/gui/sendwiisplash.png', './assets/gui/'),
                    ('assets/gui/missing.png', './assets/gui/'),
                    ('assets/themes/oscdark.qss', './assets/themes/'),
                    ('assets/gui/icons/spinner.gif', './assets/gui/icons/'),
                    ('assets/gui/icons/browse.png', './assets/gui/icons/'),
                    ('assets/gui/icons/disk.png', './assets/gui/icons/'),
                    ('assets/gui/icons/sdcard.png', './assets/gui/icons/'),
                    ('assets/gui/icons/downloadlocationdialog.png', './assets/gui/icons/')],
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
          name='xosc_dl',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, icon='oscicon.ico')
