# 概要

このリポジトリではBlenderのPython APIを使って、Blender上でBatch Renderingを行う方法を書いています。
Blenderはバックグラウンドで実行し、CLIから実行させます。

# Pythonスクリプト

- [render_batch.py](render_batch.py)
- [create_folder.py](create_folder.py)

# 使い方
1. BlenderとVSCodeをインストールします
1. VSCodeで`tasks.json`と`keybindings.json`を編集し、`Ctrl+Shift+B`で現在開いている`.py`ファイルを、BlenderのPythonスクリプトとして実行できるようにします
