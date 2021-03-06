## Chapter 1. 工具的安裝與熟悉 [內容](ch1/README.md)
### Python 簡介
+ Python 是什麼
  - Python 於1991年發表，是一種高階的直譯式物件導向語言！
  - 作者：Guido van Rossum，人稱「仁慈的獨裁者」（Benevolent Dictator For Life, BDFL）！
  - 強調程式可讀性及簡潔的語法！
  - 使用縮排的方式來劃分程式碼區塊。
  - 廣泛應用於資料分析、機器學習、網站開發、桌面應用程式及自動化腳本等。
+ Python優點
  - 簡潔易學：語法簡潔且可讀性佳，學習時非常好上手。
  - 跨平台：可於Mac、Linux及Windows上運行和開發。
  - 可讀性佳：Python官方有一份用來規範Python程式碼撰寫風格文件(PEP8 - Style Guide for Python Code)，開發人員可以遵循通用原則，提高程式碼內容的可讀性。
  - 豐富的免費函式庫：Python擁有許多強大的函式庫，可輕鬆引入，快速完成複雜任務：
    - Numpy -- 提供高效能的多維陣列與矩陣運算，普遍使用於科學運算領域。
    - Scrapy -- 是一個開源的函式庫，用來建立網頁爬蟲、資料採礦(Data mining)及自動化測試等。
    - Matplotlib - Python 2D繪圖函式庫，主要運用於資料的視覺化。

### 平台選擇

### 開發工具
+ 使用 Visual Studio Code
  + 安裝 VSCode
  + 配置 Python 工具
    + 使用 Extensions 安裝 Python
      ```python
      <Ctrl>+<Shift>+<X>
      查詢方框中，輸入「Python」
      選擇第一個項目，按下「Install」
      ```
    + 選擇 Python 解譯器
      ```python
      <Ctrl>+<Shift>+<P>
      執行：Python: Select Interpreter
      選擇需要的解譯器
      ```
  + 開始第一個程式
    + 開一個新的檔案
    + 輸入下列程式碼
      ```python
      msg = "Hello World"
      print(msg)
      ```
    + 存成 hello.py 
    + 執行程式碼
      ```python
      右上方的綠色箭頭符號
      or
      在檔案空白處，按下滑鼠右鍵，可以選擇單行執行
      or
      在 Explorer 中，針對檔案按下滑鼠右鍵，可以選擇「Run Python File in Terminal」
      or 
      使用滑鼠拖選想要執行的程式碼區塊，再按下<Shift>+<Enter>即可區域執行
      or
      使用 <Ctrl>+<Shift>+<P>，輸入 Python: Start REPL 可呼叫 Terminal 視窗執行
      or
      檔案空白處，按下滑鼠右鍵，選擇「Run Current File in Python Interactive Window」(可能需要安裝一些軟體)
      ```

### 開始使用

#### 參考文獻
[Python之父心很累，宣布永久卸下「仁慈的獨裁者」重任](https://www.ithome.com.tw/news/124556)