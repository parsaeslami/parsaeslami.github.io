from requests import post

def get_data(tag):
    response = post('http://tinywebdb.appinventor.mit.edu/getvalue', data={"tag" : tag})
    response = response.json()

    return response