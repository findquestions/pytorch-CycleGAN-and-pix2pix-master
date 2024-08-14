import visdom

# 尝试连接到 Visdom 服务器
try:
    vis = visdom.Visdom(port=8097)
    assert vis.check_connection(), "Visdom 服务器连接失败。请确保 Visdom 服务器已启动。"
except Exception as e:
    print(f"无法连接到 Visdom 服务器: {e}")
    # 你可以选择在这里启动服务器或者进行其他处理

# 如果连接成功，可以继续进行后续的可视化操作
if vis.check_connection():
    # 示例：创建一个简单的散点图
    vis.scatter(X=[[1, 2], [3, 4]], opts=dict(title="示例散点图"))
else:
    print("Visdom 服务器不可用，跳过可视化部分。")
