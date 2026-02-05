# 密碼產生器

[English](./README.md)

這是一個命令列工具，根據使用者輸入的長度來建立安全的密碼。程式會混合字母、數字和符號，以確保隨機性。

建立這個專案是為了練習 Python 基礎語法與使用技巧，特別是字串操作和運用內建的函式庫。

# 功能特色
自訂長度：使用者可以輸入確切的字元數量。

隨機化：使用 Python 的 `random` 模組來產生不可預測的結果。

即時輸出：立即產生並顯示密碼。

錯誤處理：確保使用者的輸入是有效的。

# 執行方式
1. 確認 Python 已經安裝在你的電腦上。
   
   ```bash
   python3 -V
   ```

2. 下載或 Clone 此儲存庫。
   
   ```bash
   git clone ssh://git@codeberg.org/JurisByte/Generator.git
   ```

3. 進入專案資料夾。
   
   ```bash
   cd Generator/
   ```

4. 執行程式。
   
   ```bash
   python3 main.py
   ```