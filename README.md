# Bust Cup Measurement Script v1.0

モデルのエッジを選択して、バストカップ数を測ることができるスプリクト
作成:Miru(mirumoru),ChatGPT-3.5,ChatGPT‑4o 


###《導入方法》
Maya2023で起動確認しました。
ドキュメントファイルにあるmayaのスプリクトファイルに「measure」を入れる。
mayaのスプリクトエディターで「import_measure.py」を読み込み。
※PyMELがインストールされている必要があります。インストールされていない場合は以下のサイトを参考にインストールしてください。
https://mononoco.com/creative/maya/2023-pymel

###《使い方》
上記で読み込んだpyを起動するとGUIが表示されます。
主にEdgeの方を使います。Vertexはおまけです。
単位はmayaの設定によって変わりますがcmにしないとカップサイズ(AAA～Jまで)が測れません。


1.トップにあるエッジを全て選択してTopの横にある「Measure Edge Distance」をクリックします。
すると、選択されたエッジの長さが入力されます。

2.次にアンダーにあるエッジを全て選択してUnderの横に「Measure Edge Distance」をボタンをクリックします。
すると、選択されたエッジの長さが入力されます。

3.両方の長さがはかれたら「Result」ボタンをクリックします。
すると、TopとUnderの長さを引いた値が入力されます。

4.最後に「Bust Cup」をクリックするとおおよそのバストカップが入力されます。


###《おまけ》
Vertexは2の頂点を選択するとその距離を測ることができます。
バストカップ数測定スクリプト(未使用)は「美少女、バストカップ数測定スクリプト」(http://negifukyu.x.fc2.com/bustcheck/cupchecker.html)
をmayaのスプリクトエディターからできるように変換したものです。元々はこれを使う予定でしたがふと思った時、使う必要が無いことに気付き使わなくなったコードです。

・スペシャルサンクス　音伎

###《ライセンス》
MITライセンスです。
ファイルの改変、配布も可能です。ただし、このReadmeを同封してください。(連絡の必要はありません)

###《更新内容》

2024年5月17日 v1.0