# PDF Unlock GUI

GUIでPDFの制限解除を行えるツールです。

## Features

- PDFファイル選択
- パスワード付きPDF対応
- GUI操作
- EXE化対応

## Install

```bash
pip install pikepdf
```

## Run

```bash
python pdf_unlock_gui.py
```

## EXE Build

```bash
pyinstaller --onefile --windowed --hidden-import=pikepdf pdf_unlock_gui.py
```

## License

MIT
