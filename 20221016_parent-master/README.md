### 「赤外線リモコン」タブについて
![](http://www.kodai.uec.ac.jp/blocks_img/UR/sample.png)
#### 図. 配線図

![](http://www.kodai.uec.ac.jp/blocks_img/UR/real.png)
#### 図. 実際の配線状況

#### 1. 概要
　このカスタムブロックは、ライトをコントロールするもので、
ON/OFF, 色の指定等を行うブロックです。赤外線LEDと抵抗（ここでは200Ω）を利用して,
配線図のように配線することで演習ができます。
配線図は演習用のため数十センチ～１ｍ程度の距離を想定しています。
「ずっと」のブロックに直接繋げることは可能ですが、動かなくなりますので繋げないようにしてください。
<!-- 　このカスタムブロックは、SALKING社のタッチライト（４色対応）をコントロールするもので、
ON/OFF, 色の指定等を行うブロックです。赤外線LEDと抵抗（ここでは200Ω）を利用して,
配線図のように配線することで演習ができます。
配線図は演習用のため数十センチ～１ｍ程度の距離を想定しています。
「ずっと」のブロックに直接繋げることは可能ですが、動かなくなりますので繋げないようにしてください。 -->

#### 2. ブロックの説明
- ##### ライトを点ける  
![](http://www.kodai.uec.ac.jp/blocks_img/UR/light_on.png)
ライトの電源を入れます。
ライトを点けたときの色は、ライトを消す直前の色となります。
このブロック以外で、ライトを点けることはできません。  
micro:bitの画面には[1]が表示されます。  


- ##### ライトを消す/白にしてライトを消す  
![](http://www.kodai.uec.ac.jp/blocks_img/UR/light_off.png)
![](http://www.kodai.uec.ac.jp/blocks_img/UR/light_off2.png)
ライトの電源を落とします。
ただし、「白にしてライトを消す」ブロックでは、
次にライトを点けるときの色を白にするために、
ライトの色を一度白に変えてから消します。  
micro:bitの画面には[0]が表示されます。


- ##### ライトの明るさを変える  
![](http://www.kodai.uec.ac.jp/blocks_img/UR/light_brighter.png)
パラメーター: 明るくする・暗くする  
ライトの明るさを変化させます。
明るさは4段階あります
ライトの初期の明るさは4なので、ライトを暗くしてからでないと、明るくなりません。  
ただし、ライトの色が白の時のみ有効。  
明るくする: micro:bitの画面には[+]が表示されます。  
暗くする　: micro:bitの画面には[-]が表示されます。


- ##### 色を変える   
![](http://www.kodai.uec.ac.jp/blocks_img/UR/light_change.png)
パラメーター: 赤・青・緑・橙・碧・藍・黄・水・紫・空・桃・白・電球
ライトの色を変化させます。
ライトが点いている状態でのみ、動作します。
ライトの色を赤・青・緑・橙・碧・藍・黄・水・紫・空・桃・白・電球に変えます。
別の色へと上書き可能。  
micro:bitの画面には、それぞれ [R], [B], [G], [O], [E], [I], [Y],
[A], [Pu], [S], [Pi], [W], [L]が表示されます。


- ##### グラデーション
![](http://www.kodai.uec.ac.jp/blocks_img/UR/light_change16)
パラメーター: 普通・スムーズ・ゆっくり・ストロボ 
ライトの色が順に変化するようになります。
順番は以下の通り
赤 → 橙 → 黄 → 黄緑 → 緑 → 碧 → 水 → 空 → 青 → 藍 → 紫 → 桃 → 白 → 赤
ストロボのみ色の種類が三色
赤 → 緑 → 青

普通　　: micro:bitの画面には[N]が表示されます。
スムーズ: micro:bitの画面には[G]が表示されます。
ゆっくり: micro:bitの画面には[S]が表示されます。
ストロボ: micro:bitの画面には[T]が表示されます。

#### 3. 使用例
![](http://www.kodai.uec.ac.jp/blocks_img/UR/light_exp.png)



> Open this page at [https://sabu006.github.io/20221016_parent/](https://sabu006.github.io/20221016_parent/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/sabu006/20221016_parent** and import

## Edit this project ![Build status badge](https://github.com/sabu006/20221016_parent/workflows/MakeCode/badge.svg)

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/sabu006/20221016_parent** and click import

## Blocks preview

This image shows the blocks code from the last commit in master.
This image may take a few minutes to refresh.

![A rendered view of the blocks](https://github.com/sabu006/20221016_parent/raw/master/.github/makecode/blocks.png)

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
