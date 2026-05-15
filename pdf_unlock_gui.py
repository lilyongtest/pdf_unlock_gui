import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pikepdf
import os


def remove_pdf_restrictions(input_path, output_path, password=None):
    try:
        # パスワード付き / なし の両方に対応
        with pikepdf.open(input_path, password=password) as pdf:
            pdf.save(output_path)

        messagebox.showinfo(
            "成功",
            f"制限解除されたPDFを保存しました！\n\n{output_path}"
        )

    except Exception as e:
        messagebox.showerror("エラー", f"エラーが発生しました:\n\n{e}")


# =========================
# GUI開始
# =========================
root = tk.Tk()
root.withdraw()  # メインウィンドウを非表示

# 1. PDFファイル選択
input_file = filedialog.askopenfilename(
    title="PDFファイルを選択してください",
    filetypes=[("PDF files", "*.pdf")]
)

# キャンセル時
if not input_file:
    messagebox.showwarning("キャンセル", "ファイルが選択されませんでした")
    exit()


# 2. 保存先を指定
base_name = os.path.splitext(os.path.basename(input_file))[0]

output_file = filedialog.asksaveasfilename(
    title="保存先を指定してください",
    defaultextension=".pdf",
    initialfile=f"{base_name}_unrestricted.pdf",
    filetypes=[("PDF files", "*.pdf")]
)

# キャンセル時
if not output_file:
    messagebox.showwarning("キャンセル", "保存先が選択されませんでした")
    exit()


# 3. パスワードの有無を確認
has_password = messagebox.askyesno(
    "パスワード確認",
    "このPDFにはパスワードがありますか？"
)

pdf_password = None

# 4. パスワード入力
if has_password:
    pdf_password = simpledialog.askstring(
        "パスワード入力",
        "PDFのパスワードを入力してください",
        show="*"
    )

    # 未入力チェック
    if pdf_password is None:
        messagebox.showwarning("キャンセル", "パスワード入力がキャンセルされました")
        exit()


# 5. 実行
remove_pdf_restrictions(input_file, output_file, pdf_password)
