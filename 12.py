# -*- coding: utf-8 -*-
"""
2次元運動のシミュレーション
電界中の荷電粒子のシミュレーション
matplotlibによるグラフ描画機能付き
def を使った例

"""
# モジュールのインポート
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import math

fig = plt.figure()  # 描画全体の領域を確保する。
ax = plt.axes()  # 描画するデータを与える
ims = []  # グラフ画像の格納

# 定数
Q = (((0.0, 0.0), 15.0), ((5.0, -5.0), 10.0), ((-5.0, 5.0), -10.0))  # 電荷の位置と値
TIMELIMIT = 20.0  # シミュレーション打ち切り時刻
RLIMIT = 0.1  # 距離rの最低値
H = 0.01  # 時刻の刻み幅
G = (2, -8)  # Goalの中心座標
Goal = 0.5  # Goal判定の距離

# メイン実行部
t = 0.0  # 時刻t

# 電荷位置のプロット
for qi in Q:
    plt.plot(qi[0][0], qi[0][1], ".")

plt.plot(G[0], G[1], "o")  # Goalの中心座標のプロット
c = patches.Circle(xy=G, radius=Goal, ec='b', fill=False)  # Goal の円
ax.add_patch(c)  # Goal の円の貼り付け
ax.set_aspect('equal')  # グラフを等倍率に指定

# 係数の入力
vx = 0
vy = 0
x = 4
y = 4

print("{:.7f} {:.7f} {:.7f} {:.7f} {:.7f}".format(t, x, y, vx, vy))
# 現在時刻と現在の位置
# グラフデータに現在位置を追加
xlist = [x]
ylist = [y]

t2 = 0  # 処理回数のカウント


# 粒子の位置の速度
def particle(x1, y1, rmin, vx, vy):
    rx = x1 - x  # 距離rxの計算
    ry = y1 - y  # 距離ryの計算
    r = math.sqrt(rx * rx + ry * ry)  # 距離rの計算
    if r < rmin:
        rmin = r  # 距離の最小値を更新
    vx += (rx / r / r / r * qi[1]) * H  # 速度vxの計算
    vy += (ry / r / r / r * qi[1]) * H  # 速度vyの計算
    return vx, vy, rmin


# 2次元運動の計算
while t < TIMELIMIT:  # 打ち切り時間まで計算
    t = t + H  # 時刻の更新
    t2 += 1
    rmin = float("inf")  # 距離の最小値を初期化
    for qi in Q:
        vx, vy, rmin = particle(qi[0][0], qi[0][1], rmin, vx, vy)

    x += vx * H  # 位置xの計算
    y += vy * H  # 位置yの計算
    # print("{:.7f} {:.7f} {:.7f} {:.7f} {:.7f}".format(t, x, y, vx, vy))
    # 現在時刻と現在の位置
    xlist.append(x)
    ylist.append(y)
    # グラフの描画（10回置き）
    if t2 % 10 == 0:
        im = plt.plot(x, y, color='g', marker='o')

        ims.append(im)
    if rmin < RLIMIT:
        break  # 電荷に非常に近づいたら終了

    if abs(math.sqrt(x**2 + y**2) - math.sqrt(G[0]**2 + G[1]**2)) < Goal/2:
        break

# グラフの表示
ani = animation.ArtistAnimation(fig, ims, interval=10)
ani.save('anim.gif', writer="ffmpeg")
plt.plot(xlist, ylist)  # グラフをプロット
plt.show()
