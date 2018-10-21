ACM-ICPC Code Template
==============================
Generate ACM-ICPC Code Template with LaTex.

(1) Write code.

(2) Place your code in **./source** and classify in different subdirectory.

Example:
```
.
└───source
    ├── DataStructure
    │   └── Code_1.cpp
    ├── Graph
    │   └── Code_1.cpp
    └── Math
        ├── Code_1.cpp
        └── Code_2.cpp
```
## Required
- LaTex
- Python 3
- Pygments `pip install Pygments`
- (optional) Clang-Format
- (optional) mono Font: [Iosevka Term Slab](https://github.com/be5invis/Iosevka)
- (optional) CJK mono Font: [Sarasa Gothic](https://github.com/be5invis/Sarasa-Gothic)
## Usage
``` python
python gen.py
```
## feature
- Support CJK
- Can format code with [Clang-Format](http://clang.llvm.org/docs/ClangFormat.html)

Switch True/False the *Format function* by change the `FORMAT` value in **./gen.py** (default False)</br>
Using **listings** or **minted** to highlight code by change the `MINTED` value in **./gen.py** (default True)

Sorted by lexicographical order.

**./head:** you can change the author and font here.</br>
**./.clang-format:** set the code style if necessary.</br>

Code inside is for fun, that's all.

The `README.md` & `head` are based on [ACM-ICPC-CodeTemplate-Latex @jasison27](https://github.com/jasison27/ACM-ICPC-CodeTemplate-Latex)
