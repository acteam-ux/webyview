from setuptools import setup

extras_require = {
    'cef': ['cefpython3'],
    'gtk': ['PyGObject'],
    'pyside2': ['QtPy', 'PySide2'],
    'pyside6': ['QtPy', 'PySide6'],
    'qt': ['QtPy', 'PyQt5', 'pyqtwebengine'],
}

install_requires = [
    'pythonnet ; sys_platform == "win32"',
    'pyobjc-core ; sys_platform == "darwin"',
    'pyobjc-framework-Cocoa ; sys_platform == "darwin"',
    'pyobjc-framework-WebKit ; sys_platform == "darwin"',
    'QtPy ; sys_platform == "openbsd6"',
    'importlib_resources; python_version < "3.7"',
    'proxy_tools',
    'bottle'
]


with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='webyview',
    author='acteam-ux',
    author_email='abolfazlmalekpour@gmail.com',
    description=('Build GUI for your Python program with JavaScript, HTML, and CSS.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/acteam-ux/webyview',
    download_url='https://github.com/acteam-ux/webyview/archive/23.3.0.tar.gz',
    keywords=['gui', 'html', 'web'],
    install_requires=install_requires,
    extras_require=extras_require,
    version='23.3.0',
    include_package_data=True,
    packages=['webview', 'webview.js', 'webview.platforms'],
    package_dir={'webview': 'webview'},
    package_data={
        'webview': [
            'webview/lib/WebBrowserInterop.x64.dll',
            'webview/lib/WebBrowserInterop.x86.dll',
            'webview/lib/arm64/WebView2Loader.dll',
            'webview/lib/arm64/WebView2Loader.dll',
            'webview/lib/x64/WebView2Loader.dll',
            'webview/lib/x86/WebView2Loader.dll',
            'webview/lib/Microsoft.Web.WebView2.Core.dll',
            'webview/lib/Microsoft.Web.WebView2.LICENSE.md',
            'webview/lib/Microsoft.Web.WebView2.WinForms.dll',
        ]
    },
    license='New BSD license',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications :: GTK',
        'Environment :: X11 Applications :: Qt',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces'
    ],
)
