# ミニプロジェクト: パスワードポリシーチェッカー

**トピック:** 変数 · 条件分岐 · ループ · 文字列 · 集合 (set) · 関数

## 概要

次のすべてのルールをパスワードが満たしているかどうかを確認するCLIツールを作成します。

1. 8文字以上であること
2. 小文字を1つ以上含むこと
3. 大文字を1つ以上含むこと
4. 数字 (0〜9) を1つ以上含むこと
5. 特殊文字 (英字でも数字でもない文字) を1つ以上含むこと
6. よくあるパスワード上位10件のいずれでもないこと

## 出力例

```
python3 password_policy_checker.py Helloworld1!
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
✅ Contains special characters
✅ Is not common

python3 password_policy_checker.py password
✅ Has 8 or more characters
✅ Contains lower-case characters
❌ Contains upper-case characters
❌ Contains numeric characters
❌ Contains special characters
❌ Is not common
```

## マイルストーン

### 1. コマンドライン引数を受け取る

パスワードを最初のコマンドライン引数として読み取り、出力します。

**出力例**

```
python3 password_policy_checker.py hello
hello
```

### 2. ルール1 — 長さ

パスワードが8文字以上かどうかを出力します。

**出力例**

```
python3 password_policy_checker.py longpassword
✅ Has 8 or more characters

python3 password_policy_checker.py hi
❌ Has 8 or more characters
```

### 3. ルール2 — 小文字

パスワードが小文字を1つ以上含むかどうかを出力します。

**出力例**

```
python3 password_policy_checker.py helloworld
✅ Has 8 or more characters
✅ Contains lower-case characters

python3 password_policy_checker.py HELLOWORLD
✅ Has 8 or more characters
❌ Contains lower-case characters
```

### 4. ルール3 — 大文字

パスワードが大文字を1つ以上含むかどうかを出力します。

**出力例**

```
python3 password_policy_checker.py Helloworld
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters

python3 password_policy_checker.py helloworld
✅ Has 8 or more characters
✅ Contains lower-case characters
❌ Contains upper-case characters
```

### 5. ルール4 — 数字

パスワードが数字を1つ以上含むかどうかを出力します。

**出力例**

```
python3 password_policy_checker.py Helloworld1
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters

python3 password_policy_checker.py Helloworld
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
❌ Contains numeric characters
```

### 6. ルール5 — 特殊文字

パスワードが特殊文字 (英字でも数字でもない文字) を1つ以上含むかどうかを出力します。

**出力例**

```
python3 password_policy_checker.py Helloworld1!
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
✅ Contains special characters

python3 password_policy_checker.py Helloworld1
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
❌ Contains special characters
```

### 7. ルール6 — よくあるパスワード

パスワードがよくあるパスワード上位10件に含まれていないかどうかを出力します。

**出力例**

```
python3 password_policy_checker.py Helloworld1!
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
✅ Contains special characters
✅ Is not common

python3 password_policy_checker.py password
✅ Has 8 or more characters
✅ Contains lower-case characters
❌ Contains upper-case characters
❌ Contains numeric characters
❌ Contains special characters
❌ Is not common
```

## ヒント

- `for c in p:` を使って文字列の各文字をループ処理できます。
- よくあるパスワードのブロックリストへの所属判定には、Pythonの集合 (set) が適しています。
