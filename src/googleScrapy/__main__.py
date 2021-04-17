from googleScrapy import Google

if __name__ == '__main__':

    query = input('enter google search query\n')

    results = Google().search(query)

    print(results['status_code'])

    print(results['links'])