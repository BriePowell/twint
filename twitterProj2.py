import twint
import nest_asyncio
nest_asyncio.apply()

c = twint.Config()
hashtag = "welcomehomeharryandmeghan"

c.Search = hashtag
c.Since = "2022-09-05"
c.Until = "2022-09-28"
c.Count = True
c.User_full = True
c.Output = ".\outputs\data_welcome01.json"
twint.run.Search(c)
