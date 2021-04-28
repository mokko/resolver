from starlette.responses import RedirectResponse, JSONResponse
from starlette.applications import Starlette
from starlette.routing import Route

"""
Redirect from sourceURL to targetURL

sourceURL has type
http://smb-digital.de/eMuseumPlus?service=ExternalInterface&module=collection&objectId=778401&viewType=detailView

The sourceURL contains 4 elements
baseURL: http://smb-digital.de/eMuseumPlus (required)
service: service=ExternalInterface (required)
module:collection (required)
objectId:778401 (required)
viewType:detailView (optional)

targetURL has this form: https://recherche.smb.museum/detail/212315
"""

def resolver(request):
    if request.query_params['service'] == "ExternalInterface" and \
    request.query_params['module'] == "collection" and \
    "objectId" in request.query_params:
        objId = request.query_params['objectId']
        new_url = f"https://recherche.smb.museum/detail/{objId}"
        return RedirectResponse(url=new_url)
    else:
        return JSONResponse({'no': 'redirect'})

app = Starlette(debug=True, routes=[ 
    Route('/eMuseumPlus', resolver)] #defaults to get
)

