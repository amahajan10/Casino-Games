class DealerAI:
    def __init__(self, dealer_score):
        self._dealer_score = dealer_score

    @property
    def dealer_score(self):
        return self._dealer_score

    @dealer_score.setter
    def dealer_score(self,val):
        self._dealer_score = val

    def do_hit(self):
        if int(self._dealer_score) > 17:
            return False
        else:
            return True
