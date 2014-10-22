# Permutation

## 前置き

この度は私が Twitter 上で軽々しく「○○できない？（後述）」と言って  
多くの人の貴重な時間を奪ったことを反省しております。  
せめてもの罪滅ぼしで、皆様にいただいた知見をここに残しておきます。

## 問題設定

長さ n の配列 a と順列 p が与えられたとき、  
a を p 順に並べ替えて得られる配列を p(a) とします。  

つまり、p(a) を得る関数を愚直に書くと以下のようになります。

    def permuate(a, p):
        return [ a[ p[i] ] for i in xrange( len(a) ) ]

今 sizeof(a[i]) を d とすれば、  
この関数は dn bits の補助領域を利用して  
O(n) の時間計算量で並べ替えを達成することになります。  

ここで以下の疑問が生じるわけです。

「a から p(a) への並べ替えは、n に依存しない補助領域のみで O(n) の時間計算量で可能か」

この疑問にチャレンジして下さった人たちがいるので  
感謝の気持ちを込めてここに紹介します。


## 方法1 : [beam2d][beam2d] 法

    def permutate_beam2d(a, p):
        for i in xrange(len(a)):
            t, p[i] = p[i], a[i]           # escape p[i] -> t and a[i] -> p[i]
            a[i] = a[t] if t > i else p[t] # change a[i] to (escaped) target value

この手法のポイントは、  
a[i] を書き換えるときにその値を p[i] に待避することです。  

これで a[i] を a[ p[i] ] に書き換えようとしたときに  
既に a[ p[i] ] が変更されていても  
代わりに p[ p[i] ] から値をとれるという寸法です。  

この方法は a のみではなく、p も破壊します。  
また a の要素は p に待避可能であると仮定します。  
つまり sizeof(a[i]) > sizeof(p[i]) であるときには、  
s = sizeof(a[i]) - sizeof(p[i]) とすれば、  
sn bit の補助領域を必要とすることになります。


## 方法2 : [Darsein][Darsein] 法

    def permutate_Darsein(a, p):
        n = len(a)

        # permutate a
        for i in xrange(n):
            # permuate cycle starting with i
            j = i
            while p[j] < n:
                k = p[j]     # next point
                if k != i: a[j], a[k] = a[k], a[j] # swap if not starting point
                p[j] = k + n # mark as visited
                j = k        # move to next

        # recover p
        for i in xrange(n):
            p[i] -= n

この方法は beam2d 法と異なり p を書き換えはするものの、
ちゃんと最初の状態に復元することが可能です。

この方法のポイントは、  
a[i] を変更した時に p[i] に n を加えることで  
p[i] >= n ならば a[i] は編集済みであるというフラグを立てる点です。  

順列はいくつかの cyclic な部分順列に分割できます。  
その cycle に添って a[i] を変更する場合、補助領域は不要です。  
よって cycle の数だけ cycle に添った変更を行えば良いわけです。  
すべての変更終了後に各 p[i] から n を引けばもとの p に戻ります。

この手法が仮定していることは、  
各 p[i] に n を加算できることです。  
つまり各 p[i] は log n bit の余裕がある、  
言い換えれば n log n bit の補助領域を仮定していることになります。  
フラグを立てるだけなら n bit あればできるので、  
この手法は n bit の補助領域を使うことになります。

## まとめ

方法1は a の値を p に待避可能と仮定すれば p を破壊するが O(n) で並べ替え可能。  
方法2は n bit の補助領域があれば p を破壊することなく O(n) で並べ替え可能。  

つまり最初の疑問にはまだ答えられていない状態です。  

興味ある人は考えてみてね！  
[beam2d][beam2d] さん、[Darsein][Darsein] さんありがとう！  
他にも挑戦してくださった方々、ありがとう！

[beam2d]: https://twitter.com/beam2d "beam2d"
[Darsein]: https://twitter.com/Darsein "Darsein"
