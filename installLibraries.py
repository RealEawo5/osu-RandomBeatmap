import urllib.request
import os


def install_libraries(libs):
    try:
        for lib in libs:
            os.system(f'pip install {lib}')
        print('Libraries installed!')
    except:
        print('\'pip\' not installed!')
        print('Installing \'pip\'!')
        if 'get-pip.py' in os.listdir(os.getcwd()):
            pass
        else:
            url = 'https://bootstrap.pypa.io/get-pip.py'
            urllib.request.urlretrieve(url, f'{os.getcwd()}\\get-pip.py')
        os.system('python get-pip.py')
        try:
            for lib in libs:
                os.system(f'pip install {lib}')
        except:
            print('Intallation of \'pip\' failed!')
