# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: BookTrail
import sys, os

ANSI = os.environ.get('NOANSI', '').lower() != '1'

if ANSI:
    C = '\033[1;35m'
    NC = '\033[0m'
    def w(s): return f'{C}{s}{NC}'
    def log(s): print(w(f'>>> {s}'))
    def info(s): print(w(f'  • {s}'))
    def warn(s): print(f'\033[93m  ! {s}\033[0m')
    def err(s): print(f'\033[91m  ✖ {s}\033[0m')
    def header(s): print(w(f'\n═══ {s} ═══'))
else:
    C = NC = ''
    def w(s): return s
    def log(s): print(f'>>> {s}')
    def info(s): print(f'  • {s}')
    def warn(s): print(f'  ! {s}')
    def err(s): print(f'  ✖ {s}')
    def header(s): print(f'\n═══ {s} ═══')
