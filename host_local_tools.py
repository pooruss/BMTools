import bmtools
import os

server = bmtools.ToolServer()
print(server.list_tools())
server.load_tool("weather")
# server.load_tool("database")
server.load_tool("chemical-prop")
server.load_tool("douban-film")
server.load_tool("wikipedia")
server.load_tool("wolframalpha")
server.load_tool("bing_search", {"subscription_key": os.getenv("BING_SUBSCRIPT_KEY", None)})
server.load_tool("office-ppt")
server.load_tool("stock", {"subscription_key": os.getenv("ALPHA_VANTAGE_KEY", None)})
server.load_tool("bing_map", {"subscription_key": os.getenv("BING_MAP_KEY", None)})
server.load_tool("baidu_map", {"subscription_key": os.getenv("BAIDU_MAP_KEY", None), "baidu_secret_key": os.getenv("BAIDU_SECRET_KEY", None)})
server.load_tool("google_scholar", {"subscription_key": os.getenv("SERPAPI_KEY", None)})
server.load_tool("zillow", {"subscription_key": os.getenv("RAPIDAPI_KEY", None)})
server.load_tool("airbnb", {"subscription_key": os.getenv("RAPIDAPI_KEY", None)})
server.load_tool("job_search", {"subscription_key": os.getenv("RAPIDAPI_KEY", None)})
# server.load_tool("nllb-translation")
server.load_tool("baidu-translation")
server.load_tool("tutorial")
server.load_tool("file_operation")
server.load_tool("meta_analysis")
server.load_tool("code_interpreter")
server.load_tool("arxiv")
server.load_tool("google_places")
server.load_tool("google_serper")
server.load_tool("python")
server.load_tool("sceneXplain")
server.load_tool("shell")
server.load_tool("image_generation")
server.serve()