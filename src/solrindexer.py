import json
import urllib.parse
import urllib.request

solr_url = 'http://192.168.33.10:8983/solr/#/'

opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def load(collection,data):
    # Solrへデータを登録するリクエストを作成
    req = urllib.request.Request(
        url = '{0}/{1}/update'.format(solr_url,collection),
        data = json.dump(data).encode('utf-8'),
        headers = {'content-type':'application/json'}
    )

    # データの登録を実行
    with opener.open(req) as res:
        # データ確認
        print(res.read().decode('utf-8'))

    # コミット
    url = '{0}/{1}/update?softCommit=true'.format(solr_url,collection)
    req = urllib.request.Request(url)
    with opener.open(req) as res:
        print(res.read().decode('utf-8'))
