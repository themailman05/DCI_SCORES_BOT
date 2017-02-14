

class ApiWrapper():
    def __init__(baseurl='https://bridge.competitionsuite.com/api'):
        self.baseurl = baseurl
    def getSeasons(org_code='96b77ec2-333e-41e9-8d7d-806a8cbe116b'):
        url = '/orgscores/GetCompetitionsByOrganization/jsonp?organization="{0}"&version="1.1.5"'.format(org_code)
        seasons = http_get(url)
        return seasons
    def getScores(season_code, org_code)
        seasonprefix = '/orgscores/GetSeasons/jsonp?organization="{0}"&version="1.1.5"&season="{1}"'
        url = seasonprefix.format(org_code, season_code)
        scores = http_get(url)
        return event
    def getEvent(comp_code):
        event_prefix = '/orgscores/GetCompetition/jsonp?competition={0}&version=1.1.5'
        url = event_prefix.format(comp_code = comp_code)
        event = http_get(url):
        return event
