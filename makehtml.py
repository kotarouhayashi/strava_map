# パッケージのインポート
import folium
import glob
import gpxpy
from folium.plugins import HeatMap

# foliumを使用して、地図を作成 (初期表示は、緯度37.0、経度139.0、拡大率4倍)
map = folium.Map(location=[37, 139],zoom_start=4,tiles="Stamen Terrain", max_zoom=8)
points = []

# StravaのGPXファイルを読み込み。
for gpx_file in sorted(glob.glob("data/activities/*.gpx")):
    with open(gpx_file, 'r') as f:
        gpx = gpxpy.parse(f)
        for track in gpx.tracks:
          for segment in track.segments:
              for point in segment.points:
                  points.append([point.latitude, point.longitude])

# GPXファイルからトレースデータを抽出し、地図上に表示
folium.PolyLine(points, color='cyan').add_to(map)
HeatMap(points, radius=8).add_to(map)

# 地図をHTMLファイルとして保存
map.save("map.html")