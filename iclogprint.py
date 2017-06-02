# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Просмотрщик логов, создаваемых python программами.
"""

import sys
import os.path
import traceback

__version__ = (0, 0, 0, 2)

# Шаблон для использования в современных
# командных оболочках и языках
# программирования таков: \x1b[...m.
# Это ESCAPE-последовательность,
# где \x1b обозначает символ ESC
# (десятичный ASCII код 27), а вместо "..."
# подставляются значения из таблицы,
# приведенной ниже, причем они могут
# комбинироваться, тогда нужно их
# перечислить через точку с запятой.

# атрибуты
# 0 	нормальный режим
# 1 	жирный
# 4 	подчеркнутый
# 5 	мигающий
# 7 	инвертированные цвета
# 8 	невидимый

# цвет текста
# 30 	черный
# 31 	красный
# 32 	зеленый
# 33 	желтый
# 34 	синий
# 35 	пурпурный
# 36 	голубой
# 37 	белый

# цвет фона
# 40 	черный
# 41 	красный
# 42 	зеленый
# 43 	желтый
# 44 	синий
# 45 	пурпурный
# 46 	голубой
# 47 	белый

# Цвета в консоли
RED_COLOR_TEXT = '\x1b[31;1m'   # red
GREEN_COLOR_TEXT = '\x1b[32m'   # green
YELLOW_COLOR_TEXT = '\x1b[33m'  # yellow
BLUE_COLOR_TEXT = '\x1b[34m'    # blue
PURPLE_COLOR_TEXT = '\x1b[35m'  # purple
CYAN_COLOR_TEXT = '\x1b[36m'    # cyan
WHITE_COLOR_TEXT = '\x1b[37m'   # white
NORMAL_COLOR_TEXT = '\x1b[0m'   # normal

DEFAULT_ENCODING = 'utf_8'


def print_color_txt(sTxt, sColor=NORMAL_COLOR_TEXT):
    """
    Печать цветного текста в консоли.
    @param sTxt: Текст
    @param sColor: Цвет текста.
    """
    if type(sTxt) == unicode:
        sTxt = sTxt.encode(DEFAULT_ENCODING)
    txt = sColor+sTxt+NORMAL_COLOR_TEXT
    print(txt)


def print_error(sMsg):
    """
    Вывести информацию ОБ ОШИБКЕ.
    @param sMsg: Текстовое сообщение.
    """
    trace_txt = traceback.format_exc()
    msg = sMsg+'\n'+trace_txt
    print_color_txt(msg, RED_COLOR_TEXT)


def print_log(log_filename):
    """
    Печать лог файла в цвете.
    @param log_filename: Полное имя log файла.
    @return: True/False.
    """
    log_file = None
    cur_color = NORMAL_COLOR_TEXT

    if os.path.exists(log_filename):
        try:
            log_file = open(log_filename, 'r')
            for line in log_file:
                analize_line = line.rstrip()
                if ' DEBUG ' in analize_line:
                    cur_color = BLUE_COLOR_TEXT
                elif ' INFO ' in analize_line:
                    cur_color = GREEN_COLOR_TEXT
                elif ' WARNING ' in analize_line:
                    cur_color = YELLOW_COLOR_TEXT
                elif ' ERROR ' in analize_line:
                    cur_color = PURPLE_COLOR_TEXT
                elif ' CRITICAL ' in analize_line:
                    cur_color = RED_COLOR_TEXT
                print_color_txt(analize_line, cur_color)
            log_file.close()
        except:
            if log_file:
                log_file.close()
            print_error(u'Ошибка чтения файла <%s>' % log_filename)

    else:
        print_color_txt(u'Файл <%s> не найден' % log_filename, YELLOW_COLOR_TEXT)
    return False


def main(args):
    """
    Главная запускаемая функция.
    @param args: Аргументы коммандной строки.
    """
    if args:
        filename = args[0].replace('\\', '')
        return print_log(filename)


if __name__ == '__main__':
    main(sys.argv[1:])
