import os
import subprocess


def main():
    os.makedirs('build', exist_ok=True)
    subprocess.check_call('cmake -B build -G "NMake Makefiles"', shell=True)
    subprocess.check_call('cmake --build .', shell=True, cwd='build')

    subprocess.check_call('experiments 1 2 3', shell=True, cwd='build')
    subprocess.check_call('experiments 2 3 4', shell=True, cwd='build')


if __name__ == '__main__':
    main()
