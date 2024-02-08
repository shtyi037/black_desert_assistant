# 啟動方式
從main.py啟動
```commandline
python main.py
```
# 產出EXE檔案
* 使用 --onefile 參數可以將所有程式碼和相依的檔案打包成單一的可執行檔，而不是多個檔案。
* 使用 --icon=your_icon.ico 參數可以指定可執行檔的圖示。
* 使用 --name=your_app_name 參數可以指定生成的可執行檔的名稱。

```commandline
pyinstaller -F main.py
```
