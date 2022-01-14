from full_text_query import FullTextQuery


class Query(FullTextQuery):
    def hello():
        print()


query = Query().match(field="test", search="hello word")
print(query)
