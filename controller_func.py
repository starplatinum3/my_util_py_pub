import requests

@api_view([{method}])
def {func_name}(request):
    
    url = "https://login.salesforce.com/services/oauth2/token"

    payload='grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion='
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)