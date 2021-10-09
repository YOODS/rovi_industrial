# UR対応
# UR対応

## 追加パッケージのインストール

- RTDE  
RTDE(RealTime Data EXchange)はUR社が提供する、データ授受プロトコルです。UR社はCライブラリのみ提供していますが、https://gitlab.com/sdurobotics/ur_rtde がPythonラッパーを公開しているので、簡単に利用できます。
~~~
pip install ur-rtde --user
~~~
- ur-description  
Ros Industrialが、提供しているもの( https://github.com/ros-industrial/universal_robot )をベースに、当社にて以下の改編を行って公開しています。
  - VTに不要なパッケージを除外
  - 長さの単位をmmに変更

  インストールはcatkin_ws\src以下で
~~~
git clone https://github.com/YOODS/ur_min.git
~~~

