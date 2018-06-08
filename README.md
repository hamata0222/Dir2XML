# Dir2XML.py
指定したディレクトリのサブディレクトリも含めて、ディレクトリ構造をXMLとしてファイルに出力します。
## 使い方
引数にディレクトリを指定して実行します。

```
C:\example\python>Dir2XML.py C:\project\root
```

引数を指定せずに実行すると、対話式のUIでディレクトリの入力を求められます。

```
C:\example\python>Dir2XML.py
Please input the directory path which is as root: 
C:\project\root
```

## 結果
出力結果のXMLは、デフォルトでは``result.xml``という名前で指定されたディレクトリ直下に保存します。

``group``タグがディレクトリを表します。
``file``タグの``name``は指定したディレクトリ（``$PROJ_DIR$``）からの相対パスで表します。

```
<root>
  <group>
    <name>SubDir1</name>
    <group>
      <name>SubDir2</name>
      <file>
        <name>$PROJ_DIR$\SubDir1\SubDir2\file4.txt</name>
      </file>
    </group>
    <file>
      <name>$PROJ_DIR$\SubDir1\file3.txt</name>
    </file>
  </group>
  <file>
    <name>$PROJ_DIR$\file1.txt</name>
  </file>
  <file>
    <name>$PROJ_DIR$\file2.txt</name>
  </file>
</root>
```
