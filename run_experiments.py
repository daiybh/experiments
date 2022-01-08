import os
import subprocess
import shutil

#"C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\VC\Auxiliary\Build\vcvarsall.bat" x86_amd64
def doB(buildType):
    
    tempFolder='buildxx\\'+buildType
	shutil.rmtree(tempFolder)
    #os.rmdir(tempFolder)
    os.makedirs(tempFolder, exist_ok=True)    
    subprocess.check_call('cmake -B {} -G "Ninja" -DCMAKE_BUILD_TYPE:STRING="{}" -DCMAKE_INSTALL_PREFIX=ainstall\\'.format(tempFolder,buildType), shell=True)
    subprocess.check_call('cmake --build .', shell=True, cwd=tempFolder)

    subprocess.check_call('cmake --install .', shell=True, cwd=tempFolder)
    
    #subprocess.check_call('experiments 1 2 3', shell=True, cwd='build')
    #subprocess.check_call('experiments 2 3 4', shell=True, cwd='build')


if __name__ == '__main__':
    doB("Debug")
    doB("RelWithDebInfo")
