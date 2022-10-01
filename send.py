import requests


class SignalAdsApi(object):
    def __init__(self):
        self.host = 'http://192.168.1.198:8000/api/v1'
        self.api_key = ''

    def set_api_key(self, api_key):
        self.api_key = api_key

    def send_single_sms(self, sender, text, receptor):
        body = {'sender': sender, 'text': text, 'receptor': receptor}
        result = requests.post(self.host + '/' + self.api_key + '/send', body)
        return result.json()

    def send_multiple_sms(self, sender, text, receptors):
        body = {'sender': sender, 'text': text, 'receptors': receptors}
        result = requests.post(self.host + '/' + self.api_key + '/sendGroup', body)
        return result.json()

    def send_pair_to_pair_sms(self, sender, pairs):
        body = {'sender': sender, 'message': pairs}
        result = requests.post(self.host + '/' + self.api_key + '/sendPair', body)
        return result.json()

    def send_sms_with_pattern(self, sender, pattern_id, pattern_params, receptors):
        body = {'sender': sender, 'pattern_id': pattern_id, 'pattern_params': pattern_params, 'receptors': receptors}
        result = requests.post(self.host + '/' + self.api_key + '/messages/send-pattern', body)
        return result.json()

    def get_account_credit(self):
        result = requests.get(self.host + '/' + self.api_key + '/credit')
        return result.json()
