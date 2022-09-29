import twint
import nest_asyncio
nest_asyncio.apply()

c = twint.Config()
hashtag = "#GoHomeMeghanMarkle"

c.Search = hashtag
c.Since = "2022-09-04"
c.Until = "2022-09-20"
c.Count = True
c.User_full = True
c.Output = "..\outputs\data.json"
twint.run.Search(c)
