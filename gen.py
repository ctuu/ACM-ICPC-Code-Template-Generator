import os

IGNORE = ['config', '.gitkeep']
HEAD = 'head'
TAIL = 'tail'
PATH = 'source'
FILENAME = 'template'
FORMAT = False

_list = []
_dict = {}
_root = os.path.expanduser(PATH)


def _format(path):
    os.system('clang-format -i "%s"' % (path))


def p_add(path, name, parent, suffix):
    if FORMAT is True:
        _format(path)

    if parent not in _dict:
        _dict[parent] = []

    name = name.replace('_', '\\_')
    path_tuple = (path, name, suffix)

    _dict[parent].append(path_tuple)


def p_walk(root, parent):
    if not os.path.isdir(root):
        os.mkdir(root)
        return

    for i in os.listdir(root):
        cur_path = os.path.join(root, i)
        name, suffix = os.path.splitext(i)

        if i in IGNORE:
            continue

        if os.path.isdir(cur_path):
            p_walk(cur_path, i)
            continue

        p_add(cur_path, name, parent, suffix)


def p_tran():
    for c in _dict:
        _tuple = (c, _dict[c])

        _list.append(_tuple)


def p_sort():
    _list.sort(key=lambda c: c[0])

    for _sub in _list:
        _sub[1].sort(key=lambda c: c[2])
        _sub[1].sort(key=lambda c: c[1])


def p_gen():
    _doc = open(FILENAME + '.tex', 'w', encoding='utf-8')

    with open(HEAD, 'r', encoding='utf-8') as r:
        _doc.write(r.read())

    for section, sub_list in _list:
        _doc.write('\\section{%s}\n' % (section))

        for path, name, suffix in sub_list:
            _doc.write('\\subsection{%s}\n' % (name))
            _doc.write('\\lstinputlisting{%s}\n' % (path))

            suffix = suffix

    with open(TAIL, 'r', encoding='utf-8') as r:
        _doc.write(r.read())

    _doc.close()


def p_build():
    os.system('xelatex %s.tex' % FILENAME)
    os.unlink('%s.pdf' % FILENAME)
    os.system('xelatex %s.tex' % FILENAME)
    os.unlink('%s.aux' % FILENAME)
    os.unlink('%s.log' % FILENAME)
    os.unlink('%s.toc' % FILENAME)


p_walk(_root, 'Not classified')
p_tran()
p_sort()
p_gen()
p_build()

print('Done.')
