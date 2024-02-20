# venv — Создание виртуальных сред

    Новое в версии 3.3.

> Исходный код: `Lib/venv/`

- venv Модуль обеспечивает поддержку для создания облегченных “виртуальных сред” с их собственными каталогами сайтов, необязательно изолированными от системных каталогов сайтов. Каждая виртуальная среда имеет свой собственный двоичный файл Python (который соответствует версии двоичного файла, который использовался для создания этой среды) и может иметь свой собственный независимый набор установленных пакетов Python в каталогах своего сайта.

- См. `PEP 405` для получения дополнительной информации о виртуальных средах Python.

Смотрите также Руководство пользователя по упаковке Python: создание и использование виртуальных сред
Создание виртуальных сред
Создание виртуальных сред выполняется путем выполнения командыvenv:

***python3 -m venv /path/to/new/virtual/environment***

Выполнение этой команды создает целевой каталог (создавая любые родительские каталоги, которые еще не существуют) и помещает pyvenv.cfgв него файл с homeключом, указывающим на установку Python, из которой была запущена команда (общее имя для целевого каталога - .`venv`). Он также создает binподкаталог (или Scriptsв Windows), содержащий копию / символическую ссылку двоичного файла / двоичных файлов Python (в зависимости от платформы или аргументов, используемых во время создания среды). Он также создает (изначально пустой) `lib/pythonX.Y/site-packages` подкаталог (в Windows это `Lib\site-packages`). Если указан существующий каталог, он будет использоваться повторно.

Устарел с версии 3.6:pyvenv был рекомендуемым инструментом для создания виртуальных сред для Python 3.3 и 3.4 и устарел в Python 3.6.

Изменено в версии 3.5: venvтеперь для создания виртуальных сред рекомендуется использовать.

В Windows вызовите venvкоманду следующим образом:

`c:\>c:\Python35\python -м venv c:\path\to\myenv`
В качестве альтернативы, если вы настроили `PATH``PATHEXT` переменные and для вашей установки Python:

`c:\>python -m venv c:\path\to\myenv`

Команда, если она выполняется с-h, покажет доступные параметры:

использование: `venv [-h] [--system-site-packages] [--символические ссылки | --копии] [--очистить]
 [--upgrade] [--without-pip] [--prompt ПОДСКАЗКА] [--upgrade-deps]
 ENV_DIR [ENV_DIR ...]`

Создает виртуальные среды Python в одном или нескольких целевых каталогах.

позиционные аргументы:
 `ENV_DIR` Каталог для создания среды.

необязательные аргументы:
> `-h`, `--help` показать это справочное сообщение и выйти
 `--system-site-packages`

 Предоставьте виртуальной среде доступ к системному
сайту-каталог пакетов.
> --символические ссылки Пытаются использовать символические ссылки, а не копии, когда символические
ссылки не используются по умолчанию для платформы.
>> --копии Пытаются использовать копии, а не символические ссылки, даже если
символические ссылки используются по умолчанию для платформы.

     --очистить Удалить содержимое каталога среды, если оно
    уже существует, перед созданием среды.
     --обновление Обновите каталог среды, чтобы использовать эту версию
Python, предполагая, что Python был обновлен на месте.
 `--without-pip` Пропускает установку или обновление `pip` в виртуальной
среде (по умолчанию `pip` загружается)
 --приглашение `PROMPT` предоставляет альтернативный префикс приглашения для этой
среды.
 --обновление-deps Обновление основных зависимостей: `pip setuptools` до
последней версии в `PyPI`

После создания среды вы можете захотеть активировать ее, например, путем
поиска скрипта `activate` в его каталоге `bin`.
Изменено в версии 3.9: добавлена `--upgrade-deps` возможность обновления `pip + setuptools` до последней версии в `PyPI`

Изменено в версии 3.4: устанавливает `pip` по умолчанию, добавлены параметры `--without-pipи--copies`
Изменено в версии 3.4: в более ранних версиях, если целевой каталог уже существовал, возникала ошибка, если `--clear--upgrade` не была указана опция или.

Примечание Хотя символические ссылки поддерживаются в Windows, они не рекомендуются. Особо следует отметить, что двойной щелчок `python.exe` в проводнике файлов быстро разрешит символическую ссылку и проигнорирует виртуальную среду.
Примечание В Microsoft Windows может потребоваться включить `Activate.ps1` сценарий, установив политику выполнения для пользователя. Вы можете сделать это, выполнив следующую команду PowerShell:
PS `C:> Set-ExecutionPolicy -ExecutionPolicy` RemoteSigned -Область CurrentUser

Дополнительные сведения см. в разделе О политиках выполнения.

Созданный `pyvenv.cfg` файл также включает в `include-system-site-packages` себя ключ, для которого установлено trueзначение, если venvвыполняется с `--system-site-packages` параметром, `false` иначе.

Если `--without-pip` опция не указана, ensurepipбудет вызываться для начальной загрузки pipв виртуальную среду.

Может быть задано несколько путейvenv, и в этом случае в соответствии с заданными параметрами на каждом предоставленном пути будет создана идентичная виртуальная среда.

После создания виртуальной среды ее можно “активировать” с помощью скрипта в двоичном каталоге виртуальной среды. Вызов скрипта зависит от платформы (`<venv>` должен быть заменен путем к каталогу, содержащему виртуальную среду):

## Платформа

### Оболочка

Команда для активации виртуальной среды

```bash
    POSIX

    bash/zsh

    $ source <venv>/bin/activate

    fish

    $ source <venv>/bin/activate.fish

    csh/tcsh

    $ source <venv>/bin/activate.csh

    Ядро PowerShell

    $ <venv>/bin/Activate.ps1

    Windows

    cmd.exe

    C:\> <venv>\Scripts\activate.bat

    PowerShell

    PS C:\> <venv>\Scripts\Activate.ps1
```

Когда виртуальная среда активна, `VIRTUAL_ENV` переменной среды устанавливается путь к виртуальной среде. Это можно использовать, чтобы проверить, выполняется ли он внутри виртуальной среды.

Вам специально не нужно активировать среду; активация просто добавляет двоичный каталог виртуальной среды к вашему пути, так что `“python”` вызывает интерпретатор `Python` виртуальной среды, и вы можете запускать установленные скрипты без необходимости использовать их полный путь. Однако все скрипты, установленные в виртуальной среде, должны быть доступны для запуска без ее активации и автоматически запускаться с помощью `Python` виртуальной среды.

Вы можете деактивировать виртуальную среду, введя “деактивировать” в своей оболочке. Точный механизм зависит от платформы и является внутренней деталью реализации (обычно используется скрипт или функция оболочки).

Новое в версии 3.4:`fish` и `csh` сценарии активации.

Новое в версии 3.8: сценарии активации `PowerShell`, установленные в `POSIX` для поддержки ядра PowerShell.

Примечание Виртуальная среда - это среда Python, в которой интерпретатор Python, библиотеки и скрипты, установленные в нем, изолированы от тех, которые установлены в других виртуальных средах, и (по умолчанию) любых библиотек, установленных в “системном” Python, то есть той, которая установлена как часть вашей операционной системы.
Виртуальная среда - это дерево каталогов, содержащее исполняемые файлы `Python` и другие файлы, которые указывают, что это виртуальная среда.

Обычные средства установки, такие как `setuptools` и `pip`, работают с виртуальными средами, как и ожидалось. Другими словами, когда виртуальная среда активна, они устанавливают пакеты `Python` в виртуальную среду без необходимости явного указания сделать это.

Когда виртуальная среда активна (т. Е. Запущен интерпретатор Python виртуальной среды), атрибуты `sys.prefix` и `sys.exec_prefix` указывают на базовый каталог виртуальной среды, тогда `sys.base_prefix` как и sys.`base_exec_prefix` указывают на установку `Python` в невиртуальной среде, которая использовалась для создания виртуальной среды. Если виртуальная среда не активна, то `sys.prefix` это то же `sys.base_prefix` самое, что и и `sys.exec_prefix` то же `sys.base_exec_prefix` самое, что и (все они указывают на установку `Python` в невиртуальной среде).

Когда виртуальная среда активна, любые параметры, изменяющие путь установки, будут игнорироваться во всех `distutils` файлах конфигурации, чтобы предотвратить непреднамеренную установку проектов за пределами виртуальной среды.

При работе в командной оболочке пользователи могут сделать виртуальную среду активной, запустив `activate` скрипт в каталоге исполняемых файлов виртуальной среды (точное имя файла и команда для использования файла зависят от оболочки), который добавляет каталог виртуальной среды для исполняемых файлов к переменной `PATH` среды для запущенной оболочки. При других обстоятельствах не должно быть необходимости в активации виртуальной среды; скрипты, установленные в виртуальных средах, имеют строку “`shebang`”, которая указывает на интерпретатор `Python` виртуальной среды. Это означает, что скрипт будет выполняться с этим интерпретатором независимо от значения `PATH`. В Windows обработка строк “shebang” поддерживается, если у вас установлен `Python Launcher` для Windows (это было добавлено в Python в 3.3 - см. `PEP 397` для получения более подробной информации). Таким образом, двойной щелчок установленного скрипта в окне проводника Windows должен запускать скрипт с правильным интерпретатором без необходимости какой-либо ссылки на его виртуальную среду `PATH`.

## API

Описанный выше высокоуровневый метод использует простой API, который предоставляет сторонним создателям виртуальных сред механизмы для настройки создания среды в соответствии с их потребностями, `EnvBuilder` классом.

`Falsevenv`.`EnvBuilder=system_site_packages` (класс, очистить =False, символические ссылки = False, обновить =False, with_pip=False, подсказка = Нет, upgrade_deps=False)
EnvBuilderКласс принимает следующие аргументы ключевого слова при создании экземпляра:

`system_site_packages` – логическое значение, указывающее, что системные пакеты сайта Python должны быть доступны для среды (по умолчанию `False`).

`clear` – логическое значение, которое, если `true`, удаляет содержимое любого существующего целевого каталога перед созданием среды.

`symlinks` – логическое значение, указывающее, следует ли пытаться использовать символическую ссылку на двоичный файл `Python` вместо копирования.

`upgrade` – логическое значение, которое, если `true`, обновит существующую среду с помощью запущенного `Python` - для использования, когда этот `Python` был обновлен на месте (по умолчанию `False`).

`with_pip` – логическое значение, которое, если true, гарантирует, что `pip` установлен в виртуальной среде. Это используется ensurepipс `--default-pip` опцией.

`prompt` – Строка, которая будет использоваться после активации виртуальной среды (по умолчанию Noneэто означает, что будет использоваться имя каталога среды). Если указана специальная строка".", в качестве запроса используется базовое имя текущего каталога.

`upgrade_deps` – Обновите базовые модули `venv` до последней версии в `PyPI`

Изменено в версии 3.4: добавлен `with_pip` параметр

Новое в версии 3.6: добавлен promptпараметр

Новое в версии 3.9: добавлен `upgrade_deps` параметр

Создатели сторонних инструментов виртуальной среды могут свободно использовать предоставленный `EnvBuilder` класс в качестве базового класса.

Возвращаемый `env-builder` представляет собой объект, который имеет метод,create:

`create(env_dir)`
Создайте виртуальную среду, указав целевой каталог (абсолютный или относительный к текущему каталогу), который должен содержать виртуальную среду. createМетод либо создаст среду в указанном каталоге, либо вызовет соответствующее исключение.

createМетод EnvBuilderкласса иллюстрирует крючки, доступные для настройки подкласса:

```python

def  create(self, env_dir):
    '''
    Создайте виртуализированную среду Python в каталоге.
    env_dir - это целевой каталог для создания среды.
    '''
    env_dir = os.path.abspath(env_dir)
    context = self.ensure_directories(env_dir)
    self.create_configuration(context)
    self.setup_python(context)
    self.setup_scripts(context)
    self.post_setup(context)

```

Каждый из методов ensure_directories(), create_configuration(), setup_python(), setup_scripts()и post_setup()может быть переопределен.

ensure_directories(env_dir)
Создает каталог среды и все необходимые каталоги и возвращает объект контекста. Это просто держатель для атрибутов (таких как пути), для использования другими методами. Каталогам разрешено существовать уже, если либо clearили upgradeбыли указаны, чтобы разрешить работу с существующим каталогом среды.

create_configuration(контекст)
Создает файл pyvenv.cfgконфигурации в среде.

setup_python(контекст)
Создает копию или символическую ссылку на исполняемый файл Python в среде. В системах POSIX, если использовался конкретный исполняемый python3.xфайл, pythonбудут созданы символические ссылки на python3и, указывающие на этот исполняемый файл, если файлы с такими именами уже не существуют.

setup_scripts(контекст)
Устанавливает сценарии активации, соответствующие платформе, в виртуальную среду.

upgrade_dependencies(контекст)
Обновляет основные пакеты зависимостей venv (в настоящее pipвремя и setuptools) в среде. Это делается путем pipперехода к исполняемому файлу в среде.

Новое в версии 3.9.

post_setup(контекст)
Метод-заполнитель, который может быть переопределен в сторонних реализациях для предварительной установки пакетов в виртуальной среде или выполнения других шагов после создания.

Изменено в версии 3.7.2: Windows теперь использует сценарии перенаправления python[w].exeвместо копирования реальных двоичных файлов. В 3.7.2 только setup_python()ничего не делает, если не запускается из сборки в исходном дереве.

Изменено в версии 3.7.3: Windows копирует сценарии перенаправления как часть setup_python()вместо setup_scripts(). В 3.7.2 этого не было. При использовании символических ссылок исходные исполняемые файлы будут связаны.

Кроме того, EnvBuilderпредоставляет этот служебный метод, который можно вызывать из setup_scripts()подклассов или post_setup()в подклассах, чтобы помочь в установке пользовательских сценариев в виртуальную среду.

install_scriptsконтекст (, путь)
path - это путь к каталогу, который должен содержать подкаталоги “common”, “posix”, “nt”, каждый из которых содержит сценарии, предназначенные для каталога bin в среде. Содержимое “общего” и соответствующего каталога os.nameкопируется после некоторой замены текста заполнителей:

    __VENV_DIR__   заменяется абсолютным путем к каталогу среды.

    __VENV_NAME__   заменяется именем среды (конечным сегментом пути каталога среды).

    __VENV_PROMPT__   заменяется на приглашение (имя среды, заключенное в круглые скобки, и следующий пробел)
    __VENV_BIN_NAME__   заменяется именем каталога bin (либо binили Scripts).
    __VENV_PYTHON__  заменяется абсолютным путем к исполняемому файлу среды.

Каталогам разрешено существовать (при обновлении существующей среды).

Существует также удобная функция на уровне модуля:

    venv.create(env_dir, system_site_packages=False, clear=False, symlinks=False, with_pip=False, prompt=None, upgrade_deps=False)

Create an EnvBuilder with the given keyword arguments, and call its create() method with the env_dir argument.

Новое в версии 3.3.

Изменено в версии 3.4: добавлен with_pipпараметр

Изменено в версии 3.6: добавлен promptпараметр

Изменено в версии 3.9: добавлен upgrade_depsпараметр

Пример расширения EnvBuilder
Следующий сценарий показывает, как расширитьEnvBuilder, реализовав подкласс, который устанавливает setuptools и pip в созданную виртуальную среду:

```python
import os
import os.path
from subprocess import Popen, PIPE
import sys
from threading import Thread
from urllib.parse import urlparse
from urllib.request import urlretrieve
import venv

class ExtendedEnvBuilder(venv.EnvBuilder):
    """
    This builder installs setuptools and pip so that you can pip or
    easy_install other packages into the created virtual environment.

    :param nodist: If true, setuptools and pip are not installed into the
                   created virtual environment.
    :param nopip: If true, pip is not installed into the created
                  virtual environment.
    :param progress: If setuptools or pip are installed, the progress of the
                     installation can be monitored by passing a progress
                     callable. If specified, it is called with two
                     arguments: a string indicating some progress, and a
                     context indicating where the string is coming from.
                     The context argument can have one of three values:
                     'main', indicating that it is called from virtualize()
                     itself, and 'stdout' and 'stderr', which are obtained
                     by reading lines from the output streams of a subprocess
                     which is used to install the app.

                     If a callable is not specified, default progress
                     information is output to sys.stderr.
    """

    def __init__(self, *args, **kwargs):
        self.nodist = kwargs.pop('nodist', False)
        self.nopip = kwargs.pop('nopip', False)
        self.progress = kwargs.pop('progress', None)
        self.verbose = kwargs.pop('verbose', False)
        super().__init__(*args, **kwargs)

    def post_setup(self, context):
        """
        Set up any packages which need to be pre-installed into the
        virtual environment being created.

        :param context: The information for the virtual environment
                        creation request being processed.
        """
        os.environ['VIRTUAL_ENV'] = context.env_dir
        if not self.nodist:
            self.install_setuptools(context)
        # Can't install pip without setuptools
        if not self.nopip and not self.nodist:
            self.install_pip(context)

    def reader(self, stream, context):
        """
        Read lines from a subprocess' output stream and either pass to a progress
        callable (if specified) or write progress information to sys.stderr.
        """
        progress = self.progress
        while True:
            s = stream.readline()
            if not s:
                break
            if progress is not None:
                progress(s, context)
            else:
                if not self.verbose:
                    sys.stderr.write('.')
                else:
                    sys.stderr.write(s.decode('utf-8'))
                sys.stderr.flush()
        stream.close()

    def install_script(self, context, name, url):
        _, _, path, _, _, _ = urlparse(url)
        fn = os.path.split(path)[-1]
        binpath = context.bin_path
        distpath = os.path.join(binpath, fn)
        # Download script into the virtual environment's binaries folder
        urlretrieve(url, distpath)
        progress = self.progress
        if self.verbose:
            term = '\n'
        else:
            term = ''
        if progress is not None:
            progress('Installing %s ...%s' % (name, term), 'main')
        else:
            sys.stderr.write('Installing %s ...%s' % (name, term))
            sys.stderr.flush()
        # Install in the virtual environment
        args = [context.env_exe, fn]
        p = Popen(args, stdout=PIPE, stderr=PIPE, cwd=binpath)
        t1 = Thread(target=self.reader, args=(p.stdout, 'stdout'))
        t1.start()
        t2 = Thread(target=self.reader, args=(p.stderr, 'stderr'))
        t2.start()
        p.wait()
        t1.join()
        t2.join()
        if progress is not None:
            progress('done.', 'main')
        else:
            sys.stderr.write('done.\n')
        # Clean up - no longer needed
        os.unlink(distpath)

    def install_setuptools(self, context):
        """
        Install setuptools in the virtual environment.

        :param context: The information for the virtual environment
                        creation request being processed.
        """
        url = 'https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py'
        self.install_script(context, 'setuptools', url)
        # clear up the setuptools archive which gets downloaded
        pred = lambda o: o.startswith('setuptools-') and o.endswith('.tar.gz')
        files = filter(pred, os.listdir(context.bin_path))
        for f in files:
            f = os.path.join(context.bin_path, f)
            os.unlink(f)

    def install_pip(self, context):
        """
        Install pip in the virtual environment.

        :param context: The information for the virtual environment
                        creation request being processed.
        """
        url = 'https://bootstrap.pypa.io/get-pip.py'
        self.install_script(context, 'pip', url)

def main(args=None):
    compatible = True
    if sys.version_info < (3, 3):
        compatible = False
    elif not hasattr(sys, 'base_prefix'):
        compatible = False
    if not compatible:
        raise ValueError('This script is only for use with '
                         'Python 3.3 or later')
    else:
        import argparse

        parser = argparse.ArgumentParser(prog=__name__,
                                         description='Creates virtual Python '
                                                     'environments in one or '
                                                     'more target '
                                                     'directories.')
        parser.add_argument('dirs', metavar='ENV_DIR', nargs='+',
                            help='A directory in which to create the '
                                 'virtual environment.')
        parser.add_argument('--no-setuptools', default=False,
                            action='store_true', dest='nodist',
                            help="Don't install setuptools or pip in the "
                                 "virtual environment.")
        parser.add_argument('--no-pip', default=False,
                            action='store_true', dest='nopip',
                            help="Don't install pip in the virtual "
                                 "environment.")
        parser.add_argument('--system-site-packages', default=False,
                            action='store_true', dest='system_site',
                            help='Give the virtual environment access to the '
                                 'system site-packages dir.')
        if os.name == 'nt':
            use_symlinks = False
        else:
            use_symlinks = True
        parser.add_argument('--symlinks', default=use_symlinks,
                            action='store_true', dest='symlinks',
                            help='Try to use symlinks rather than copies, '
                                 'when symlinks are not the default for '
                                 'the platform.')
        parser.add_argument('--clear', default=False, action='store_true',
                            dest='clear', help='Delete the contents of the '
                                               'virtual environment '
                                               'directory if it already '
                                               'exists, before virtual '
                                               'environment creation.')
        parser.add_argument('--upgrade', default=False, action='store_true',
                            dest='upgrade', help='Upgrade the virtual '
                                                 'environment directory to '
                                                 'use this version of '
                                                 'Python, assuming Python '
                                                 'has been upgraded '
                                                 'in-place.')
        parser.add_argument('--verbose', default=False, action='store_true',
                            dest='verbose', help='Display the output '
                                               'from the scripts which '
                                               'install setuptools and pip.')
        options = parser.parse_args(args)
        if options.upgrade and options.clear:
            raise ValueError('you cannot supply --upgrade and --clear together.')
        builder = ExtendedEnvBuilder(system_site_packages=options.system_site,
                                       clear=options.clear,
                                       symlinks=options.symlinks,
                                       upgrade=options.upgrade,
                                       nodist=options.nodist,
                                       nopip=options.nopip,
                                       verbose=options.verbose)
        for d in options.dirs:
            builder.create(d)
    
    if __name__ == '__main__':
    rc = 1
    try:
        main()
        rc = 0
    except Exception as e:
        print('Error: %s' % e, file=sys.stderr)
    sys.exit(rc)

```
