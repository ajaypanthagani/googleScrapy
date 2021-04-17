# googleScrapy

* response structure:

```python
{
    'status_code' : status_code, #Eg. 200, 429, 500
    'links' : [link1, link2, link3] #Eg. https://example.com
}
```

* Usage:

```python
from googleScrapy import Google

response = Google().search('search query goes here')

if response.status_code == 200:
    print('fetched succesfully')
    for link in response.links:
        print(link)
else:
    print(f'Error, status code: {response.status_code}')
```

* Free Software: MIT License